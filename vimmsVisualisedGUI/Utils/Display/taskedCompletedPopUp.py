from PyQt5 import QtWidgets as qtw


def task_completed_pop_up(task_title, task_msg, button_to_activate=None):
    
    if button_to_activate:
        button_to_activate.setEnabled(True)
    pop_up = qtw.QMessageBox()
    pop_up.setObjectName("popup")
    pop_up.setWindowTitle(task_title)
    pop_up.setText(task_msg)
    pop_up.setIcon(qtw.QMessageBox.Information)
    pop_up.exec()
