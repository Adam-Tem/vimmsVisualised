def setCharge(self):
    if self.text() == "Positive":
        self.setText("Negative")
        self.setStyleSheet("background-color: red; color: black;")
    else:
        self.setText("Positive")
        self.setStyleSheet("background-color: green; color: white;")