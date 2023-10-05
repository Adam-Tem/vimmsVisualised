def setCharge(self):
    if self.IonModeButton.text() == "Positive":
        self.IonModeButton.setText("Negative")
        self.IonModeButton.setStyleSheet("background-color: red; color: black;")
    else:
        self.IonModeButton.setText("Positive")
        self.IonModeButton.setStyleSheet("background-color: green; color: white;")