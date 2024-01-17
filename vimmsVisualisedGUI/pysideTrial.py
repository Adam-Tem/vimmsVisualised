import sys
from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QApplication, QDesktopWidget, QLineEdit,
    QMainWindow, QPushButton, QToolBar)
from PySide2.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class StubWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, type, isMainFrame):
        if (type == QWebEnginePage.NavigationTypeLinkClicked):
            print("This should only fire if you click a link.")
        return QWebEnginePage.acceptNavigationRequest(self, url, type, isMainFrame)

class MainWindow(QMainWindow):

    def death(i, p):
        print(i, p)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('PySide2 WebEngineWidgets Example')

        self.toolBar = QToolBar()
        self.addToolBar(self.toolBar)
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/left-32.png'))
        self.backButton.clicked.connect(self.back)
        self.toolBar.addWidget(self.backButton)
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.addressLineEdit)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'http://qt.io'
        self.addressLineEdit.setText(initialUrl)
        page = StubWebEnginePage(self.webEngineView)
        self.webEngineView.setPage(page)
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)
        self.webEngineView.setUrl(QUrl("https://google.com/"))
        self.webEngineView.renderProcessTerminated.connect(self.death)

    

    def load(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    availableGeometry = app.desktop().availableGeometry(mainWin)
    mainWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
    mainWin.show()
    sys.exit(app.exec_())