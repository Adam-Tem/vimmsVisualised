from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from Interfaces.ExtractGenerateInterface import *
from Interfaces.StartPageInterface import *

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

if __name__ == "__main__":
    app = qtw.QApplication([])
    stackedWidget = qtw.QStackedWidget()
    stackedWidget.setGeometry(50, 25, 600, 500)

    #Initialise widgets
    homeWidget = StartPage()
    extractGenerateWidget = ExtractGeneratePage()
    #Add navigation to widgets once created
    homeWidget.ExtractGenerateButton.clicked.connect(lambda: changePage(stackedWidget, 1))
    extractGenerateWidget.ExtractHomeButton.clicked.connect(lambda: changePage(stackedWidget, 0))
    #Add to stacked widget
    stackedWidget.addWidget(homeWidget)
    stackedWidget.addWidget(extractGenerateWidget)
    stackedWidget.show()

    app.exec_()

