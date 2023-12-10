# script-version: 2.0
# Catalyst state generated using paraview version 5.12.0-RC1-261-g442d053e56
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [529, 620]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-3.0833695828914642, 0.9808887392282486, -15.8959641456604]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-3.688172561873803, -4.222090624155089, -42.177539989584695]
renderView1.CameraFocalPoint = [-3.4756156904281363, 2.2471037909309897, -2.268482630488684]
renderView1.CameraViewUp = [-0.49216799618312473, 0.8596944418530357, -0.1367337931167172]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 12.79532298858206
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(529, 620)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'IOSS Reader'
canex2 = IOSSReader(registrationName='can.ex2', FileName=['/Applications/ParaView-5.12.20231209.app/Contents/examples/can.ex2'])
canex2.ElementBlocks = ['block_1']
canex2.NodeBlockFields = ['ACCL', 'DISPL', 'VEL']
canex2.ElementBlockFields = ['EQPS']
canex2.NodeSets = []
canex2.SideSets = []

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(registrationName='ExtractTimeSteps1', Input=canex2)
extractTimeSteps1.TimeStepIndices = [43]
extractTimeSteps1.TimeStepRange = [0, 43]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from extractTimeSteps1
extractTimeSteps1Display = Show(extractTimeSteps1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'ACCL'
aCCLTF2D = GetTransferFunction2D('ACCL')

# get color transfer function/color map for 'ACCL'
aCCLLUT = GetColorTransferFunction('ACCL')
aCCLLUT.TransferFunction2D = aCCLTF2D
aCCLLUT.RGBPoints = [240351.78348822956, 0.231373, 0.298039, 0.752941, 101090816.04098687, 0.865003, 0.865003, 0.865003, 201941280.29848552, 0.705882, 0.0156863, 0.14902]
aCCLLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ACCL'
aCCLPWF = GetOpacityTransferFunction('ACCL')
aCCLPWF.Points = [240351.78348822956, 0.0, 0.5, 0.0, 201941280.29848552, 1.0, 0.5, 0.0]
aCCLPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
extractTimeSteps1Display.Representation = 'Surface'
extractTimeSteps1Display.ColorArrayName = ['POINTS', 'ACCL']
extractTimeSteps1Display.LookupTable = aCCLLUT
extractTimeSteps1Display.SelectTCoordArray = 'None'
extractTimeSteps1Display.SelectNormalArray = 'None'
extractTimeSteps1Display.SelectTangentArray = 'None'
extractTimeSteps1Display.OSPRayScaleArray = 'ACCL'
extractTimeSteps1Display.OSPRayScaleFunction = 'Piecewise Function'
extractTimeSteps1Display.Assembly = 'Assembly'
extractTimeSteps1Display.SelectOrientationVectors = 'ACCL'
extractTimeSteps1Display.ScaleFactor = 1.8172473251819612
extractTimeSteps1Display.SelectScaleArray = 'ACCL'
extractTimeSteps1Display.GlyphType = 'Arrow'
extractTimeSteps1Display.GlyphTableIndexArray = 'ACCL'
extractTimeSteps1Display.GaussianRadius = 0.09086236625909805
extractTimeSteps1Display.SetScaleArray = ['POINTS', 'ACCL']
extractTimeSteps1Display.ScaleTransferFunction = 'Piecewise Function'
extractTimeSteps1Display.OpacityArray = ['POINTS', 'ACCL']
extractTimeSteps1Display.OpacityTransferFunction = 'Piecewise Function'
extractTimeSteps1Display.DataAxesGrid = 'Grid Axes Representation'
extractTimeSteps1Display.PolarAxes = 'Polar Axes Representation'
extractTimeSteps1Display.ScalarOpacityFunction = aCCLPWF
extractTimeSteps1Display.ScalarOpacityUnitDistance = 1.2406673238330228
extractTimeSteps1Display.OpacityArrayName = ['POINTS', 'ACCL']
extractTimeSteps1Display.SelectInputVectors = ['POINTS', 'ACCL']
extractTimeSteps1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractTimeSteps1Display.ScaleTransferFunction.Points = [-80080944.0, 0.0, 0.5, 0.0, 47764300.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractTimeSteps1Display.OpacityTransferFunction.Points = [-80080944.0, 0.0, 0.5, 0.0, 47764300.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper
timeKeeper1.SuppressedTimeSources = canex2

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.008599977008998394
animationScene1.StartTime = 0.004299988504499197
animationScene1.EndTime = 0.008599977008998394

# initialize the animation scene

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'Time Step' selected for 'Trigger'
pNG1.Trigger.UseStartTimeStep = 1
pNG1.Trigger.UseEndTimeStep = 1

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'colormap_shading_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [1000, 1000]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(extractTimeSteps1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.ExtractsOutputDirectory = 'extracts'
options.GlobalTrigger = 'Time Step'
options.CatalystLiveTrigger = 'Time Step'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
