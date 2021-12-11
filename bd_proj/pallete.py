import pandas as pd


LIGHT_BACKCOLOR = '#F5F5F5'
LIGHT_SUBCOLOR1 = "#ffffff"
LIGHT_SUBCOLOR2 = '#e6e6e6'
LIGHT_TEXTCOLOR = '#3c3c3c'

DARK_BACKCOLOR = '#232629'
DARK_SUBCOLOR2 = "#4F5B62"
DARK_SUBCOLOR1 = "#31363B"
DARK_TEXTCOLOR = "#7D7D7D"
DARK_TEXTCOLOR2 = "#969696"

pallete = pd.read_csv("./resources/data/pallete.csv", index_col = "name")

def set_pallete(theme) :
    # theme = "dark_blue.xml" or "light_red.xml"
    print(theme)
    background_theme = theme.split('_')[0]
    print(background_theme)
    main_theme = theme.split('_')[1].split('.')[0]

    # 배경색 설정
    if background_theme == "dark" :
        bg_color = DARK_BACKCOLOR
        bg_color_sub1 = DARK_SUBCOLOR1
        bg_color_sub2 = DARK_SUBCOLOR2
        text_color = DARK_TEXTCOLOR
        text_color2 = DARK_TEXTCOLOR2
    else :
        bg_color = LIGHT_BACKCOLOR
        bg_color_sub1 =LIGHT_SUBCOLOR1
        bg_color_sub2 = "#4F5B62"
        text_color = LIGHT_TEXTCOLOR
        text_color2 = LIGHT_TEXTCOLOR
    # 메인색 설정
    main_color = pallete['main'][main_theme]
    sub_color = pallete['sub'][main_theme]

    ### 추가예정

    color_pallete = {
        "bg_color" : bg_color,
        "bg_color_sub1" : bg_color_sub1,
        "bg_color_sub2": bg_color_sub2,
        "main_color" : main_color,
        "sub_color" : sub_color,
        "text_color" : text_color,
        "WHITE_SUB_COLOR" : "#4F5B62",
        "text_color2" : text_color2
    }

    return color_pallete

