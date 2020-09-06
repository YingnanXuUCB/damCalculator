import matplotlib.pyplot as plt
from .. import geometry
fig,ax=plt.subplots()
plt.close(fig)

class plotDam:
    def __init__(self,damGeometry,fig,ax):
        self.damPoints=damGeometry.damPoints
        self.fig=fig
        self.ax=ax
    def showDam(self):
        dummy = plt.figure()
        new_manager = dummy.canvas.manager
        new_manager.canvas.figure = self.fig
        self.fig.set_canvas(new_manager.canvas)
        self.ax.plot(*zip(*self.damPoints),color="darkorange")
        plt.show()