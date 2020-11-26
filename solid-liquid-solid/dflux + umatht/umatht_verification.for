      SUBROUTINE UMATHT(U,DUDT,DUDG,FLUX,DFDT,DFDG,
     1 STATEV,TEMP,DTEMP,DTEMDX,TIME,DTIME,PREDEF,DPRED,
     2 CMNAME,NTGRD,NSTATV,PROPS,NPROPS,COORDS,PNEWDT,
     3 NOEL,NPT,LAYER,KSPT,KSTEP,KINC)
C
      INCLUDE 'ABA_PARAM.INC'

C
      CHARACTER*80 CMNAME
      DIMENSION DUDG(NTGRD),FLUX(NTGRD),DFDT(NTGRD),
     1 DFDG(NTGRD,NTGRD),STATEV(NSTATV),DTEMDX(NTGRD),
     2 TIME(2),PREDEF(1),DPRED(1),PROPS(NPROPS),COORDS(3),
     3 TABLE_K(2,20),TABLE_C(2,20)

      REAL*8 TempatTdT,TMEP,DTEMP,TABLE_K,TABLE_KP,TABLE_C,
     1 asoltemp, aliqtemp, alatht, TempatT, deltu, DTIME, DTDTIME,
     2 Mat_ID

C     Solidus Temperature
      asoltemp = PROPS(1)
C     Liquidus Temperature
      aliqtemp = PROPS(2)
C     Latent Heat of Fusion
      alatht = PROPS(3)

C     Conductivity of Solid
      DATA TABLE_K/ 6.2,20.0,6.635068493,100.0,7.17890411,200.0,7.722739726,300.0, 
     &8.266575342,400.0,8.810410959,500.0,9.354246575,600.0,9.898082192,700.0, 
     &10.17,750.0,10.44191781,800.0,10.98575342,900.0,10.50239726,995.0, 
     &12.07342466,1100.0,12.61726027,1200.0,13.16109589,1300.0,13.70493151,1400.0, 
     &14.24876712,1500.0,14.79260274,1600.0,15.06452055,1650.0,15.0917,1655.0/

C     Specific Heat
      DATA TABLE_C/5.46E+08,25, 5.62E+08,100,5.84E+08,200,6.06E+08,300,
     &6.29E+08,400,6.51E+08,500,6.73E+08,600,6.94E+08,700,
     &7.14E+08,800,7.34E+08,900,6.41E+08,995,6.60E+08,1100, 
     &6.78E+08,1200,6.96E+08,1300,7.14E+08,1400,7.32E+08,1500,
     &7.50E+08,1600,7.59E+08,1650,8.30E+08,1651,8.30E+08,1903/
     
      INC = 0
      INC1 = 0
      INC2 = 0

c                    
      TempatTdT = temp+dtemp
      TempatT = temp 

C     Conductivity of Solid
      IF (TempatTdT .LE. TABLE_K(2,1)) THEN
        COND = TABLE_K(1,1)
        DCOND = 0.d0
      ELSEIF (TempatTdT .GE. TABLE_K(2,20)) THEN
        COND = TABLE_K(1,20)
        DCOND = 0.d0
      ELSEIF (TempatTdT .GT. TABLE_K(2,1) .AND. TempatTdT .LT. TABLE_K(2,20)) THEN
        DO K1=1,19
          TL1 = TABLE_K(2, K1+1)
          IF (TempatTdT .LT. TL1 .AND. INC1 .EQ. 0) THEN
            TL0 = TABLE_K(2,K1)
            DT = TL1-TL0
            C0 = TABLE_K(1,K1)
            C1 = TABLE_K(1,K1+1)
            DC = C1-C0
            DCOND = DC/DT
            COND = DCOND*(TempatTdT-TL0)+C0
            INC1 = 1
          ENDIF
        END DO
      END IF
