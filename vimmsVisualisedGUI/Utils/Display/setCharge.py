def setButtonText(button, options):
    if button.text() in ["Positive", "True"]:
        button.setText(options[1])
        button.setStyleSheet("background-color: red; color: black;")
        button.setAccessibleName(options[1])
    else:
        button.setText(options[0])
        button.setStyleSheet("background-color: green; color: white;")
        button.setAccessibleName(options[0])