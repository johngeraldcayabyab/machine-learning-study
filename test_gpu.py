import pygfx as gfx
import pylinalg as la

cube = gfx.Mesh(
    gfx.box_geometry(200, 200, 200),
    gfx.MeshPhongMaterial(color="#336699"),
)


def animate():
    rot = la.quat_from_euler((0.005, 0.01), order="XY")
    # cube.
    # cube.positio
    cube.rotation = la.quat_mul(rot, cube.rotation)


if __name__ == "__main__":
    disp = gfx.Display()
    disp.before_render = animate
    disp.stats = True
    disp.show(cube)