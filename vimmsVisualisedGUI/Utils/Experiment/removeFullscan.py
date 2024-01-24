from PyQt5 import QtWidgets as qtw

from Utils.Experiment.updateLabel import remove_from_label

def remove_option(self, scroll_area, label_type):
    
    if label_type == "fullscan":
        self.fullscan_list = self.fullscan_list[:-1]
        text_label = scroll_area.findChild(qtw.QLabel, "FullscanNamesLabel")
        button = self.InjectionUndoButton
        scroll_area_contents = scroll_area.findChild(qtw.QWidget, "ScrollContents")
        if len(self.fullscan_list) == 0:
            button.setEnabled(False)
    else:
        self.experiment_case_list = self.experiment_case_list[:-1]
<<<<<<< HEAD
        self.experiment_name_list = self.experiment_name_list[:-1]
=======
>>>>>>> 84f8a4c4993f6138f7d9b613ad41a8f79e35b62d
        text_label = scroll_area.findChild(qtw.QLabel, "ExperimentNamesLabel")
        button = self.CaseUndoButton
        scroll_area_contents = scroll_area.findChild(qtw.QWidget, "ScrollContents_2")
        if len(self.experiment_case_list) == 0:
            button.setEnabled(False)
    remove_from_label(scroll_area_contents, text_label)
    