import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import os

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

def handleLoadFinished(ok, lol):
    print(ok, lol)

def render(screen):
    screen.load(qtc.QUrl(os.path.join(current_dir, "test.html")))
    print(screen.loadFinished)

def add_val(layout):

    current_dir = os.getcwd()
    page = QWebEngineView()
    page.setHtml("test.html", qtc.QUrl.fromLocalFile(os.path.join(current_dir, "test.html")))
    layout.addWidget(page)


app = qtw.QApplication([])
window = qtw.QMainWindow()

layout = qtw.QVBoxLayout()

view = QWebEngineView()
current_dir = os.getcwd()
view.setUrl(qtc.QUrl.fromLocalFile(os.path.join(current_dir, "temp-plot.html")))

cache_path = "C:/Users/adams/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/Local"



btn = qtw.QPushButton()
btn2 = qtw.QPushButton("render")
btn2.clicked.connect(lambda: render(view))
btn.clicked.connect(lambda: add_val(layout))
btn.clicked.connect(lambda: print("btn press"))
layout.addWidget(btn)
view.renderProcessTerminated.connect(handleLoadFinished)
layout.addWidget(view)
layout.addWidget(btn2)
placeholder = qtw.QWidget()
placeholder.setLayout(layout)
window.setCentralWidget(placeholder)
window.show()
sys.exit(app.exec_())

# import sys


# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWebEngineWidgets import *




# class WebEnginePage(QWebEnginePage):
#     def certificateError(self, error):
#         # If you want to ignore the certificates of certain pages
#         # then do something like
#         # if error.url() == QUrl("https://www.us.army.mil/"):
#         #     error.ignoreCertificateError()
#         #     return True
#         # return super().certificateError(error)

#         error.ignoreCertificateError()
#         return True


# def main(args):
#     app = QApplication(args)
#     QWebEngineSettings.globalSettings().setDefaultTextEncoding("utf-8")
#     webview = QWebEngineView()
#     page = WebEnginePage()
#     webview.setPage(page)
#     webview.load(QUrl("https://www.google.com"))
#     webview.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main(sys.argv)


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtCore import QUrl
# import os 

# class MyMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Create a central widget to hold the layout
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         # Create a vertical layout
#         layout = QVBoxLayout(central_widget)

#         # Create a QWebEngineView
#         self.web_view = QWebEngineView()

#         # Connect to the loadFinished signal
#         self.web_view.renderProcessTerminated.connect(self.handleLoadFinished)

#         # Add the QWebEngineView to the layout
#         layout.addWidget(self.web_view)

#         # Set the layout for the central widget
#         central_widget.setLayout(layout)

#         # Load a URL

#         dirhre = os.getcwd()
#         pathhere = os.path.join(dirhre, "test.html")
        
#         self.web_view.setUrl(QUrl.fromLocalFile(pathhere))

#     def handleLoadFinished(self, ok):
#         if ok:
#             print(ok)
#         else:
#             print("Error loading web page. Check for details.")

# def main():
#     app = QApplication(sys.argv)
#     window = MyMainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()