from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from main_window import *
from menu_window import *
def show_questions():
    result_gbox.hide()
    answers_gbox.show()
def show_result():
    result_gbox.show()
    answers_gbox.hide()





def check_answer():
    if give_answer_pbtn.text() == 'Відповісти':
        show_result()
        give_answer_pbtn.setText('Наступне питання')
    elif give_answer_pbtn.text() == 'Наступне питання':
        show_questions()
        give_answer_pbtn.setText('Відповісти')




def show_menu():
    window_menu.show()
    window_main.hide()
def show_main():
    window_menu.hide()
    window_main.show()
def connect_buttons():
    menu_pbtn.clicked.connect(show_menu)
    give_answer_pbtn.clicked.connect(check_answer)
    back_to_main_pbtn.clicked.connect(show_main)