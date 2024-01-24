from PyQt5 import QtWidgets as qtw

from Utils.Experiment.updateLabel import add_to_label

def add_fullscan_to_list(self, scroll_area, file_name, file_location, base_dir, count):

    text_label = scroll_area.findChild(qtw.QLabel, "FullscanNamesLabel")
    scroll_area_contents = scroll_area.findChild(qtw.QWidget, "ScrollContents")
    self.fullscan_list.extend([file_location[len(base_dir)+1:]] * count)
    self.InjectionUndoButton.setEnabled(True)
    add_to_label(scroll_area_contents, text_label, file_name, "fullscan", count)