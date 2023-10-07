from PyQt5 import QtWidgets as qtw

class LoadingWidget(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel()
        self.label.setText("Simulating...")
        self.finishedButton = qtw.QPushButton()
        self.finishedButton.setText("Okay")
        self.finishedButton.clicked.connect(lambda: self.close())
        self.layout.addWidget(self.label)
        self.setGeometry(100,100,200,200)
        self.setLayout(self.layout)

    def showLoadingWidget(self):
        self.show()
        
    def addExitButton(self):
        self.label.setText("Simulation Complete!")
        self.layout.addWidget(self.finishedButton)

    

