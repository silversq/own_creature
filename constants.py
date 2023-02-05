import numpy 

numberOfGenerations = 10
populationSize = 10

motorJointAngle = 1
nSteps = 500

numSensorNeurons = 1
numMotorNeurons = 6
backAmplitude = numpy.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 7
frontPhaseOffset = numpy.pi/4

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
frontTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*frontFrequency)+frontPhaseOffset)*(frontAmplitude)
backTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*backFrequency)+backPhaseOffset)*(backAmplitude)