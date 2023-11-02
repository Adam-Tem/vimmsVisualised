def setButtonText(self, options):
    if self.text() in ["Positive", "True"]:
        self.setText(options[1])
        self.setStyleSheet("background-color: red; color: black;")
    else:
        self.setText(options[0])
        self.setStyleSheet("background-color: green; color: white;")