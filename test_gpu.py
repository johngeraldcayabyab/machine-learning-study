import pygfx
import pygfx as gfx
import pylinalg as la

cube = gfx.Mesh(
    gfx.box_geometry(50, 50, 50),
    gfx.MeshPhongMaterial(color="#336699"),
    # gfx.po
)

pygfx.Controller.enabled = 1

cube.local.position = (0, 300 ,0)

# print(cube.positions)


# cube.

def animate():
    rot = la.quat_from_euler((0.005, 0.01), order="XY")
    cube.local.rotation = la.quat_mul(rot, cube.local.rotation)


if __name__ == "__main__":
    disp = gfx.Display()
    # disp.before_render = animate
    disp.stats = True
    disp.show(cube)
