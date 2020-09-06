# damCalculator

A useful tool to calculate the dam's slidding and overturning safety factors, also can derive all the complicated forces applied to a single dam. The project is programmed in an object-oriented way, so most of the time when you want to pass parameters from one object to another, remember this "parameter" may also be an object.

# Installation

Use pip to install damCalculator:

.. code:: bash
pip install damcalculator


# Example

Here's an simple example of how to use this package on the St.Francis dam.

Import some bascis packages:

..code::python
from matplotlib import pyplot as plt
import damCalculator



Prepare for plotting:

..code::python
fig,ax=plt.subplots()
plt.close(fig)


Define some inner parameters of the St.Francis dam:

..code::python
damGeometry=damCalculator.geometry.damGeometry(H=85*0.3048,h=170*0.3048,l=15*0.3048,a=10*0.3048,b=135*0.3048,c=30*0.3048,hu=200*0.3048,hd=20*0.3048)
concrete=damCalculator.material.concrete(density=2400)
water=damCalculator.material.water(density=1000)


The distribution of uplift water pressure, choose one from the two below, or you can create your own:

..code::python
upliftForce=damCalculator.force.upliftForce(upliftPressure=[(0,598017.6,0)],damGeometry=damGeometry)
upliftForce=damCalculator.force.upliftForce(upliftPressure=[(0,0)],damGeometry=damGeometry)

Create model instance:

..code::python
model=damCalculator.model(damGeometry=damGeometry,concrete=concrete,water=water,upliftForce=upliftForce,fig=fig,ax=ax)


Print overturning safety factor and slipping safety factor:

..code::python
print(model.overtuningFactor.oFactor)
print(model.slipFactor.sFactor)

Plot the shape of the dam

..code::python
model.plotDam.showDam()

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
[MIT](https://choosealicense.com/licenses/mit/)
