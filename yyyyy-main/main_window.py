#ФАЙЛ В ЯКОМУ ПРОГРАМИ. ВІН ЗАПУСКАЄ ЇЇ
from  PyQt5.QtCore import*
from PyQt5.QtWidgets import*

window_main = QWidget() #вікно головного окна
window_main_layout = QVBoxLayout() # для вікна головного меню


#ВІДЖЕТИ ВІКНА
menu_pbtn = QPushButton('Налуштування')
rest_pbtn = QPushButton('ВІДПОЧИНОК')
give_answer_pbtn = QPushButton('Відповісти')

rest_sbox = QSpinBox()
rest_sbox.setValue(38)

ans1_rbtn = QRadioButton('Answer 1')
ans2_rbtn = QRadioButton('Answer 2')
ans3_rbtn = QRadioButton('Answer 3')
ans4_rbtn = QRadioButton('Answer 4')

question_lbl = QLabel('Question')
minutes_lbl = QLabel('хвилин')
resul_lbl = QLabel('Праильна відповідь')

answers_gbox = QGroupBox()
result_gbox = QGroupBox()


#лайаути вікна
header_layout = QHBoxLayout()
answers_gbox_layout = QVBoxLayout()
result_gbox_layout = QVBoxLayout()
answers_buttons_row1_layout = QHBoxLayout()
answers_buttons_row2_layout = QHBoxLayout()
#наповнили верхню частину віджетами додалив головний лайаут вікна

header_layout.addWidget(menu_pbtn)
header_layout.addWidget(rest_pbtn)
header_layout.addWidget(rest_sbox)
header_layout.addWidget(minutes_lbl)
window_main_layout.addLayout(header_layout)

#додати текст ші питання у головний  лейаут
window_main_layout.addWidget(question_lbl)


#додаємо віджети у лайаут  
answers_buttons_row1_layout.addWidget(ans1_rbtn)
answers_buttons_row1_layout.addWidget(ans2_rbtn)

answers_buttons_row2_layout.addWidget(ans3_rbtn)
answers_buttons_row2_layout.addWidget(ans4_rbtn)

answers_gbox_layout.addLayout(answers_buttons_row1_layout)
answers_gbox_layout.addLayout(answers_buttons_row2_layout)

answers_gbox.setLayout(answers_gbox_layout)
window_main_layout.addWidget(answers_gbox)


result_gbox_layout.addWidget(resul_lbl)
result_gbox.setLayout(result_gbox_layout)
window_main_layout.addWidget(result_gbox)


window_main_layout.addWidget(give_answer_pbtn)
window_main.setLayout(window_main_layout)

