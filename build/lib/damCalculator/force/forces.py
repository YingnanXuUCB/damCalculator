from .. import material
from .. import geometry
import numpy
import shapely
from shapely.geometry import Polygon


class upstreamWaterPressure:
    """
    Attributes
    ---------------------------------
    fx:Horizontal force of upstream pressure
    fy:Vertical force of upstream pressure
    xFocus:Centroid's x-coordinate
    yFocus:Centroid's y-coordinate
    """
    def __init__(self,damGeometry,water):
        if damGeometry.H>damGeometry.hu:
            self.fx=0.5*water.density*9.81*damGeometry.hu*damGeometry.hu
            self.fy=-0.5*water.density*9.81*damGeometry.hu*damGeometry.hu*(damGeometry.a/damGeometry.H)
            self.xFocus=(1/3)*damGeometry.a*damGeometry.hu/damGeometry.H
            self.yFocus=(1/3)*damGeometry.hu
        else:
            self.fx=0.5*water.density*9.81*damGeometry.hu*damGeometry.hu
            self.fy=-0.5*water.density*9.81*damGeometry.a*(2*damGeometry.hu-damGeometry.H)
            self.xFocus=(1/3)*damGeometry.a*(3*damGeometry.hu-2*damGeometry.H)/(2*damGeometry.hu-damGeometry.H)
            self.yFocus=(1/3)*damGeometry.hu

class downstreamWaterPressure:
    """
    Attributes
    ---------------------------------
    fx:Horizontal force of downstream pressure
    fy:Vertical force of downstream pressure
    xFocus:Centroid's x-coordinate
    yFocus:Centroid's y-coordinate
    **Assume that downstream water head is lower than h
    """
    def __init__(self,damGeometry,water):
        self.fx=-0.5*water.density*9.81*damGeometry.hd*damGeometry.hd
        self.fy=-0.5*water.density*9.81*damGeometry.hd*damGeometry.hd*(damGeometry.b/damGeometry.h)
        self.xFocus=damGeometry.a+damGeometry.l+damGeometry.b-(1/3)*damGeometry.b*damGeometry.hd/damGeometry.h
        self.yFocus=(1/3)*damGeometry.hd

class upliftForce:
    """
    Attributes
    ----------------------
    up:Tuples of the uplift pressure's shape
    upliftPolygon:Instance of shapely of up
    f:Magnitude of centroid uplift force
    x:Centroid force's x-center of uplift force
    """
    def __init__(self,upliftPressure,damGeometry):
        self.uP=upliftPressure+[(damGeometry.a+damGeometry.l+damGeometry.b,0),(0,0)]
        self.upliftPolygon = Polygon(self.uP)
        self.f=self.upliftPolygon.area
        self.x=self.upliftPolygon.centroid.coords[:][0][0]

class damGravity:
    '''
    Attributes
    --------------------------
    gravity:gravity of the dame
    x:Centroid's x-coordinate
    y:Centroid's y-coordinate
    '''
    def __init__(self,sectionArea,sectionCentroid,concrete):
        self.gravity=-1*9.81*sectionArea.area*concrete.density
        self.x=sectionCentroid.xCentroid
        self.y=sectionCentroid.yCentroid
class maxFriction:
    '''
    Attributes
    --------------------
    f:Friction on the dam's bottom face
    '''
    def __init__(self,damGravity,upstreamWaterPressure,downstreamWaterPressure,upliftForce):
        self.f=-1*numpy.tan(40/180*numpy.pi)*(-1*damGravity.gravity-upstreamWaterPressure.fy-downstreamWaterPressure.fy-upliftForce.f)





        


