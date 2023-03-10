init:
    transform mnd_chapter_anim:
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.2
                    choice:
                        xanchor 0.3
                    choice:
                        xanchor 0.4
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.6
                    choice:
                        xanchor 0.7
                    choice:
                        xanchor 0.8
                parallel:
                    choice:
                        yanchor 0.2
                    choice:
                        yanchor 0.3
                    choice:
                        yanchor 0.4
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.6
                    choice:
                        yanchor 0.7
                    choice:
                        yanchor 0.8
            parallel:
                choice:
                    rotate -2
                choice:
                    rotate -1
                choice:
                    rotate 0
                choice:
                    rotate 1
                choice:
                    rotate 2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
                choice:
                    alpha 0.7
                choice:
                    alpha 0.6
                choice:
                    alpha 0.5
                choice:
                    alpha 0.4
            pause 0.02
            repeat 20
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.498
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.502
                parallel:
                    choice:
                        yanchor 0.498
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.502
            parallel:
                choice:
                    rotate -0.2
                choice:
                    rotate -0.1
                choice:
                    rotate 0
                choice:
                    rotate 0.1
                choice:
                    rotate 0.2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
            pause 0.02
            repeat

    python:
        style.mnd_chapter_text.font = "gesmemories/fnt/beer money.ttf"
        style.mnd_chapter_text.xalign = 0.5
        style.mnd_chapter_text.yalign = 0.5
        style.mnd_chapter_text.size = 150
        style.mnd_chapter_text.color = "#ffffff"

        def MND_Chapter(name, time=3):
            renpy.show_screen("mnd_chapter", name)
            renpy.pause(time-0.4, hard=True)
            renpy.hide("mnd_chapter", layer="screens")
            renpy.show_screen("mnd_chapter", name)
            renpy.pause(0.4, hard=True)
            renpy.hide("mnd_chapter", layer="screens")

screen mnd_chapter(name):
    text name:
        style "mnd_chapter_text"
        at mnd_chapter_anim









screen say(who, what):
    style_prefix "say"

    if showstatus and pps > 0:
        add im.MatrixColor("gesmemories/image/gui/screens/say/status.webp", im.matrix.colorize("#000", status_color)):
            xpos 1104
            ypos 871
        text status_name:
            xpos 1162
            ypos 875
            size 20
    imagebutton:
        idle im.MatrixColor("gesmemories/image/gui/screens/say/backward_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gesmemories/image/gui/screens/say/backward_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 38
        ypos 924
        action Rollback()
    add im.MatrixColor("gesmemories/image/gui/screens/say/dialogue_box_large.webp", im.matrix.colorize("#000", status_color)):
        xpos 174
        ypos 866
    imagebutton:
        idle im.MatrixColor("gesmemories/image/gui/screens/say/hide_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gesmemories/image/gui/screens/say/hide_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 1508
        ypos 883
        action HideInterface()
    imagebutton:
        idle im.MatrixColor("gesmemories/image/gui/screens/say/save_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gesmemories/image/gui/screens/say/save_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 1568
        ypos 883
        action ShowMenu('save')
    imagebutton:
        idle im.MatrixColor("gesmemories/image/gui/screens/say/menu_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gesmemories/image/gui/screens/say/menu_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 1628
        ypos 883
        action ShowMenu('preferences')
    imagebutton:
        idle im.MatrixColor("gesmemories/image/gui/screens/say/load_idle.webp", im.matrix.colorize("#000", status_color))
        hover im.MatrixColor("gesmemories/image/gui/screens/say/load_hover.webp", im.matrix.colorize("#000", status_color))
        xpos 1688
        ypos 883
        action ShowMenu('load')
    if not config.skipping:
        imagebutton:
            idle im.MatrixColor("gesmemories/image/gui/screens/say/forward_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("gesmemories/image/gui/screens/say/forward_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1768
            ypos 924
            action Skip()
    else:
        imagebutton:
            idle im.MatrixColor("gesmemories/image/gui/screens/say/fast_forward_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("gesmemories/image/gui/screens/say/fast_forward_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1768
            ypos 924
            action Skip()
    text what:
        id "what"
        xpos 194
        ypos 914
        xmaximum 1541
        size 32
        line_spacing 1
    if who:
        text who:
            id "who"
            xpos 194
            ypos 890
            size 32
            line_spacing 1
