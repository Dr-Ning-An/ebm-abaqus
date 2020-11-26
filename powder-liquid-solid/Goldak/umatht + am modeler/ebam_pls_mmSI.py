# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import os

Mdb()

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)
mdb.models['Model-1'].setValues(absoluteZero=-273.15, stefanBoltzmann=5.669e-11)

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=42.0)

mdb.models['Model-1'].sketches['__profile__'].rectangle(
    point1=(0.0, 0.0), 
    point2=(21.0, 2.5))

mdb.models['Model-1'].Part(
    dimensionality=THREE_D, 
    name='Part-1', 
    type=DEFORMABLE_BODY)

mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(
    depth=10.07, 
    sketch=mdb.models['Model-1'].sketches['__profile__'])

del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].parts['Part-1'].Set(
    edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((5.25, 0.0, 10.07), )), 
    name='Set-Nodes')

# Partition
plane1 = mdb.models['Model-1'].parts['Part-1'].DatumPlaneByPrincipalPlane(
    offset=10.0, 
    principalPlane=XYPLANE)

mdb.models['Model-1'].parts['Part-1'].PartitionCellByDatumPlane(
    cells=mdb.models['Model-1'].parts['Part-1'].cells, 
    datumPlane=mdb.models['Model-1'].parts['Part-1'].datums[plane1.id])

mdb.models['Model-1'].ConstrainedSketch(
    gridSpacing=1.16, 
    name='__profile__', 
    sheetSize=46.51, 
    transform=mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
        sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces.findAt((21.0/2.0, 0.0, 10.0/2.0), ), 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges.findAt((21.0, 0.0, 10.0/2.0), ), 
    sketchOrientation=RIGHT, 
    origin=(0.0, 0.0, 0.0)))

for i in range(450):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0+i*0.05, 10.07), 
        point2=(0.0+i*0.05, 10.0))    

########################################################################################

for j in range(3):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0, 10.0-j*0.05), 
        point2=(21.0, 10.0-j*0.05))

for i in range(150):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0+i*0.05*3, 10.0), 
        point2=(0.0+i*0.05*3, 10.0-4*0.05))    

for i in range(150):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.05+i*0.05*3, 10.0), 
       point2=(0.05+i*0.05*3, 10.0-3*0.05))
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.10+i*0.05*3, 10.0), 
       point2=(0.10+i*0.05*3, 10.0-3*0.05))
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.05+i*0.05*3, 10.0-3*0.05), 
       point2=(0.10+i*0.05*3, 10.0-3*0.05))
#
for i in range(150):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0 + 0.15*i, 10.0-4*0.05), 
        point2=(0.05 + 0.15*i, 10.0-3*0.05))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.1 + 0.15*i, 10.0-3*0.05), 
        point2=(0.15 + 0.15*i, 10.0-4*0.05))
##
for j in range(3):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0, 10.0-4*0.05 - j*0.15), 
        point2=(21.0, 10.0-4*0.05 - j*0.15))
##
for i in range(50):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0+i*0.45, 10.0-4*0.05), 
        point2=(0.0+i*0.45, 0.0))
##
for i in range(50):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.15 + i*0.45, 10.0-4*0.05), 
        point2=(0.15 + i*0.45, 10.0-4*0.05 - 0.15*1))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.30 + i*0.45, 10.0-4*0.05), 
        point2=(0.30 + i*0.45, 10.0-4*0.05 - 0.15*1))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.15 + i*0.45, 10.0-4*0.05 - 0.15*1), 
        point2=(0.30 + i*0.45, 10.0-4*0.05 - 0.15*1))
##
for i in range(50):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0 + 0.45*i, 10.0-4*0.05-2*0.15), 
        point2=(0.15 + 0.45*i, 10.0-4*0.05-1*0.15))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.3 + 0.45*i, 10.0-4*0.05-1*0.15), 
        point2=(0.45 + 0.45*i, 10.0-4*0.05-2*0.15))
