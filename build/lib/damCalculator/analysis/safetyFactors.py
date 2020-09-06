from .. import force
from .. import geometry


class slipFactor:
    '''
    Attributes
    sFactor:Slipping safety factor
    '''
    def __init__(self,upstreamWaterPressure,downstreamWaterPressure,maxFriction):
        self.sFactor=abs(maxFriction.f/(upstreamWaterPressure.fx+downstreamWaterPressure.fx))

class overtuningFactor:
    '''
    Attributes
    oFactor:Overturning safety factor
    '''
    def __init__(self,damGeometry,upstreamWaterPressure,downstreamWaterPressure,upliftForce,damGravity):
        self.oFactor=abs(
            (damGravity.gravity*(damGeometry.a+damGeometry.l+damGeometry.b-damGravity.x))/\
                        (upstreamWaterPressure.fx*upstreamWaterPressure.yFocus+\
                        upstreamWaterPressure.fy*(damGeometry.a+damGeometry.l+damGeometry.b-upstreamWaterPressure.xFocus)+\
                        upliftForce.f*(damGeometry.a+damGeometry.l+damGeometry.b-upliftForce.x)+\
                        downstreamWaterPressure.fy*(damGeometry.a+damGeometry.l+damGeometry.b-downstreamWaterPressure.xFocus)+\
                        downstreamWaterPressure.fx*downstreamWaterPressure.yFocus)
        )

