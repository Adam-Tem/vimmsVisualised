import unittest

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtTest as qtt
from PyQt5 import QtCore as qtc

from ViMMSMain import ViMMSMain
from Interfaces.StartPageInterface import StartPage
from Interfaces.ExtractGenerateInterface import ExtractGeneratePage
from Interfaces.SimulateInterface import SimulatePage
from Interfaces.VisualiseInterface import VisualisePage
from Interfaces.ExperimentInterface import ExperimentPage

class ViMMSTestSuite(unittest.TestCase):

    def setUp(self):
        self.app = qtw.QApplication([])
        self.window = ViMMSMain()

    def test_navigation(self):
        #Starting from the homepage, navigate to every possible page and back.

        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExtractGenerateButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), ExtractGeneratePage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExtractHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().SimulateButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), SimulatePage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().SimulateHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().VisualiseButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), VisualisePage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().VisualiseHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExperimentButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), ExperimentPage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExperimentHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)


if __name__ == "__main__":
    unittest.main()