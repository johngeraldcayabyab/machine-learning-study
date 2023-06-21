import pygfx as gfx

cube = gfx.Mesh(
    gfx.box_geometry(200, 200, 200),
    gfx.MeshPhongMaterial(color="#336699"),
)


def animate():
    rot = gfx.linalg.Quaternion().set_from_euler(gfx.linalg.Euler(0.110, -0.1))
    cube.rotation.multiply(rot)

disp = gfx.Display()
disp.before_render = animate
disp.show(cube)