C
C     Specific Heat
C
      IF (TempatTdT .LE. TABLE_C(2,1)) THEN
        SPECHT = TABLE_C(1,1)
      ELSEIF (TempatTdT .GE. TABLE_C(2,20)) THEN
        SPECHT = TABLE_C(1,20)
      ELSEIF (TempatTdT .GT. TABLE_C(2,1) .AND. TempatTdT .LT. TABLE_C(2,20)) THEN
        DO K1=1,19
          TL1 = TABLE_C(2, K1+1)
          IF (TempatTdT .LT. TL1 .AND. INC2 .EQ. 0) THEN
            TL0 = TABLE_C(2, K1)
            DT = TL1-TL0
            C2 = TABLE_C(1, K1)
            C3 = TABLE_C(1, K1+1)
            DCC = C3-C2
            SPECHT = (DCC/DT)*(TempatTdT-TL0)+C2
            INC2 = 1
          ENDIF
        END DO
      END IF

      DUDT = SPECHT
      deltu = DUDT*DTEMP   
C     
      ulatn1 = 0.0d0
      ulatn2 = 0.0d0
      ulatnp = 0.0d0
      slope = 0.0d0
      frac = 0.25d0
c                    
c     account for latent heat effects
c                                        
      if (TempatT  .gt. asoltemp .and. TempatT .lt. aliqtemp) then
         ulatn1 = (TempatT-asoltemp)*alatht/(aliqtemp-asoltemp)
      else if (TempatT .gt. aliqtemp) then
         ulatn1 = alatht
      end if
c                    
      if (TempatTdT .gt. asoltemp .and. TempatTdT .lt. aliqtemp) then
         ulatn2 = (TempatTdT-asoltemp)*alatht/(aliqtemp-asoltemp)
         slope = alatht/(aliqtemp-asoltemp)
      else if (TempatTdT .gt. aliqtemp) then
         ulatn2 = alatht
         slope = 0.0d0
      end if
c                    
      if (ulatn2 .ne. ulatn1) then
         deltu = deltu+ulatn2-ulatn1
         dudt = dudt+slope
         if (slope .eq. 0.d0) then
            tempp = TempatTdT-frac*dtemp
            if (tempp .gt. asoltemp .and. tempp .lt. aliqtemp) then
               ulatnp = (tempp-asoltemp)*alatht/(aliqtemp-asoltemp)
               slope = alatht/(aliqtemp-asoltemp)
            else if (tempp .gt. aliqtemp) then
               ulatnp = alatht
               slope=0.0d0
            end if
c                          
            if (ulatnp .ne. ulatn2) then
               dudt = dudt+slope
            end if
         end if
      end if
c      

      U = U+deltu

C     Heat FLUX
      DO I=1, NTGRD
        FLUX(I) = -COND*DTEMDX(I)
        DFDG(I, I) = -COND
        DFDT(I) = -DCOND*DTEMDX(I)
      END DO

      RETURN
      END


      SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP,
     1 TEMP,PRESS,SNAME)
C
      INCLUDE 'ABA_PARAM.INC'
C
      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME


      real*8 t,pi,phi,eta,U,Ib,v,S,x,y,z,x0,y0,z0,Hs,Iz
      t=time(2)
      pi=3.1415926
      phi = 0.55
      eta = 0.9
      U = 60.0e3
      Ib = 6.7
      v = 632.6
      S = 0.062
C     defining position parameters
      x=coords(1)
      y=coords(2)
      z=coords(3)
      x0 = 0.0 + v*t - phi
      y0 = 0.0 
      z0 = 10.07

      Hs = 2.0*U*Ib/(pi*phi**2.0)*exp(-2.0*((x-x0)**2.0 + (y-y0)**2.0)/phi**2.0)
      Iz = 1.0/0.75*(-2.25*((z0-z)/S)**2 + 1.5*((z0-z)/S) + 0.75)

      IF (z<=10.07 .AND. z>=10.008) THEN
            Uz = 1.0
      ELSE IF (z<10.008 .AND. z>=0.0) THEN
            Uz = 0.0
      END IF

      flux(1) = eta*Hs*Uz*Iz/S
      flux(2) = 0

      RETURN
      END
