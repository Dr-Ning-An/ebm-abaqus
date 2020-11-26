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
import numpy

Mdb()

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)
mdb.models['Model-1'].setValues(absoluteZero=-273.15, stefanBoltzmann=5.669e-11)

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=42.0)

mdb.models['Model-1'].sketches['__profile__'].rectangle(
    point1=(0.0, 0.0), 
    point2=(9.9, 1.2))

mdb.models['Model-1'].Part(
    dimensionality=THREE_D, 
    name='Part-1', 
    type=DEFORMABLE_BODY)

mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(
    depth=5.0+0.07*60, 
    sketch=mdb.models['Model-1'].sketches['__profile__'])

del mdb.models['Model-1'].sketches['__profile__']

# Partition
plane1 = mdb.models['Model-1'].parts['Part-1'].DatumPlaneByPrincipalPlane(
    offset=5.0, 
    principalPlane=XYPLANE)

mdb.models['Model-1'].parts['Part-1'].PartitionCellByDatumPlane(
    cells=mdb.models['Model-1'].parts['Part-1'].cells, 
    datumPlane=mdb.models['Model-1'].parts['Part-1'].datums[plane1.id])

mdb.models['Model-1'].ConstrainedSketch(
    gridSpacing=1.16, 
    name='__profile__', 
    sheetSize=46.51, 
    transform=mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
        sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces.findAt((9.9/2.0, 0.0, 5.0/2.0), ), 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges.findAt((9.9, 0.0, 5.0/2.0), ), 
    sketchOrientation=RIGHT, 
    origin=(0.0, 0.0, 0.0)))

for i in range(198):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0+i*0.05, 5.0+0.07*60), 
        point2=(0.0+i*0.05, 5.0))    

########################################################################################

for j in range(3):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0, 5.0-j*0.05), 
        point2=(9.9, 5.0-j*0.05))

for i in range(66):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0+i*0.05*3, 5.0), 
        point2=(0.0+i*0.05*3, 5.0-4*0.05))    

for i in range(66):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.05+i*0.05*3, 5.0), 
       point2=(0.05+i*0.05*3, 5.0-3*0.05))
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.10+i*0.05*3, 5.0), 
       point2=(0.10+i*0.05*3, 5.0-3*0.05))
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.05+i*0.05*3, 5.0-3*0.05), 
       point2=(0.10+i*0.05*3, 5.0-3*0.05))
#
for i in range(66):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0 + 0.15*i, 5.0-4*0.05), 
        point2=(0.05 + 0.15*i, 5.0-3*0.05))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.1 + 0.15*i, 5.0-3*0.05), 
        point2=(0.15 + 0.15*i, 5.0-4*0.05))
##
for j in range(3):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0, 5.0-4*0.05 - j*0.15), 
        point2=(9.9, 5.0-4*0.05 - j*0.15))
##
for i in range(22):
   mdb.models['Model-1'].sketches['__profile__'].Line(
       point1=(0.0+i*0.45, 5.0-4*0.05), 
        point2=(0.0+i*0.45, 0.0))
##
for i in range(22):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.15 + i*0.45, 5.0-4*0.05), 
        point2=(0.15 + i*0.45, 5.0-4*0.05 - 0.15*1))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.30 + i*0.45, 5.0-4*0.05), 
        point2=(0.30 + i*0.45, 5.0-4*0.05 - 0.15*1))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.15 + i*0.45, 5.0-4*0.05 - 0.15*1), 
        point2=(0.30 + i*0.45, 5.0-4*0.05 - 0.15*1))
##
for i in range(22):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0 + 0.45*i, 5.0-4*0.05-2*0.15), 
        point2=(0.15 + 0.45*i, 5.0-4*0.05-1*0.15))
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.3 + 0.45*i, 5.0-4*0.05-1*0.15), 
        point2=(0.45 + 0.45*i, 5.0-4*0.05-2*0.15))
##
for j in range(2):
    mdb.models['Model-1'].sketches['__profile__'].Line(
        point1=(0.0, 5.0-4*0.05 - 2*0.15 - j*0.45), 
        point2=(9.9, 5.0-4*0.05 - 2*0.15 - j*0.45))
#

##
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(
    faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(((9.9/2.0, 0.0, 5.0/2.0), ), ((9.9/2.0, 0.0, (5.0+0.07*60+5.0)/2.0), ), ), 
    sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges.findAt((9.9, 0.0, 5.0/2.0), ))
##### 
mdb.models['Model-1'].parts['Part-1'].setMeshControls(
    regions=mdb.models['Model-1'].parts['Part-1'].cells, 
    technique=SWEEP)
#
mdb.models['Model-1'].parts['Part-1'].seedEdgeByNumber(
    constraint=FINER, 
    edges=mdb.models['Model-1'].parts['Part-1'].edges, number=1)
#
for i in range(199):
    mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(
        constraint=FINER, 
        edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0 + i*0.05, 0.0, (5.0+5.0+0.07*60)/2.0), )), 
        size=0.0175*2)
#
for i in range(199):
    mdb.models['Model-1'].parts['Part-1'].seedEdgeBySize(
        constraint=FINER, 
        edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0 + i*0.05, 0.0, (5.0+4.95)/2.0), )), 
        size=0.0175*2)   
##
for i in range(1,22):
    mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
        biasMethod=SINGLE, 
        constraint=FINER, 
        end1Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0 + i*0.45, 0.0, 1.975), ), ), 
        maxSize=0.9, 
        minSize=0.45)
#
mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0, 0.0, 1.975), ), ), 
    maxSize=0.9, 
    minSize=0.45)

mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((9.9, 0.0, 1.975), ), ), 
    maxSize=0.9, 
    minSize=0.45)
#
mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0, 0.625, 5.0+0.07*60), )), 
    maxSize=0.15, 
    minSize=0.05)

mdb.models['Model-1'].parts['Part-1'].seedEdgeByBias(
    biasMethod=SINGLE, 
    constraint=FINER, 
    end2Edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.0, 0.625, 5.0), )), 
    maxSize=0.15, 
    minSize=0.05)
#
mdb.models['Model-1'].parts['Part-1'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-1'].cells)

mdb.models['Model-1'].parts['Part-1'].setElementType(
    elemTypes=(ElemType(elemCode=DC3D8, elemLibrary=STANDARD), ElemType(elemCode=DC3D6, 
      elemLibrary=STANDARD), ElemType(elemCode=DC3D4, elemLibrary=STANDARD)), 
    regions=(mdb.models['Model-1'].parts['Part-1'].cells, ))
#
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
#
mdb.models['Model-1'].parts['Part-1'].Set(
    cells=mdb.models['Model-1'].parts['Part-1'].cells.findAt(
        ((7.0, 0.833333, 0.0), ), ), 
    name='Set-Solid')

mdb.models['Model-1'].parts['Part-1'].Set(
    cells=mdb.models['Model-1'].parts['Part-1'].cells.findAt(
        ((7.0, 0.833333, 5.0+0.07*60), ), ), 
    name='Set-Powder')
#
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
#
mdb.models['Model-1'].HeatTransferStep(
    deltmx=100.0, 
    initialInc=1e-05, 
    maxInc=0.1, 
    maxNumInc=1000000, 
    minInc=1e-20, 
    name='Step-1', 
    previous='Initial', 
    timePeriod=12.0)
mdb.models['Model-1'].steps['Step-1'].control.setValues(allowPropagation=OFF, 
    resetDefaultValues=OFF, timeIncrementation=(4.0, 8.0, 9.0, 16.0, 10.0, 4.0, 
    12.0, 30.0, 6.0, 3.0, 50.0))
mdb.models['Model-1'].steps['Step-1'].Restart(frequency=500, numberIntervals=0
    , overlay=ON, timeMarks=OFF)


#TimePointArray = []
#for i in range(60):
#    TimePointArray = numpy.concatenate((TimePointArray, numpy.linspace(0.2*i+0.01, 0.2*i+0.1, 10), numpy.linspace(0.2*i+0.102, 0.2*i+0.2, 50)))
#TimePointData = []
#for i in range(len(TimePointArray)):
#	TimePointData.append((float(TimePointArray[i]), ))
#mdb.models['Model-1'].TimePoint(
#    name='TimePoints-1', 
#    points=TimePointData)

mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(rebar=EXCLUDE
     , region=
     mdb.models['Model-1'].rootAssembly.allInstances['Part-1-1'].sets['Set-Powder']
     , sectionPoints=DEFAULT, variables=('SDV', ), frequency=
    100)

#
mdb.models['Model-1'].rootAssembly.Surface(
    name='Surf-1', 
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.findAt(
        ((7.0, 0.833333, 5.0+0.07*60), ), ))
#
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
    faces=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.findAt(((7.0, 0.833333, 0.0), )), 
    name='Set-BottomFace')
#
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
#
#
######################################################################################
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
    eventSeriesName='Event Series - Material Deposition', 
    eventSeriesTypeName='"ABQ_AM.MaterialDeposition"', 
    timeSpan='TOTAL TIME', 
    fileName='es_roller.inp', 
    isFile=ON)

mdb.customData.am.amModels['AM-Model-1'].addTableCollection(
    tableCollectionName='ABQ_AM_Table Collection - Material Deposition')
mdb.customData.am.amModels['AM-Model-1'].dataSetup.tableCollections['ABQ_AM_Table Collection - Material Deposition'].ParameterTable(
    name='parameterTable_"ABQ_AM.MaterialDeposition"', 
    parameterTabletype='"ABQ_AM.MaterialDeposition"', 
    parameterData=(('Event Series - Material Deposition', 'Roller'), ))

mdb.customData.am.amModels['AM-Model-1'].addMaterialArrival(
    materialArrivalName='Material Source -1', 
    tableCollection='ABQ_AM_Table Collection - Material Deposition', 
    followDeformation=OFF, 
    useElementSet=ON, 
    elementSetRegion=('Part-1-1.Set-Powder', ))

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
    elementSetRegion=('Part-1-1.Set-Powder', ))

mdb.customData.am.amModels['AM-Model-1'].addCoolingInteractions(
    coolingInteractionName='Cooling Interaction -1', useElementSet=ON, 
    elementSetRegion=('Part-1-1.Set-Powder', ), isConvectionActive=OFF, 
    isRadiationActive=ON, filmDefinition='Embedded Coefficient', 
    filmCoefficient=1, filmcoefficeintamplitude='Instantaneous', 
    sinkDefinition='Uniform', sinkTemperature=26, 
    sinkAmplitude='Instantaneous', radiationType='toAmbient', 
    emissivityDistribution='Uniform', emissivity=0.7, ambientTemperature=730, 
    ambientTemperatureAmplitude='Instanteneous')
#############################################################################################


jobName = 'ebam_pls_reduced_materialdeposit_goldak_plugin_mmSI'
mdb.Job(model='Model-1', name=jobName, numCpus=12, numDomains=12, numGPUs=1, userSubroutine=os.path.realpath("umatht_dflux.for") )
mdb.saveAs(pathName=jobName)
#mdb.jobs[jobName].submit()
#mdb.jobs[jobName].waitForCompletion()
