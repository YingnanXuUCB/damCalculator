import numpy 
import shapely
from matplotlib import pyplot as plt
import damCalculator

fig,ax=plt.subplots()
plt.close(fig)
# Define the basic parameters
damGeometry=damCalculator.geometry.damGeometry(H=85*0.3048,h=170*0.3048,l=15*0.3048,a=10*0.3048,b=135*0.3048,\
                                               c=30*0.3048,hu=200*0.3048,hd=20*0.3048)
concrete=damCalculator.material.concrete(density=2400)
water=damCalculator.material.water(density=1000)
#upliftForce=damCalculator.force.upliftForce(upliftPressure=[(0,598017.6)],damGeometry=damGeometry)
upliftForce=damCalculator.force.upliftForce(upliftPressure=[(0,0)],damGeometry=damGeometry)
# Define the model

model=damCalculator.model(damGeometry=damGeometry,concrete=concrete,water=water,upliftForce=upliftForce,fig=fig,ax=ax)
print(model.overtuningFactor.oFactor)
print(model.slipFactor.sFactor)
model.plotDam.showDam()