##
for j in range(2):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0, 10.0-4*0.05 - 2*0.15 - j*0.45), 
        point2=(21.0, 10.0-4*0.05 - 2*0.15 - j*0.45))
#

##
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(
    faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(((21.0/2.0, 0.0, 10.0/2.0), ), ((21.0/2.0, 0.0, (10.07+10.0)/2.0), ), ), 
    sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges.findAt((21.0, 0.0, 10.0/2.0), ))
## 
mdb.models['Model-1'].parts['Part-1'].setMeshControls(
    regions=mdb.models['Model-1'].parts['Part-1'].cells, 
    technique=SWEEP)
#
mdb.models['Model-1'].parts['Part-1'].seedEdgeByNumber(
    constraint=FINER, 
    edges=mdb.models['Model-1'].parts['Part-1'].edges, number=1)
#
for i in range(421):
    mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(
        constraint=FINER, 
        edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0 + i*0.05, 0.0, (10.0+10.07)/2.0), )), 
        size=0.0175)

for i in range(421):
    mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(
        constraint=FINER, 
        edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0 + i*0.05, 0.0, (10.0+9.95)/2.0), )), 
        size=0.0175)   
#
for i in range(1,47):
    mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
        biasMethod=SINGLE, 
        constraint=FINER, 
        end1Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0 + i*0.45, 0.0, 1.975), ), ), 
        maxSize=0.9, 
        minSize=0.45)

mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0, 0.0, 1.975), ), ), 
    maxSize=0.9, 
    minSize=0.45)

mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((21.0, 0.0, 1.975), ), ), 
    maxSize=0.9, 
    minSize=0.45)

mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0, 0.625, 10.07), )), 
    maxSize=0.15, 
    minSize=0.05)

mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0, 0.625, 10.0), )), 
    maxSize=0.15, 
    minSize=0.05)

