import unittest
import os
import time

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtTest as qtt
from PyQt5 import QtCore as qtc

from ViMMSMain import ViMMSMain
from Interfaces.StartPageInterface import StartPage
from Interfaces.ExtractGenerateInterface import ExtractGeneratePage
from Interfaces.SimulateInterface import SimulatePage
from Interfaces.VisualiseInterface import VisualisePage
from Interfaces.ExperimentInterface import ExperimentPage
from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY

class ViMMSTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = qtw.QApplication([])
        cls.window = ViMMSMain()


    ## ---- NAVIGATION TESTING ---- ##
    def test_nav_home_extract(self):
        self.window.stackedWidget.setCurrentIndex(0)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExtractGenerateButton, 
                            qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), ExtractGeneratePage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExtractHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)
    
    def test_nav_home_simulate(self):
        self.window.stackedWidget.setCurrentIndex(0)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().SimulateButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), SimulatePage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().SimulateHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)
    
    def test_nav_home_visualise(self):
        self.window.stackedWidget.setCurrentIndex(0)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().VisualiseButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), VisualisePage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().VisualiseHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)

    def test_nav_home_experiment(self):
        self.window.stackedWidget.setCurrentIndex(0)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExperimentButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), ExperimentPage)
        qtt.QTest.mouseClick(self.window.stackedWidget.currentWidget().ExperimentHomeButton, 
                             qtc.Qt.LeftButton)
        self.assertEqual(type(self.window.stackedWidget.currentWidget()), StartPage)

    ## ---- BUTTON EXECUTION TESTING ---- ##
    def test_extract_btn(self):
        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        qtt.QTest.mouseClick(page.tabWidget.tabBar(), qtc.Qt.LeftButton, 
                              pos=page.tabWidget.tabBar().tabRect(0).center())
        page.extract_upload_button.file_name = "test_mzml.mzML"
        page.extract_upload_button.file_location = os.path.join(os.getcwd(), "test_mzml.mzML")
        param_box = page.ExtractParamBox

        for param_line_edit in param_box.findChildren(qtw.QLineEdit):
            qtt.QTest.keyClicks(param_line_edit, "10")
        
        qtt.QTest.keyClicks(page.ExtractFileNameTextEdit, "extract_test")
        qtt.QTest.mouseClick(page.ExtractDataButton, qtc.Qt.LeftButton)
        self.app.processEvents()

        self.assertTrue(os.path.exists(os.path.join(SAVE_DIRECTORY, "extracted_data", "extract_test.p")))

    # def test_generate_btn(self):

    #     self.window.stackedWidget.setCurrentIndex(1)
    #     page = self.window.stackedWidget.currentWidget()

    #     page.FormulaSamplerComboBox.setCurrentIndex(1)
    #     page.RTISamplerComboBox.setCurrentIndex(1)
    #     page.ChromoSamplerComboBox.setCurrentIndex(1)
    #     page.MS2SamplerComboBox.setCurrentIndex(1)

    #     qtt.QTest.keyClicks(page.GenerateFileNameTextEdit, "generate_test")
    #     qtt.QTest.mouseClick(page.GenerateDataButton, qtc.Qt.LeftButton)

    #     self.app.processEvents()
    #     qtt.QTest.keyClick(self.window, qtc.Qt.Key_Enter)

    #     self.assertTrue(os.path.exists(os.path.join(SAVE_DIRECTORY, "generated_data", "generate_test.p")))

    ### you can't perform clicks on a QFileDialog.....
    # def test_save_state_btn(self):
        
    #     self.window.stackedWidget.setCurrentIndex(2)
    #     page = self.window.stackedWidget.currentWidget()

    #     page.ControllerComboBox.setCurrentIndex(1)
        
    #     for param_line_edit in page.ParamsBox.findChildren(qtw.QLineEdit):
    #         qtt.QTest.keyClicks(param_line_edit, "10")
        
    #     pass

    # def test_simulate_btn(self):
        
    #     self.window.stackedWidget.setCurrentIndex(2)
    #     page = self.window.stackedWidget.currentWidget()

    #     page.ControllerComboBox.setCurrentIndex(1)

    #     for param_line_edit in page.ParamsBox.findChildren(qtw.QLineEdit):
    #         qtt.QTest.keyClicks(param_line_edit, "10")
        
    #     page.ParamsBox.findChildren(qtw.QSpinBox)[0].setValue(2)

    #     page.p_upload_button.file_name = "test.p"
    #     page.p_upload_button.file_location = os.path.join(os.getcwd(), "test.p")

    #     qtt.QTest.keyClicks(page.OutputFileTextEdit, "test_sim")

    #     qtt.QTest.mouseClick(page.SimulateButton, qtc.Qt.LeftButton)

    #     self.app.processEvents()

    #     msg_box = self.window.stackedWidget.currentWidget().findChild(qtw.QMessageBox)
    #     qtt.QTest.mouseClick(msg_box.button(qtw.QMessageBox.Ok), qtc.Qt.LeftButton)

    #     self.assertTrue(os.path.exists(os.path.join(SAVE_DIRECTORY, "simulations", "test_sim.mzML")))

if __name__ == "__main__":
    unittest.main()