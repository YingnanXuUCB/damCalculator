from . import damGeometry


class sectionArea:
    def __init__(self,damGeometry):
        '''
        Attributes
        --------------------
        area:Area of the dam's section
        '''
        self.area=0.5*damGeometry.a*damGeometry.H+0.5*damGeometry.b*damGeometry.h+damGeometry.l*(damGeometry.h+damGeometry.c)

class sectionCentroid:
    def __init__(self,damGeometry):
        '''
        Attributes
        ---------------------------------
        xcentroid:x-coordinate of dam's shape center
        yCentroid:y-coordinate of dam's shape center
        '''
        self.xCentroid=(0.5*damGeometry.a*damGeometry.H*(2/3)*damGeometry.a+
                        damGeometry.l * (damGeometry.h+damGeometry.c)*(damGeometry.a+0.5*damGeometry.l)+
                        0.5*damGeometry.b*damGeometry.h*(damGeometry.a+damGeometry.l+(1/3)*damGeometry.b))/\
                       (0.5*damGeometry.a*damGeometry.H+0.5*damGeometry.b*damGeometry.h+damGeometry.l*(damGeometry.h+damGeometry.c))
        self.yCentroid=(0.5*damGeometry.a*damGeometry.H*(1/3)*damGeometry.H+
                        damGeometry.l * damGeometry.H*(0.5*damGeometry.h+0.5*damGeometry.c)+
                        0.5*damGeometry.b*damGeometry.h*((1/3)*damGeometry.h))/\
                       (0.5*damGeometry.a*damGeometry.H+0.5*damGeometry.b*damGeometry.h+damGeometry.l*(damGeometry.h+damGeometry.c))

