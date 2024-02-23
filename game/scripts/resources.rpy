init python:

    class MndMenuCh(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/logo/chast1.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("menuanima", MndMenuCh().sm)

    import math
    class MndCutM(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/scene/cutm.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("mndcutm", MndCutM().sm)

init:

    image anim blink_down = "images/anim/blink_down.png"
    image anim blink_up = "images/anim/blink_up.png"

    image unblink:
        contains:
            "anim blink_up" 
            xalign 0yalign 0
            ease 1.5pos (0,-1080)
        contains:
            "anim blink_down" 
            xalign 0yalign 0
            ease 1.5pos (0,1080)

    image blink:
        contains:
            "anim blink_up" 
            pos (0,-1080)
            ease 1.5xalign 0yalign 0
        contains:
            "anim blink_down" 
            pos (0,1080)
            ease 1.5xalign 0yalign 0


    image blinking:
        contains:
            "anim blink_up" 
            pos (0,-1080)
            ease 1.5xalign 0yalign 0
        contains:
            "anim blink_down" 
            pos (0,1080)
            ease 1.5xalign 0yalign 0
        pause 2.0
        contains:
            "anim blink_up" 
            xalign 0yalign 0
            ease 1.5pos (0,-1080)
        contains:
            "anim blink_down" 
            xalign 0yalign 0
            ease 1.5pos (0,1080)

init:

    transform center:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0

    transform left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0

    transform right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0

    transform fleft:
        xalign 0.16
        xanchor 0.5
        yanchor 0.0

    transform fright:
        xalign 0.84
        xanchor 0.5
        yanchor 0.0

    transform cleft:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0

    transform cright:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0

init:

    define dis = Dissolve(0.5, alpha=True)
    $ flash = Fade(1, 0, 1, color="#fff")
    $ flash2 = Fade(2, 2, 2, color="#fff")
    $ flash_red = Fade(1, 0, 1, color="#e11")
    $ fade3 = Fade(1.5, 0, 1.5)
    $ fade2 = Fade(1, 0, 1)
    $ hell_dissolve = Dissolve(50)
    $ dissolve2 = Dissolve(2)
    $ dissolve3 = Dissolve(3)
    $ dissolve4 = Dissolve(4)
    $ dissolve_fast = Dissolve(0.5)
    $ dissolve_long = Dissolve(100)
    $ dspr = Dissolve(.2)


    image black = "#000"
    image white = "#fff"
    image bg black = "#000"
    image bg white = "#fff"