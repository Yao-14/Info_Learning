"""Interactively selecting data points with the lasso tool.
"""

import numpy as np
import pyvista as pv
import vtk

from typing import List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


def lasso_3d(
    coords: np.ndarray,
    values: np.ndarray = None,
    cmap: str = "viridis",
    point_size: int = 10,
    pick_method: Literal["rectangle", "box"] = "rectangle",
    invert: bool = False,
    merge: bool = True,
) -> np.ndarray or List[np.ndarray]:
    """
    Pick the interested part of coordinates by interactive approach.
    Args:
        coords: The coordinates of points data.
                [[x1, y1, z1],
                 [x2, y2, z2],
                 [x3, y3, z3],
                 [x4, y4, z4]
                 ...]
        values: The values of points data.
                [value1, value2, value3, value4,...]
        cmap: Visualization colors for point data.
        point_size: Points size.
        pick_method: Pick the interested part of a mesh using a 2D rectangle widget or 3D box widget. Available `pick_method` are:
                * `'rectangle'`: Pick the interested part of a mesh using a 2D rectangle widget. Multiple meshes can be generated at the same time.
                * `'box'`: Pick the interested part of a mesh using a 3D box widget. Only one mesh can be generated.
        invert: Flag on whether to flip/invert the pick.
        merge: Flag on whether to merge all picked meshes.
    Returns:
        A list of coordinate arrays or a coordinate array.
        If merge is True, return a coordinate array; else return a list of coordinate arrays.
    """

    mesh = pv.PolyData(coords)
    mesh.point_data["values"] = values
    mesh = mesh.cast_to_unstructured_grid()

    p = pv.Plotter()
    if pick_method == "rectangle":
        # Clip a mesh using a 2D rectangle widget.
        p.add_mesh(mesh, scalars="values", colormap=cmap, point_size=point_size, render_points_as_spheres=True)
        picked_meshes, invert_meshes, legend = [], [], []

        def split_mesh(original_mesh):
            """Adds a new mesh to the plotter each time cells are picked, and
            removes them from the original mesh"""

            # if nothing selected
            if not original_mesh.n_cells:
                return

            # remove the picked cells from main grid
            ghost_cells = np.zeros(mesh.n_cells, np.uint8)
            ghost_cells[original_mesh["orig_extract_id"]] = 1
            mesh.cell_data[vtk.vtkDataSetAttributes.GhostArrayName()] = ghost_cells
            mesh.RemoveGhostCells()

            # add the selected mesh this to the main plotter
            color = np.random.random(3)
            legend.append(["picked mesh %d" % len(picked_meshes), color])
            p.add_mesh(original_mesh, color=color)
            p.add_legend(legend)

            # track the picked meshes and label them
            original_mesh["picked_index"] = np.ones(original_mesh.n_points) * len(
                picked_meshes
            )
            picked_meshes.append(original_mesh)
            invert_meshes.append(mesh)

        p.enable_cell_picking(
            mesh=mesh,
            callback=split_mesh,
            show=False,
            font_size=12,
            show_message="Press `r` to enable retangle based selection. Press `r` again to turn it off. \n"
            "Press `q` to exit the interactive window. ",
        )
        p.show()
        picked_meshes = [invert_meshes[0]] if invert else picked_meshes
    else:
        # Clip a mesh using a 3D box widget.
        p.add_mesh_clip_box(mesh, invert=invert, scalars="values", colormap=cmap,
                            point_size=point_size, render_points_as_spheres=True)
        p.show()
        picked_meshes = p.box_clipped_meshes

    # plot final picked meshes
    pv.plot(picked_meshes)

    # Output coordinates array(s)
    if merge:
        if len(picked_meshes) > 1:
            merged_mesh = picked_meshes[0]
            for mesh in picked_meshes[1:]:
                merged_mesh.merge(mesh, inplace=True)
        else:
            merged_mesh = picked_meshes[0]
        return merged_mesh.points
    else:
        return [mesh.points for mesh in picked_meshes]


