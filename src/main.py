
import flet as ft

from utils import parse_questions
from topmenu import menubar 

def main(page: ft.Page):
    #Добавим главное меню
    page.add( ft.Row([menubar],rotate=0))

    #функции обработки выхода
    def handle_window_event(e):
        if e.data == "close" :
            page.open(confirm_dialog)

    page.window.prevent_close = True
    page.window.on_event = handle_window_event

    def yes_click(e):
        page.window.destroy()

    def no_click(e):
        page.close(confirm_dialog)

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Подтверждение"),
        content=ft.Text("Вы действительно хотите выйти?"),
        actions=[
            ft.ElevatedButton("Да", on_click=yes_click),
            ft.OutlinedButton("Нет", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    #Определим функцию для обработки результата выбора файла
    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files:
            #разберем файл с вопросами
            quests = parse_questions(e.files[0].path)    
            print(quests) 
            return quests 

    #Создадим FilePicker c обработчиком события выбора
    file_picker = ft.FilePicker(on_result = on_dialog_result)
    # и добавим его на страницу
    page.overlay.append(file_picker)
    page.update()

    #Добавим кнопку  вызова file_picker
    file_type = ft.FilePickerFileType.CUSTOM
    page.add(ft.ElevatedButton("Открыть тест...",
    on_click=lambda _: file_picker.pick_files(file_type=file_type,  dialog_title='File', allowed_extensions=['txt'],  allow_multiple=False)))

    mbc:ft.Control= menubar.controls[0]
    sm = mbc.controls[0] #Ссылка на меню "открыть тест"
    ex:ft.MenuItemButton = mbc.controls[2] #Ссылка на меню "выход"

    sm.on_click = lambda _: file_picker.pick_files(file_type=file_type,  dialog_title='File', allowed_extensions=['txt'],  allow_multiple=False)#handle_color_click1
    ex.event_handlers['click'] = lambda _:  page.open(confirm_dialog)

ft.app(main)
import flet as ft

def handle_on_hover(e):
    print(f"{e.control.content.value}.on_hover")

def handle_file_click(e):
    print(f"{e.control.content.value}.on_click")

def handle_exit_click(e) -> None:
    print(f"{e.control.content.value}.on_click")

menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Файл"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Открыть тест"),
                        leading=ft.Icon(ft.Icons.FILE_DOWNLOAD),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.PRESSED: ft.Colors.BLUE_200}),
                        on_click=handle_file_click,
                        on_hover=handle_on_hover,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Green"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}),
                        #on_click=handle_color_click,
                        on_hover=handle_on_hover,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Выход"),
                        leading=ft.Icon(ft.Icons.EXIT_TO_APP),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}),
                        on_click=handle_exit_click,
                        on_hover=handle_on_hover,
                    )
                ]
            ),
        ]
    )

def parse_questions(file_path: str) -> list[dict[str, list[str]]]:
    questions:list[dict] = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines:list[str] = file.readlines()

    current_question = None
    for line in lines:
        line:str = line.strip()
        if line:  # Если строка не пустая
            if not current_question:
                # Начинается новый вопрос
                current_question:dict[str, list[str]] = {
                    'question': line,
                    'answers': []
                }
            else:
                # Это вариант ответа
                current_question['answers'].append(line)
        else:
            # Пустая строка означает конец текущего вопроса
            if current_question:
                questions.append(current_question)
                current_question = None

    # Добавляем последний вопрос, если файл не заканчивается пустой строкой
    if current_question:
        questions.append(current_question)

    return questions



