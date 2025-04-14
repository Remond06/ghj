
import flet as ft
from flet import Colors

def pageSettings(page):
    '''Настройка главной страницы'''
    page.title = "Пример"
    page.vertical_alignment=ft.MainAxisAlignment.START
    page.padding = 15
    page.bgcolor=Colors.GREY_100
    page.theme_mode =ft.ThemeMode.SYSTEM
    page.window.prevent_close = True
    page.window.center()

fam = ft.TextField(label="Фамилия")    

import flet as ft
from components import fam


def onclick(e):
    fam.current.value = fam.current.value + "!"
    fam.update()


container1 = ft.Container(
    bgcolor=ft.colors.RED,
    width=200,
    height=200,
    expand=False,
    alignment= ft.alignment.top_center,
    content=ft.ElevatedButton("Кнопка", on_click=onclick),
)

container2 = ft.Container(bgcolor=ft.colors.GREEN, width=200, height=200)

container3 = ft.Container(
    bgcolor=ft.colors.BLUE,
    width=200,
    height=200,
    content=ft.TextField(
        ref=fam,
        label="Фамилия",
        autofocus=True,
    ),
)


# Список контейнеров
containers = [container1, container2, container3]
current_index = 0  # Индекс текущего контейнера

import flet as ft
from flet import Colors

class MyButton(ft.ElevatedButton):
    """Кнопка для проверки"""

    def __init__(self, text, onclick):
        super().__init__()
        self.bgcolor = Colors.BLUE_300
        self.color = ft.Colors.GREEN_800
        self.text = text
        self.on_click = onclick
