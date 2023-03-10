init python:

    #Упрощенная регестрация персонажей
    def reg_char(id, name, who_color, what_color = "#fff", pref = "", suf = ""):
        global Character
        gl = globals()
        
        gl[id] = Character( name, color=who_color, what_color=what_color, drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_prefix=pref, what_suffix=suf )

    #Новые персонажи
    reg_char("th", '', "#18FFEB", pref="~", suf="~")
    reg_char("vas", u'Василий', "#666666")
    reg_char("logdoc", u'Доктор', "#18FFEB")
    reg_char("neiz", u'Неизвестный', "#870909")
    reg_char("brod", u'Бродяга', "#BF5522")
    reg_char("phvoise", u'Голос в динамике', "#6BB7B2")
    reg_char("hartsman", u'Посетитель бара', "#6BB7B2")
    reg_char("liya", u'Лия', "#FF7C00")
    reg_char("dart", u'Артём', "#4B3DD1")
    reg_char("lizard", u'Ящер', "#0F722D")
    reg_char("neiz", u'Неизвестный', "#870909")
    reg_char("gldoc", u'Глав-врач', "#B2B087")
    reg_char("zihao", u'Доктор Зихао', "#18FFEB")
    reg_char("travmdoc", u'Tравматолог', "#4B3DD1")
    reg_char("qqpats", u'Парень', "#CB94F0")
    reg_char("qqdev", u'Девушка', "#EDE7E7")
    reg_char("andr", u'Андрей', "#FFB700")
    reg_char("ten", u'Тень', "#7C00B6")
    reg_char("tarak", u'Таракан', "#BF5522")
    reg_char("voise1", u'Голос', "#BF5522")
    reg_char("voice1", u'Голос', "#BF5522")
    reg_char("vs1", u'Голос', "#BF5522")
    reg_char("vs2", u'Голос', "#EDE7E7")
    reg_char("filin", u'Филин', "#3DCA00")
    reg_char("psyvas", u'Василий', "#891111")
    reg_char("deads", u'Смерть', "#812CE8", "#1CF0DA")
    reg_char("smert", u'Смерть', "#812CE8", "#1CF0DA")
    reg_char("medbr", u'Мед-брат', "#42CB8B")
    reg_char("miya", u'Мия', "#6BB7B2")
    reg_char("thz", u'...', "#891111", "#ff0000", "{font=fonts/beer money.ttf}{size=+30}", "{/size}{/font}")
    reg_char("thn", u'...', "#E2C778", "#aaaaaa", "{font=fonts/beer money.ttf}{size=+30}", "{/size}{/font}")
    reg_char("himera", u'Химера', "#CB94F0")
    reg_char("lin", u'Лин', "#BF2525")
    reg_char("riba", u'Рыба', "#01fff6")
    reg_char("lisa", u'Лиса', "#ff4900")
    reg_char("eretic", u'Еретик', "#9c9872")
    reg_char("mndlapa", u'Лапа', "#3c2818")
    reg_char("mndbul", u'Булыжник', "#47573c")
    reg_char("mndel", u'Электрик', "#6f929d")
    reg_char("kukla", u'Кукла', "#595859")