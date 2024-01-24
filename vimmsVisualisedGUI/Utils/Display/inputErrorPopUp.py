from PyQt5 import QtWidgets as qtw

def input_error_pop_up(button_to_activate):

    if button_to_activate:
        button_to_activate.setEnabled(True)
    pop_up = qtw.QMessageBox()
    pop_up.setWindowTitle("Input error")
    pop_up.setText("Whoops! Please ensure all input fields are valid.")
    pop_up.setIcon(qtw.QMessageBox.Critical)
    pop_up.exec_()