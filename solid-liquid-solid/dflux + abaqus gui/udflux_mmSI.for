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
