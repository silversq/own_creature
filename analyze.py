import numpy
import matplotlib.pyplot as mpl


c = numpy.load('data/backLegSensorValues.npy')
d = numpy.load('data/frontLegSensorValues.npy')

print(c)
targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))*(numpy.pi/4)
mpl.plot(targetAngles)
mpl.show()
line, = mpl.plot(c, label = 'Back Leg')
line2, = mpl.plot(d, label = 'Front Leg')
mpl.legend()

mpl.show()