mdb.models['Model-1'].parts['Part-1'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-1'].cells)

mdb.models['Model-1'].parts['Part-1'].setElementType(
    elemTypes=(ElemType(elemCode=DC3D8, elemLibrary=STANDARD), ElemType(elemCode=DC3D6, 
      elemLibrary=STANDARD), ElemType(elemCode=DC3D4, elemLibrary=STANDARD)), 
    regions=(mdb.models['Model-1'].parts['Part-1'].cells, ))

###########
import csv

with open('Conductivity_Solid_mmSI_Fitted.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    TEMP_ConductivitySolid = [row[0] for row in reader]

with open('Conductivity_Solid_mmSI_Fitted.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    ConductivitySolidValue = [row[1] for row in reader]

with open('SpecificHeat_mmSI.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    TEMP_SpecificHeat = [row[0] for row in reader]

with open('SpecificHeat_mmSI.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    SpecificHeatValue = [row[1] for row in reader]

with open('Density_Solid_mmSI.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    Temp_DensitySolid = [row[0] for row in reader]

with open('Density_Solid_mmSI.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    DensitySolidValue = [row[1] for row in reader]

ConductivitySolidData = []
for i in range(len(TEMP_ConductivitySolid)):
   ConductivitySolidData.append((float(ConductivitySolidValue[i]), float(TEMP_ConductivitySolid[i]))) 

SpecificHeatData = []
for i in range(len(TEMP_SpecificHeat)):
   SpecificHeatData.append((float(SpecificHeatValue[i]), float(TEMP_SpecificHeat[i]))) 

DensitySolidData = []
for i in range(len(Temp_DensitySolid)):
   DensitySolidData.append((float(DensitySolidValue[i]), float(Temp_DensitySolid[i]))) 

with open('Density_Powder_mmSI.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    Temp_DensityPowder = [row[0] for row in reader]

with open('Density_Powder_mmSI.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    DensityPowderValue = [row[1] for row in reader]

DensityPowderData = []
for i in range(len(Temp_DensityPowder)):
   DensityPowderData.append((float(DensityPowderValue[i]), float(Temp_DensityPowder[i]))) 

mdb.models['Model-1'].Material(name='Material-Solid')
mdb.models['Model-1'].materials['Material-Solid'].Conductivity(
    table=ConductivitySolidData, 
    temperatureDependency=ON)
mdb.models['Model-1'].materials['Material-Solid'].SpecificHeat(
    table=SpecificHeatData, 
    temperatureDependency=ON)
mdb.models['Model-1'].materials['Material-Solid'].Density(
    table=DensitySolidData, 
    temperatureDependency=ON)
mdb.models['Model-1'].materials['Material-Solid'].LatentHeat(
    table=((440.0E9, 1605.0, 1655.0), ))

mdb.models['Model-1'].Material(name='Material-Powder')
mdb.models['Model-1'].materials['Material-Powder'].Depvar(n=1)
mdb.models['Model-1'].materials['Material-Powder'].UserMaterial(
    type=THERMAL, 
    thermalConstants=(1605.0, 1655.0, 440000000000, ))
mdb.models['Model-1'].materials['Material-Powder'].Density(
    table=DensityPowderData, 
    temperatureDependency=ON)

mdb.models['Model-1'].HomogeneousSolidSection(
    material='Material-Solid', 
    name='Section-Solid', 
    thickness=None)

mdb.models['Model-1'].HomogeneousSolidSection(
    material='Material-Powder', 
    name='Section-Powder', 
    thickness=None)

mdb.models['Model-1'].parts['Part-1'].Set(
    cells=mdb.models['Model-1'].parts['Part-1'].cells.findAt(
        ((7.0, 0.833333, 0.0), ), ), 
    name='Set-Solid')

mdb.models['Model-1'].parts['Part-1'].Set(
    cells=mdb.models['Model-1'].parts['Part-1'].cells.findAt(
        ((7.0, 0.833333, 10.07), ), ), 
    name='Set-Powder')

mdb.models['Model-1'].parts['Part-1'].SectionAssignment(
    region=mdb.models['Model-1'].parts['Part-1'].sets['Set-Solid'], 
    sectionName='Section-Solid', thicknessAssignment=FROM_SECTION)

mdb.models['Model-1'].parts['Part-1'].SectionAssignment(
    region=mdb.models['Model-1'].parts['Part-1'].sets['Set-Powder'], 
    sectionName='Section-Powder', thicknessAssignment=FROM_SECTION)

mdb.models['Model-1'].rootAssembly.Instance(
    dependent=ON, 
    name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])

mdb.models['Model-1'].HeatTransferStep(
    deltmx=100.0, 
    initialInc=1e-05, 
    maxInc=0.02, 
    maxNumInc=1000000, 
    minInc=1e-20, 
    name='Step-1', 
    previous='Initial', 
    timePeriod=0.02)

mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'NT', 'SDV', ))

#
mdb.models['Model-1'].rootAssembly.Surface(
    name='Surf-1', 
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.findAt(
        ((7.0, 0.833333, 10.07), ), ))

mdb.models['Model-1'].RadiationToAmbient(
    ambientTemperature=730.0, 
    ambientTemperatureAmp='', 
    createStepName='Step-1', 
    distributionType=UNIFORM, 
    emissivity=0.7, 
    field='', 
    name='Int-1', 
    radiationType=AMBIENT, 
    surface=mdb.models['Model-1'].rootAssembly.surfaces['Surf-1'])

mdb.models['Model-1'].rootAssembly.Set(
    cells=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].cells.findAt(((20.916667, 0.0, 10.023333), )), 
    name='Set-TopLayer')

#mdb.models['Model-1'].BodyHeatFlux(
#    createStepName='Step-1', 
#    distributionType=USER_DEFINED, 
#    magnitude=1.0, 
#    name='Load-1', 
#    region=mdb.models['Model-1'].rootAssembly.sets['Set-TopLayer'])

mdb.models['Model-1'].rootAssembly.Set(
    faces=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.findAt(((14.0, 0.833333, 0.0), )), 
    name='Set-BottomFace')

mdb.models['Model-1'].TemperatureBC(
    amplitude=UNSET, 
    createStepName='Step-1', 
    distributionType=UNIFORM, 
    fieldName='', 
    fixed=OFF, 
    magnitude=730.0, 
    name='BC-1', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-BottomFace'])

mdb.models['Model-1'].Temperature(
    createStepName='Initial', 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
    distributionType=UNIFORM, 
    magnitudes=(730.0, ), 
    name='Predefined Field-1', 
    region=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Set-Solid'])

mdb.models['Model-1'].Temperature(
    createStepName='Initial', 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, 
    distributionType=UNIFORM, 
    magnitudes=(730.0, ), 
    name='Predefined Field-2', 
    region=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Set-Powder'])
#----------------------------------------------------------------------------------------------------
from amConstants import *
import customKernel, amModule, amKernelInit
amModule.createAMModel(
    amModelName='AM-Model-1', 
    modelName1='Model-1', 
    stepName1='Step-1', 
    analysisType1=HEAT_TRANSFER, 
    isSequential=OFF, 
    modelName2='', 
    stepName2='', 
    analysisType2=STRUCTURAL, 
    processType=AMPROC_ABAQUS_BUILTIN)


mdb.customData.am.amModels['AM-Model-1'].addEventSeries(
    eventSeriesName='Event Series-MovingHeat', 
    eventSeriesTypeName='"ABQ_AM.PowerMagnitude"', 
    timeSpan='TOTAL TIME', 
    fileName='es_ElectronBeam.inp', 
    isFile=ON)

mdb.customData.am.amModels['AM-Model-1'].addTableCollection(
    tableCollectionName='ABQ_AM_Table Collection-MovingHeat')
mdb.customData.am.amModels['AM-Model-1'].dataSetup.tableCollections['ABQ_AM_Table Collection-MovingHeat'].PropertyTable(
    name='_propertyTable_"ABQ_AM.AbsorptionCoeff"_', 
    propertyTableType='"ABQ_AM.AbsorptionCoeff"', 
    propertyTableData=((0.9, ), ), 
    numDependencies=0, 
    temperatureDependency=OFF)
mdb.customData.am.amModels['AM-Model-1'].dataSetup.tableCollections['ABQ_AM_Table Collection-MovingHeat'].ParameterTable(
    name='_parameterTable_"ABQ_AM.MovingHeatSource"_', 
    parameterTabletype='"ABQ_AM.MovingHeatSource"', 
    parameterData=(('Event Series-MovingHeat', 'Goldak'), ))
mdb.customData.am.amModels['AM-Model-1'].dataSetup.tableCollections['ABQ_AM_Table Collection-MovingHeat'].ParameterTable(
    name='_parameterTable_"ABQ_AM.MovingHeatSource.Goldak"_', 
    parameterTabletype='"ABQ_AM.MovingHeatSource.Goldak"', 
    parameterData=(('100', '100', '100', 0.55, 0.062, 0.55, 1.1, 0.667, 1.333, 1.), ))

mdb.customData.am.amModels['AM-Model-1'].addHeatSourceDefinition(
    heatSourceName='Heat Source -MovingHeat', 
    dfluxDistribution='Moving-UserDefined', 
    dfluxMagnitude=1, 
    tableCollection='ABQ_AM_Table Collection-MovingHeat', 
    useElementSet=ON, 
    elementSetRegion=('Set-TopLayer', ))

jobName = 'ebam_pls_goldak_plugin_mmSI'
mdb.Job(model='Model-1', name=jobName, numCpus=16, numDomains=16, userSubroutine=os.path.realpath("umatht_dflux.for") )
mdb.saveAs(pathName=jobName)
#mdb.jobs[jobName].submit()
#mdb.jobs[jobName].waitForCompletion()
