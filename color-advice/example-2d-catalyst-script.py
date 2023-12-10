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
renderView1.ViewSize = [1038, 638]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 0.0, 5464.101615137755]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 994.5253668071931
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [920, 620]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'Grid Axes 3D Actor'
renderView2.OrientationAxesVisibility = 0
renderView2.StereoType = 0
renderView2.CameraPosition = [0.0, 0.0, 5464.101615137755]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 994.5253668071931
renderView2.LegendGrid = 'Legend Grid Actor'
renderView2.Background = [0.32, 0.34, 0.43]
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView2)
layout1.SetSize(920, 620)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Wavelet'
wavelet1 = Wavelet(registrationName='Wavelet1')
wavelet1.WholeExtent = [-1000, 1000, -1000, 1000, 0, 0]
wavelet1.Center = [500.0, 400.0, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from wavelet1
wavelet1Display = Show(wavelet1, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'RTData'
rTDataTF2D = GetTransferFunction2D('RTData')

# get color transfer function/color map for 'RTData'
rTDataLUT = GetColorTransferFunction('RTData')
rTDataLUT.TransferFunction2D = rTDataTF2D
rTDataLUT.RGBPoints = [24.71866226196289, 0.231373, 0.298039, 0.752941, 155.53389167785645, 0.865003, 0.865003, 0.865003, 286.34912109375, 0.705882, 0.0156863, 0.14902]
rTDataLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RTData'
rTDataPWF = GetOpacityTransferFunction('RTData')
rTDataPWF.Points = [24.71866226196289, 0.0, 0.5, 0.0, 286.34912109375, 1.0, 0.5, 0.0]
rTDataPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
wavelet1Display.Representation = 'Slice'
wavelet1Display.ColorArrayName = ['POINTS', 'RTData']
wavelet1Display.LookupTable = rTDataLUT
wavelet1Display.SelectTCoordArray = 'None'
wavelet1Display.SelectNormalArray = 'None'
wavelet1Display.SelectTangentArray = 'None'
wavelet1Display.OSPRayScaleArray = 'RTData'
wavelet1Display.OSPRayScaleFunction = 'Piecewise Function'
wavelet1Display.Assembly = ''
wavelet1Display.SelectOrientationVectors = 'None'
wavelet1Display.ScaleFactor = 200.0
wavelet1Display.SelectScaleArray = 'RTData'
wavelet1Display.GlyphType = 'Arrow'
wavelet1Display.GlyphTableIndexArray = 'RTData'
wavelet1Display.GaussianRadius = 10.0
wavelet1Display.SetScaleArray = ['POINTS', 'RTData']
wavelet1Display.ScaleTransferFunction = 'Piecewise Function'
wavelet1Display.OpacityArray = ['POINTS', 'RTData']
wavelet1Display.OpacityTransferFunction = 'Piecewise Function'
wavelet1Display.DataAxesGrid = 'Grid Axes Representation'
wavelet1Display.PolarAxes = 'Polar Axes Representation'
wavelet1Display.ScalarOpacityUnitDistance = 1.7320508075688779
wavelet1Display.ScalarOpacityFunction = rTDataPWF
wavelet1Display.OpacityArrayName = ['POINTS', 'RTData']
wavelet1Display.ColorArray2Name = ['POINTS', 'RTData']
wavelet1Display.IsosurfaceValues = [155.53389167785645]
wavelet1Display.SliceFunction = 'Plane'
wavelet1Display.SelectInputVectors = [None, '']
wavelet1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
wavelet1Display.ScaleTransferFunction.Points = [24.71866226196289, 0.0, 0.5, 0.0, 286.34912109375, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
wavelet1Display.OpacityTransferFunction.Points = [24.71866226196289, 0.0, 0.5, 0.0, 286.34912109375, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from wavelet1
wavelet1Display_1 = Show(wavelet1, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
wavelet1Display_1.Representation = 'Slice'
wavelet1Display_1.ColorArrayName = ['POINTS', 'RTData']
wavelet1Display_1.LookupTable = rTDataLUT
wavelet1Display_1.SelectTCoordArray = 'None'
wavelet1Display_1.SelectNormalArray = 'None'
wavelet1Display_1.SelectTangentArray = 'None'
wavelet1Display_1.OSPRayScaleArray = 'RTData'
wavelet1Display_1.OSPRayScaleFunction = 'Piecewise Function'
wavelet1Display_1.Assembly = ''
wavelet1Display_1.SelectOrientationVectors = 'None'
wavelet1Display_1.ScaleFactor = 200.0
wavelet1Display_1.SelectScaleArray = 'RTData'
wavelet1Display_1.GlyphType = 'Arrow'
wavelet1Display_1.GlyphTableIndexArray = 'RTData'
wavelet1Display_1.GaussianRadius = 10.0
wavelet1Display_1.SetScaleArray = ['POINTS', 'RTData']
wavelet1Display_1.ScaleTransferFunction = 'Piecewise Function'
wavelet1Display_1.OpacityArray = ['POINTS', 'RTData']
wavelet1Display_1.OpacityTransferFunction = 'Piecewise Function'
wavelet1Display_1.DataAxesGrid = 'Grid Axes Representation'
wavelet1Display_1.PolarAxes = 'Polar Axes Representation'
wavelet1Display_1.ScalarOpacityUnitDistance = 17.817974362806787
wavelet1Display_1.ScalarOpacityFunction = rTDataPWF
wavelet1Display_1.OpacityArrayName = ['POINTS', 'RTData']
wavelet1Display_1.ColorArray2Name = ['POINTS', 'RTData']
wavelet1Display_1.IsosurfaceValues = [155.53389167785645]
wavelet1Display_1.SliceFunction = 'Plane'
wavelet1Display_1.SelectInputVectors = [None, '']
wavelet1Display_1.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
wavelet1Display_1.ScaleTransferFunction.Points = [24.71866226196289, 0.0, 0.5, 0.0, 286.34912109375, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
wavelet1Display_1.OpacityTransferFunction.Points = [24.71866226196289, 0.0, 0.5, 0.0, 286.34912109375, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = [renderView1, renderView2]
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView2, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'Time Step'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView2_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [1000, 1000]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(pNG1)
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
