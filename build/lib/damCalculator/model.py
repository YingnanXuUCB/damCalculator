from . import geometry
from . import material
from . import force
from . import analysis
from . import plot
from matplotlib import pyplot as plt
class model:
    def __init__(self,damGeometry,concrete,water,upliftForce,fig,ax):

        #First level

        self.damGeometry=damGeometry
        self.concrete=concrete
        self.water=water
        self.upliftForce=upliftForce
        self.fig=fig
        self.ax=ax



        #Second level

        self.sectionArea=geometry.sectionArea(damGeometry=self.damGeometry)
        self.sectionCentroid=geometry.sectionCentroid(damGeometry=self.damGeometry)
        self.upstreamWaterPressure=force.upstreamWaterPressure(damGeometry=self.damGeometry,water=self.water)
        self.downstreamWaterPressure=force.downstreamWaterPressure(damGeometry=self.damGeometry,water=self.water)
        self.plotDam=plot.plotDam(damGeometry=self.damGeometry,fig=self.fig,ax=self.ax)

        #Third level

        self.damGravity=force.damGravity(sectionArea=self.sectionArea,sectionCentroid=self.sectionCentroid,concrete=self.concrete)

        #Fourth level

        self.maxFriction=force.maxFriction(damGravity=self.damGravity,upstreamWaterPressure=self.upstreamWaterPressure,\
                                           downstreamWaterPressure=self.downstreamWaterPressure,upliftForce=self.upliftForce)
        self.overtuningFactor=analysis.overtuningFactor(damGeometry=self.damGeometry,upstreamWaterPressure=self.upstreamWaterPressure,\
                                                        downstreamWaterPressure=self.downstreamWaterPressure,upliftForce=self.upliftForce,\
                                                        damGravity=self.damGravity)

        #Fifth level

        self.slipFactor=analysis.slipFactor(upstreamWaterPressure=self.upstreamWaterPressure,downstreamWaterPressure=self.downstreamWaterPressure,\
                                            maxFriction=self.maxFriction)


