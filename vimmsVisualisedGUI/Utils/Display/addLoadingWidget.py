from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
def add_loading_widget(loading_label):
    
    loading_label.hide()
    loading_gif = qtg.QMovie("Images/loading.gif")
    loading_label.setAlignment(qtc.Qt.AlignCenter)
    loading_label.setMovie(loading_gif)
    loading_label.movie().start()