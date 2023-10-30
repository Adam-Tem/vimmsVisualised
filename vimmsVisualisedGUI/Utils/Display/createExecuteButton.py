from PyQt5 import QtWidgets as qtw
from Utils.Controllers.controllerSelection import controllerSelection
from Utils.Generate.RunChemicalMixtureCreator import run_chemical_mixture_creator
## Just go back and parameter pass the combo box, trying to stay abstracted,
## but then I guess you still have to pass the parent to access the box as
## apposed to just the combo box, or maybe combo box getParent???


def create_execute_button(param_box, combo_box_text, execute_button_text):
    button = qtw.QPushButton(parent=param_box, text=execute_button_text)
    if execute_button_text == "Simulate":
        button.clicked.connect(lambda: controllerSelection(param_box, combo_box_text))
    else:
        button.clicked.connect(lambda: run_chemical_mixture_creator(combo_box_text))
    button.setBaseSize(200, 75)
    button.setObjectName(execute_button_text)
    button.setVisible(True)
    return button
