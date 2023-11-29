from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from Interfaces.ExtractGenerateInterface import *
from Interfaces.StartPageInterface import *
from Interfaces.VisualiseInterface import *
from Interfaces.SimulateInterface import *
from Interfaces.ExperimentInterface import *


qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

if __name__ == "__main__":
    app = qtw.QApplication([])
    stackedWidget = qtw.QStackedWidget()
    stackedWidget.setGeometry(50, 25, 600, 500)

    #Initialise widgets
    homeWidget = StartPage()
    extractGenerateWidget = ExtractGeneratePage()
    simulateWidget = SimulatePage()
    visualiseWidget = VisualisePage()
    experimentWidget = ExperimentPage()

    #Add navigation to widgets once created
    homeWidget.ExtractGenerateButton.clicked.connect(lambda: changePage(stackedWidget, 1))
    homeWidget.SimulateButton.clicked.connect(lambda: changePage(stackedWidget, 2))
    homeWidget.VisualiseButton.clicked.connect(lambda: changePage(stackedWidget, 3))
    homeWidget.ExperimentButton.clicked.connect(lambda: changePage(stackedWidget, 4))
    extractGenerateWidget.ExtractHomeButton.clicked.connect(lambda: changePage(stackedWidget, 0))
    simulateWidget.SimulateHomeButton.clicked.connect(lambda: changePage(stackedWidget, 0))
    visualiseWidget.VisualiseHomeButton.clicked.connect(lambda: changePage(stackedWidget, 0))
    experimentWidget.ExperimentHomeButton.clicked.connect(lambda: changePage(stackedWidget, 0))

    #Add to stacked widget
    stackedWidget.addWidget(homeWidget)
    stackedWidget.addWidget(extractGenerateWidget)
    stackedWidget.addWidget(simulateWidget)
    stackedWidget.addWidget(visualiseWidget)
    stackedWidget.addWidget(experimentWidget)
    stackedWidget.show() 

    app.exec_()

