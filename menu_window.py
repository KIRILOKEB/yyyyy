#Файл, в я кому відтворено інтерфкйс меню
from  PyQt5.QtCore import*
from PyQt5.QtWidgets import*

window_menu = QWidget() # вікно меню
window_menu_layout = QVBoxLayout() # лайаут два вікна меню

#Віджети вікна

questions_list = QListWidget()
add_question_pbtn = QPushButton("Додати питання")
remove_question_pbtn = QPushButton("Видалити питання")
questions_ledit = QLineEdit()
answer_ledit = QLineEdit()
wrong1_ledit = QLineEdit()
wrong2_ledit = QLineEdit()
wrong3_ledit = QLineEdit()
back_to_main_pbtn = QPushButton('Повернутись в меню')



#Лайаути вікна

buttons_row_layout = QHBoxLayout()
question_form_layout = QFormLayout()


#РОЗТАШОВУЕМО ВІДЖЕТИ У ЛФЙАУТАХ 

window_menu_layout.addWidget(questions_list)
buttons_row_layout.addWidget(add_question_pbtn)
buttons_row_layout.addWidget(remove_question_pbtn)
window_menu_layout.addLayout(buttons_row_layout)

question_form_layout.addRow('Введіть питання ', questions_ledit)

question_form_layout.addRow('Введіть відповідь ', answer_ledit)

question_form_layout.addRow('Введіть неправильно ', wrong1_ledit)

question_form_layout.addRow('Введіть неправильно ', wrong2_ledit)

question_form_layout.addRow('Введіть неправильно ',wrong3_ledit)

window_menu_layout.addLayout(question_form_layout)

window_menu_layout.addWidget(back_to_main_pbtn)
window_menu.setLayout(window_menu_layout)