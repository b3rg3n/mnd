init -1001 python:
    
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    
    def volume(vol, chnl):
        renpy.music.set_volume(vol, channel=chnl)
    
    def stop_music():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=chnl)

init python:

    showstatus = False
    pps = 10
    status_name = ""
    status_color = "#fff"
    status_color_custom = "#fff"
    def mnd_status():
        global status_name
        global status_color
        global status_color_custom
        if not showstatus or pps <= 0:
            status_name = ""
            status_color = status_color_custom or "#ffffff"
        elif pps == 1:
            status_name = "Нервный срыв"
            status_color = "#2c2c2d"
            status_color_custom = "#ffffff"
        elif pps == 2:
            status_name = "Состояние: Критическое"
            status_color = "#8f0000"
            status_color_custom = "#ffffff"
        elif pps <= 3:
            status_name = "Состояние: Апатия"
            status_color = "#ff7900"
            status_color_custom = "#ffffff"
        elif pps <= 6:
            status_name = "Состояние: Стресс"
            status_color = "#e4ce13"
            status_color_custom = "#ffffff"
        elif pps <= 8:
            status_name = "Состояние: Нормальное"
            status_color = "#0042ff"
            status_color_custom = "#ffffff"
        else:
            status_name = "Состояние: Хорошее"
            status_color = "#31be00"
            status_color_custom = "#ffffff"

    while mnd_status in config.window_overlay_functions:
        config.window_overlay_functions.remove(mnd_status)
    config.window_overlay_functions.append(mnd_status)