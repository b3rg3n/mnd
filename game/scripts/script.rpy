define e = Character('Эйлин', color="#c8ffc8")

label splashscreen:
    scene black with dissolve2
    if(renpy.seen_label("splashscreen_2")):
        jump splashscreen_2
    $ renpy.pause(1, hard=True)
    play sound mnd_floor_amb
    play ambience mnd_coridors_ambience_1 fadein 8
    $ renpy.pause(4, hard=True)
    stop sound fadeout 3
    play sound2 mnd_r_creak
    scene bg mnd_r_int_bg_1 with dissolve2
    $ renpy.pause(2, hard=True)
    play sound mnd_r_creak2
    scene bg mnd_r_int_bg_2 with dissolve
    $ renpy.pause(0.5, hard=True)
    play sound mnd_r_vine
    scene bg mnd_r_int_bg_3 with dissolve2
    $ renpy.pause(0.5, hard=True)
    stop sound fadeout 2
    scene black
    show mnd_r_tv_log
    with fade3
    $ renpy.pause(1.5, hard=True)
    play sound mnd_tv_noise
    show mnd_r_ges_spl behind mnd_r_tv_log
    show overlay mnd_memory_back_1 behind mnd_r_tv_log
    show prologue_dream behind mnd_r_tv_log
    with dissolve2
    $ renpy.pause(2.5, hard=True)
    stop sound fadeout 3
    stop ambience fadeout 4
    scene black with fade3
    show mnd_new_dis_2 with dissolve2
    $ renpy.pause(13.5, hard=True)
label splashscreen_2:
    scene black with fade2
    show mnd_new_dis_3 with dissolve2
    $ renpy.pause(5.5, hard=True)
    scene black with fade3
    show mnd_a3_menu_1
    show expression (MndMenuCh().sm) as mndmenuch
    show mnd_a3_menu_2
    show mnd_a3_menu_3
    show mndrain_l
    with dissolve4
    return



label start:
    stop music fadeout 4
    scene black with fade3
    $ renpy.pause(2, hard=True)
    jump gesmnds
