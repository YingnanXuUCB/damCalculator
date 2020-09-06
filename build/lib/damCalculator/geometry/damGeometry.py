class damGeometry:
    '''
    Attributes
    --------------
    H:Dam height of upstream face
    h:Dam height of dowstream face
    l:Length of crest
    a:Horizontal projection of the upstream face
    b:Horizontal projection of the downstream face
    c:Height of the downstream crest
    hu:Upstream water's height
    hd:Downstream water's height
    '''
    def __init__(self,H,h,l,a,b,c,hu,hd):
        self.H=H
        self.h=h
        self.l=l
        self.a=a
        self.b=b
        self.c=c
        self.hu=hu
        self.hd=hd

        self.damPoints=[
            (0,0),
            (self.a+self.l+self.b,0),
            (self.a+self.l,self.h),
            (self.a+self.l,self.h+self.c),
            (self.a,self.h+self.c),
            (self.a,self.H),
            (0,0)
            ]

