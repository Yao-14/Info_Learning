"""
Interactively selecting data points with the lasso tool.
Tips: This method can only process point cloud data, and the data format is as follows:
    coords: np.ndarray,
        [[x1, y1],
         [x2, y2],
         [x3, y3],
         [x4, y4]
         ...]
    values: np.ndarray
        [value1, value2, value3, value4,...]
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.widgets import LassoSelector
from matplotlib.path import Path

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class SelectFromCollection:
    """
    Select indices from a matplotlib collection using `LassoSelector`.

    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        Axes to interact with.
    collection : `matplotlib.collections.Collection` subclass
        Collection you want to select from.
    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Ensure that we have separate colors for each object
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.lasso = LassoSelector(ax, onselect=self.onselect, props=dict(color="black"))
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()


def lasso_2d(
    coords: np.ndarray,
    values: np.ndarray = None,
    cmap: str = "viridis",
    point_size: int = 10
) -> np.ndarray:
    """

    Args:
        coords: The coordinates of points data.
                [[x1, y1],
                 [x2, y2],
                 [x3, y3],
                 [x4, y4]
                 ...]
        values: The values of points data.
                [value1, value2, value3, value4,...]
        cmap: Visualization colors for point data.
        point_size: Points size.
    Returns:
        select_points: The coordinates of the last selected points.

    Example:
        >>> data = pd.read_csv("A1_S13_cr.gem.gz", sep="\t")
        >>> points = (data[["x", "y", "MIDCounts"]].groupby(["x", "y"])["MIDCounts"].sum().to_frame("MIDCounts").reset_index())
        >>> select_points = lasso_2d(coords=points[["x", "y"]].values, values=points["MIDCounts"].values)
        >>> select_points = pd.DataFrame(select_points, columns=["x", "y"])
        >>> new_data = pd.merge(data, select_points, on=["x", "y"], how="inner")

    """
    def fig_set():
        mpl.use('TkAgg')
        fig, ax = plt.subplots(subplot_kw=dict(
            xlim=(coords[:, 0].min(), coords[:, 0].max()),
            ylim=(coords[:, 1].min(), coords[:, 1].max()),
            autoscale_on=False
        ))
        pts = ax.scatter(coords[:, 0], coords[:, 1], s=point_size, c=values, cmap=cmap)
        ax.set_title("Press enter to accept selected points.")
        return fig, ax, pts

    def select(event):
        if event.key == "enter":
            selector.disconnect()
            ax.set_title("The points have been selected, please exit the window.")
            fig.canvas.draw()

    # Create lasso window.
    fig, ax, pts = fig_set()
    selector = SelectFromCollection(ax, pts)
    fig.canvas.mpl_connect("key_press_event", select)
    plt.show()

    # Output the coordinates of the selected points.
    select_points = selector.xys[selector.ind].astype(coords.dtype)
    return select_points
