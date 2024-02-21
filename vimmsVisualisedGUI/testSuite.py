import unittest
import os
import inspect

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtTest as qtt
from PyQt5 import QtCore as qtc

from ViMMSMain import ViMMSMain
from Interfaces.StartPageInterface import StartPage
from Interfaces.ExtractGenerateInterface import ExtractGeneratePage
from Interfaces.SimulateInterface import SimulatePage
from Interfaces.VisualiseInterface import VisualisePage
from Interfaces.ExperimentInterface import ExperimentPage
from Utils.Extract.ExtractData import extract_data
from Utils.Generate.getAssociatedParamBox import get_associated_param_box
from Utils.Generate.RunChemicalMixtureCreator import run_chemical_mixture_creator
from Utils.Parameters.ParamWidgets import *
from testSuiteHelperFunctions import *

from vimms.Controller import *
from vimms.Experiment import ExperimentCase

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



    #---- COMBO BOX PARAMETER CREATION TESTS ----#    
    
    ### Simulation Page ###
    def test_sim_combo_box_creation_topn(self):
        
        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(1)

        constructor_params = inspect.signature(TopNController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)
    
    def test_sim_combo_box_creation_topn_roi(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(2)

        constructor_params = inspect.signature(TopN_RoiController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_sim_combo_box_creation_topn_smart_roi(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(3)

        constructor_params = inspect.signature(TopN_SmartRoiController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_sim_combo_box_creation_topnex(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(4)

        constructor_params = inspect.signature(TopNEXController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_sim_combo_box_creation_hard_roi_excl(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(5)

        constructor_params = inspect.signature(HardRoIExcludeController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_sim_combo_box_creation_intensity_roi_excl(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(6)

        constructor_params = inspect.signature(IntensityRoIExcludeController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_sim_combo_box_creation_non_overlap(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(7)

        constructor_params = inspect.signature(NonOverlapController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_sim_combo_box_creation_intensity_non_overlap(self):

        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(8)

        constructor_params = inspect.signature(IntensityNonOverlapController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    ### Experiment Page ###
    def test_exp_combo_box_creation_topn(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(1)

        constructor_params = inspect.signature(TopNController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)
    
    def test_exp_combo_box_creation_topn_roi(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(2)

        constructor_params = inspect.signature(TopN_RoiController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_exp_combo_box_creation_topn_smart_roi(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(3)

        constructor_params = inspect.signature(TopN_SmartRoiController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_exp_combo_box_creation_topnex(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(4)

        constructor_params = inspect.signature(TopNEXController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_exp_combo_box_creation_hard_roi_excl(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(5)

        constructor_params = inspect.signature(HardRoIExcludeController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_exp_combo_box_creation_intensity_roi_excl(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(6)

        constructor_params = inspect.signature(IntensityRoIExcludeController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_exp_combo_box_creation_non_overlap(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(7)

        constructor_params = inspect.signature(NonOverlapController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    def test_exp_combo_box_creation_intensity_non_overlap(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()
        page.ControllerComboBox.setCurrentIndex(8)

        constructor_params = inspect.signature(IntensityNonOverlapController.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CONTROLLER_PARAMS, page.ParamsBox)
        self.assertTrue(all_params_created)

    ### Generate Page
    
    def test_gen_formula_sampler_combo_box_creation_even_mz(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.FormulaSamplerComboBox.setCurrentIndex(1)

        constructor_params = inspect.signature(EvenMZFormulaSampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params, 
                                                          FORMULA_SAMPLER_PARAMS, page.FormulaSamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_formula_sampler_combo_box_creation_uniform_mz(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.FormulaSamplerComboBox.setCurrentIndex(2)

        constructor_params = inspect.signature(UniformMZFormulaSampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          FORMULA_SAMPLER_PARAMS, page.FormulaSamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_formula_sampler_combo_box_creation_uniform_mz(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.FormulaSamplerComboBox.setCurrentIndex(3)

        constructor_params = inspect.signature(MZMLFormulaSampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          FORMULA_SAMPLER_PARAMS, page.FormulaSamplerParamBox)
        self.assertTrue(all_params_created)
    
    def test_gen_rti_sampler_combo_box_creation_uniform_rt(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.RTISamplerComboBox.setCurrentIndex(1)

        constructor_params = inspect.signature(UniformRTAndIntensitySampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          RTI_SAMPLER_PARAMS, page.RTISamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_rti_sampler_combo_box_creation_mzml(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.RTISamplerComboBox.setCurrentIndex(2)

        constructor_params = inspect.signature(MZMLRTandIntensitySampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          RTI_SAMPLER_PARAMS, page.RTISamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_chromo_sampler_combo_box_creation_gaussian(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.ChromoSamplerComboBox.setCurrentIndex(1)

        constructor_params = inspect.signature(GaussianChromatogramSampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CHROMO_SAMPLER_PARAMS, page.ChromoSamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_chromo_sampler_combo_box_creation_constant(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.ChromoSamplerComboBox.setCurrentIndex(2)

        constructor_params = inspect.signature(ConstantChromatogramSampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CHROMO_SAMPLER_PARAMS, page.ChromoSamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_chromo_sampler_combo_box_creation_mzml(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.ChromoSamplerComboBox.setCurrentIndex(3)

        constructor_params = inspect.signature(MZMLChromatogramSampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          CHROMO_SAMPLER_PARAMS, page.ChromoSamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_ms2_sampler_combo_box_creation_uniform(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.MS2SamplerComboBox.setCurrentIndex(1)

        constructor_params = inspect.signature(UniformMS2Sampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          MS2_SAMPLER_PARAMS, page.MS2SamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_ms2_sampler_combo_box_creation_fixed(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.MS2SamplerComboBox.setCurrentIndex(2)

        constructor_params = inspect.signature(FixedMS2Sampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          MS2_SAMPLER_PARAMS, page.MS2SamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_ms2_sampler_combo_box_creation_mgf(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.MS2SamplerComboBox.setCurrentIndex(3)

        constructor_params = inspect.signature(MGFMS2Sampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          MS2_SAMPLER_PARAMS, page.MS2SamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_ms2_sampler_combo_box_creation_mzml(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.MS2SamplerComboBox.setCurrentIndex(4)

        constructor_params = inspect.signature(MZMLMS2Sampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          MS2_SAMPLER_PARAMS, page.MS2SamplerParamBox)
        self.assertTrue(all_params_created)

    def test_gen_ms2_sampler_combo_box_creation_crpm(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        page.MS2SamplerComboBox.setCurrentIndex(5)

        constructor_params = inspect.signature(CRPMS2Sampler.__init__).parameters
        all_params_created = check_controller_params(constructor_params,
                                                          MS2_SAMPLER_PARAMS, page.MS2SamplerParamBox)
        self.assertTrue(all_params_created)

    ###---- EXTRACT PAGE HELPER FUNCTIONS ----###
        
    def test_extract_data(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()
        qtt.QTest.mouseClick(page.tabWidget.tabBar(), qtc.Qt.LeftButton, 
                               pos=page.tabWidget.tabBar().tabRect(0).center())
        
        qtt.QTest.keyClicks(page.ExtractFileNameTextEdit, "extract_data_test_result")
        
        param_box = page.ExtractParamBox
        file_name = "test_mzml.mzML"
        save_directory = SAVE_DIRECTORY
        extract_data(param_box, file_name, page.ExtractFileNameTextEdit.text(), save_directory)
        
        self.assertTrue(os.path.exists(os.path.join(SAVE_DIRECTORY, "extracted_data",
                                                     page.ExtractFileNameTextEdit.text()+".p")))

    ###---- GENERATE PAGE HELPER FUNCTIONS ----###

    def test_get_associated_param_box(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()

        selected_param_box = get_associated_param_box(page.ParamBox, "Even MZ Formula Sampler")
        self.assertEqual(selected_param_box, page.FormulaSamplerParamBox)
    
    def test_run_chemical_mixture_creator(self):

        self.window.stackedWidget.setCurrentIndex(1)
        page = self.window.stackedWidget.currentWidget()

        page.FormulaSamplerComboBox.setCurrentIndex(1)
        page.RTISamplerComboBox.setCurrentIndex(1)
        page.ChromoSamplerComboBox.setCurrentIndex(1)
        page.MS2SamplerComboBox.setCurrentIndex(1)

        qtt.QTest.keyClicks(page.GenerateFileNameTextEdit, "chemical_mixture_creator_test_result")

        run_chemical_mixture_creator(page.ParamBox, page.AdductPropTextEdit.text(),
                                     page.ChemsToSampleTextEdit.text(), page.MS2LevelSpinBox.value(),
                                     page.GenerateFileNameTextEdit.text())

        self.assertTrue(os.path.exists(os.path.join(SAVE_DIRECTORY, "generated_data", 
                                                    "chemical_mixture_creator_test_result.p")))
        
    ###---- EXPERIMENT PAGE HELPER FUNCTIONS AND BUTTONS ----###
        
    def test_add_fullscan_to_list_button(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()

        page.fullscan_upload_button.file_name = "test_mzml.mzML"
        page.fullscan_upload_button.file_location = os.path.join(os.getcwd(), "test_mzml.mzML")
        page.NoOfInjectionsSpinBox.setValue(2)
        page.AddFullscanButton.setEnabled(True)
        qtt.QTest.mouseClick(page.AddFullscanButton, qtc.Qt.LeftButton)

        self.assertEqual(page.fullscan_list, ["test_mzml.mzML", "test_mzml.mzML"])

    def test_fullscan_undo_button(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()

        qtt.QTest.mouseClick(page.InjectionUndoButton, qtc.Qt.LeftButton)

        self.assertTrue(page.fullscan_list == ["test_mzml.mzML"])

    def test_add_experiment_case_button(self):

        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()

        page.ControllerComboBox.setCurrentIndex(1)
        qtt.QTest.keyClicks(page.CaseNameTextEdit, "construct_exp_case_test")
        page.AddExperimentCaseButton.setEnabled(True)
        qtt.QTest.mouseClick(page.AddExperimentCaseButton, qtc.Qt.LeftButton)
        self.app.processEvents()
        self.assertTrue((len(page.experiment_case_list) == 1) and 
                        (type(page.experiment_case_list[0]) == ExperimentCase))
        
    
    def test_case_undo_button(self):
        
        self.window.stackedWidget.setCurrentIndex(4)
        page = self.window.stackedWidget.currentWidget()

        qtt.QTest.mouseClick(page.CaseUndoButton, qtc.Qt.LeftButton)

        self.assertTrue(len(page.experiment_case_list) == 0 and 
                        len(page.experiment_name_list) == 0)


    def test_simulate_btn(self):
        
        self.window.stackedWidget.setCurrentIndex(2)
        page = self.window.stackedWidget.currentWidget()

        page.ControllerComboBox.setCurrentIndex(1)

        for param_line_edit in page.ParamsBox.findChildren(qtw.QLineEdit):
            qtt.QTest.keyClicks(param_line_edit, "10")
        
        page.ParamsBox.findChildren(qtw.QSpinBox)[0].setValue(2)

        page.p_upload_button.file_name = "test.p"
        page.p_upload_button.file_location = os.path.join(os.getcwd(), "test.p")

        qtt.QTest.keyClicks(page.OutputFileTextEdit, "test_sim")

        qtt.QTest.mouseClick(page.SimulateButton, qtc.Qt.LeftButton)

        qtc.QCoreApplication.processEvents()
        # qtt.QTest.qSleep(20000)
        qtt.QTest.qWaitForWindowActive(self.window.stackedWidget)

        self.assertTrue(os.path.exists(os.path.join(SAVE_DIRECTORY, "simulations", "test_sim.mzML")))

        
if __name__ == "__main__":
    unittest.main()