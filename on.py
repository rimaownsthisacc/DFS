import matplotlib.pyplot as mlt
import numpy as nmpi


worstxpoint=nmpi.array([1,2,3,4])
worstypoint=nmpi.array([1,2,3,4])

mlt.plot(worstxpoint,worstypoint)

bestxpoint=nmpi.array([1,2,3,4])
bestypoint=nmpi.array([1,1,1,1])

mlt.plot(bestxpoint,bestypoint)

averagexpoint=nmpi.array([1,2,3,4])
averageypoint=nmpi.array([1,2,3,4])

mlt.plot(averagexpoint,averageypoint)

mlt.show()