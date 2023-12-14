from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from Interfaces.ExtractGenerateInterface import *
from Interfaces.StartPageInterface import *
from Interfaces.VisualiseInterface import *
from Interfaces.SimulateInterface import *
from Interfaces.ExperimentInterface import *


qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class ViMMSMain(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.stackedWidget = qtw.QStackedWidget()
        self.stackedWidget.setGeometry(25,25,600,500)

        #Initialise widgets
        homeWidget = StartPage()
        extractGenerateWidget = ExtractGeneratePage()
        simulateWidget = SimulatePage()
        visualiseWidget = VisualisePage()
        experimentWidget = ExperimentPage()

        homeWidget.setMinimumSize(400,400)
        #Add navigation to widgets once created
        homeWidget.ExtractGenerateButton.clicked.connect(lambda: changePage(self.stackedWidget, 1))
        homeWidget.SimulateButton.clicked.connect(lambda: changePage(self.stackedWidget, 2))
        homeWidget.VisualiseButton.clicked.connect(lambda: changePage(self.stackedWidget, 3))
        homeWidget.ExperimentButton.clicked.connect(lambda: changePage(self.stackedWidget, 4))
        extractGenerateWidget.ExtractHomeButton.clicked.connect(lambda: changePage(self.stackedWidget, 0))
        simulateWidget.SimulateHomeButton.clicked.connect(lambda: changePage(self.stackedWidget, 0))
        visualiseWidget.VisualiseHomeButton.clicked.connect(lambda: changePage(self.stackedWidget, 0))
        experimentWidget.ExperimentHomeButton.clicked.connect(lambda: changePage(self.stackedWidget, 0))

        #Add to stacked widget
        self.stackedWidget.addWidget(homeWidget)
        self.stackedWidget.addWidget(extractGenerateWidget)
        self.stackedWidget.addWidget(simulateWidget)
        self.stackedWidget.addWidget(visualiseWidget)
        self.stackedWidget.addWidget(experimentWidget)
        self.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    app = qtw.QApplication([])
    window = ViMMSMain()
    window.stackedWidget.show()
    app.exec_()

