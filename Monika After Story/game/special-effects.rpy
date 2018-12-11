# This file is meant to store any special effects.
# These can be some images or transforms.

image yuri dragon2:
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat

image blood splatter1:
    size (1, 1)
    truecenter
    Blood("blood_particle",dripTime=0.5, burstSize=150, burstSpeedX=400.0, burstSpeedY=400.0, numSquirts=15, squirtPower=400, squirtTime=2.0).sm


image k_rects_eyes1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    8.0

image k_rects_eyes2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    8.0

image natsuki mas_ghost:
    "natsuki ghost2"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25

image mujina:
    "mod_assets/other/mujina.png"
    zoom 1.25
    parallel:
        easeout 0.5 zoom 4.5 yoffset 1200
    0.5

image mas_lightning:
    "mod_assets/other/thunder.png"
    alpha 1.0

    choice:
        block:
            0.05
            alpha 0.0
            0.05
            alpha 1.0
            repeat 3

    choice:
        block:
            0.05
            alpha 0.0
            0.05
            alpha 1.0
            repeat 2

    choice:
        0.05

    parallel:
        easeout 2.8 alpha 0.0
    3.0
    Null()

image mas_lightning_s_bg = LiveComposite(
    (1280, 720),
    (0, 0), "mod_assets/other/thunder.png",
    (30, 200), "mod_assets/other/tree_sil.png"
)

image mas_lightning_s:
    "mas_lightning_s_bg"
    alpha 1.0

    block:
        0.05
        alpha 0.0
        0.05
        alpha 1.0
        repeat 2

    0.05
    alpha 0.0
    0.05
    "mod_assets/other/thunder.png"
    alpha 1.0

    parallel:
        easeout 2.8 alpha 0.0
    3.0
    Null()

transform k_scare:
    tinstant(640)
    ease 1.0 zoom 2.0

transform otei_appear(a=0.70,time=1.0):
    i11
    alpha 0.0
    linear time alpha a


init python:
    def zoom_smoothly(trans, st, at):
        if trans.y < _mas_current_kiss_y:
            trans.y = 50
        if trans.zoom < _mas_current_kiss_zoom:
            trans.zoom = 50
        return 0

transform mas_kissing(_zoom, _y,time=2.0):
    i11
    xcenter 640 yoffset ((680 - mas_sprites.adjust_y)  * mas_sprites.value_zoom / 1.1)   yanchor 1.0
    linear time ypos _y zoom _zoom


transform test_kissing(_zoom,_y=360):
    i11
    xcenter 640 yoffset ((600 * mas_sprites.value_zoom / 1.1) - mas_sprites.adjust_y ) yanchor 1.0
    linear 6.0 ypos _y zoom _zoom

label monika_kissing_motion(duration=5.0):
    # zoom_level
    # value_zoom
    # default_zoom_level
    # adjust_zoom
    # ajust_y
    # default_y
    python:
        config.log = "perrito.txt"
        renpy.log("I have no idea what's going on")
        renpy.log("{}".format( 4.6))
        renpy.log("{}".format(mas_sprites.value_zoom))
        renpy.log("{}".format(4.6 - mas_sprites.value_zoom))
    $ _mas_kiss_zoom = 4.9 / mas_sprites.value_zoom
    $ renpy.log("{}".format(_mas_kiss_zoom))
    $ _mas_kiss_y = 2060 - ( 1700  * (mas_sprites.value_zoom - 1.1))# plus something if below  def zoom
    #show monika at mas_kissing(store.mas_sprites.zoom_level, adjust_y)

    #show monika at test_kissing(_mas_kiss_zoom)

    show monika at mas_kissing(_mas_kiss_zoom,int(_mas_kiss_y),duration)

    return
