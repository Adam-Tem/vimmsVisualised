from PyQt5 import QtWidgets as qtw


def add_fullscan_to_list(self, scroll_area, file_name, count):

    text_label = scroll_area.findChild(qtw.QLabel, "FullscanNamesLabel")
    scroll_area_contents = scroll_area.findChild(qtw.QWidget, "ScrollContents")
    current_text = text_label.text()
    self.fullscan_list.extend([file_name] * count)

    if len(current_text) > 0:
        current_text = current_text + ", "
    text_label.setText(current_text + file_name + " x" + str(count) )
    scroll_area_contents.setFixedWidth(len(text_label.text()) * 5)
    text_label.setFixedWidth(len(text_label.text()) * 5)