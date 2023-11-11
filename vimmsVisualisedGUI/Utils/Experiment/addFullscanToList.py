


def add_fullscan_to_list(self, file_name, count):
    current_list = self.FullscanNamesLabel.text()
    self.fullscan_list.extend([file_name] * count)

    if self.FullscanNamesLabel != "":
        self.FullscanNamesLabel.setText(current_list + ", ")
    self.FullscanNamesLabel.setText(current_list + "\n" + file_name + " x" + str(count) )