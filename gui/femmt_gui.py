import sys

import gmsh
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import femmt as fmt
import json

# import sys
# import matplotlib
#
# matplotlib.use('Qt5Agg')
#
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi('femmt_gui.ui', self)
        _translate = QtCore.QCoreApplication.translate
        # self.setWindowIcon(QIcon('Images\\logo.png'))
        self.setWindowTitle(_translate("MainWindow", "Femmt ToolBox"))
        pixmap = QPixmap('ferriteCore.png')
        #self.coreImageLabel.setPixmap(pixmap)
        #self.imageBoxImageLabel.setPixmap(pixmap)
        self.translation_dict =  {
            # key: Used in FEMMT code
            # value: Used in GUI
            "inductor": "inductor",
            "transformer": "transformer",
            "integrated transformer": "transformer with integrated stray path",
            "litz": "Litz Wire",
            "solid": "Solid Round Wire",
            "implicit_litz_radius": 'Litz Radius',
            "implicit_ff": "Fill Factor",
            "implicit_strands_number": "Strands count",
            "center": "Center Placement",
            "random": "Random Placement",
            "percent": "Percent",
            "manually": "Manual Placement",
            "hexa": "Hexadimensional",
            "square": "Square"
        }

        "Signals in Definition Tab"
        self.md_simulation_type_comboBox.currentTextChanged.connect(self.md_change_simulation_type)
        self.md_winding1_implicit_litz_comboBox.currentTextChanged.connect(self.md_winding1_change_litz_implicit)
        self.md_winding1_type_comboBox.currentTextChanged.connect(self.md_winding1_change_wire_type)
        self.md_air_gap_count_comboBox.currentTextChanged.connect(self.md_change_air_gap_count)
        self.md_air_gap_placement_method_comboBox.currentTextChanged.connect(self.md_change_air_gap_placement)
        self.md_gmsh_visualisation_QPushButton.clicked.connect(self.md_gmsh_pre_visualisation)

        "Signals in Excitation Tab"
        self.md_fk1_checkBox.stateChanged.connect(self.md_change_frequencies_1)
        self.md_fk2_checkBox.stateChanged.connect(self.md_change_frequencies_2)
        self.md_fk3_checkBox.stateChanged.connect(self.md_change_frequencies_3)
        self.md_fk4_checkBox.stateChanged.connect(self.md_change_frequencies_4)
        self.md_fk5_checkBox.stateChanged.connect(self.md_change_frequencies_5)
        self.md_fk6_checkBox.stateChanged.connect(self.md_change_frequencies_6)
        self.md_fk7_checkBox.stateChanged.connect(self.md_change_frequencies_7)
        self.md_fk8_checkBox.stateChanged.connect(self.md_change_frequencies_8)
        self.md_excitation_update_graph_Button.clicked.connect(self.md_redraw_input_signals)

        "Signals in Simulation Tab"
        self.md_simulation_QPushButton.clicked.connect(self.md_action_run_simulation)

        # initialize checkboxes. Need to be set to True and then to False, so represent a change and the signal
        # triggers the action to uncheck all boxes
        self.md_fk1_checkBox.setChecked(True)
        self.md_fk2_checkBox.setChecked(True)
        self.md_fk3_checkBox.setChecked(True)
        self.md_fk4_checkBox.setChecked(True)
        self.md_fk5_checkBox.setChecked(True)
        self.md_fk6_checkBox.setChecked(True)
        self.md_fk7_checkBox.setChecked(True)
        self.md_fk8_checkBox.setChecked(True)
        # self.md_fk1_checkBox.setChecked(False)
        self.md_fk2_checkBox.setChecked(False)
        self.md_fk3_checkBox.setChecked(False)
        self.md_fk4_checkBox.setChecked(False)
        self.md_fk5_checkBox.setChecked(False)
        self.md_fk6_checkBox.setChecked(False)
        self.md_fk7_checkBox.setChecked(False)
        self.md_fk8_checkBox.setChecked(False)

        "Init controls"
        self.md_initialize_controls()

    def md_initialize_controls(self):
        md_simulation_type_options = [self.translation_dict['inductor'], self.translation_dict['transformer']]
        md_core_material_options = ['N95']
        md_winding_material = ['Copper']
        md_winding_type = [self.translation_dict['litz'], self.translation_dict['solid']]
        md_implicit_litz = [self.translation_dict["implicit_litz_radius"], self.translation_dict["implicit_ff"], self.translation_dict['implicit_strands_number']]
        md_air_gap_method = [self.translation_dict['manually'], self.translation_dict["percent"]]
        md_air_gap_counts = ['0', '1', '2', '3', '4', '5']
        md_winding_scheme = [self.translation_dict["square"], self.translation_dict["hexa"]]

        for option in md_simulation_type_options:
            self.md_simulation_type_comboBox.addItem(option)
        for option in md_core_material_options:
            self.md_core_material_comboBox.addItem(option)
        for option in md_winding_material:
            self.md_winding1_material_comboBox.addItem(option)
            self.md_winding2_material_comboBox.addItem(option)
        for option in md_winding_type:
            self.md_winding1_type_comboBox.addItem(option)
            self.md_winding2_type_comboBox.addItem(option)
        for option in md_implicit_litz:
            self.md_winding1_implicit_litz_comboBox.addItem(option)
            self.md_winding2_implicit_litz_comboBox.addItem(option)
        for option in md_air_gap_method:
            self.md_air_gap_placement_method_comboBox.addItem(option)
        for option in md_air_gap_counts:
            self.md_air_gap_count_comboBox.addItem(option)
        for option in md_winding_scheme:
            self.md_winding1_scheme_comboBox.addItem(option)

    def md_gmsh_pre_visualisation(self):
        geo = fmt.MagneticComponent(component_type="inductor")
        geo.Mesh.generate_hybrid_mesh(do_meshing=False)





    def md_winding2_enable(self, status: bool) -> None:
        """
        Enable/disable all fields being in contact with winding 2.

        :param status: True / False
        :type status: bool
        :return: None
        :rtype: None
        """
        # set winding definitions of winding 2
        self.md_winding2_material_comboBox.setEnabled(status)
        self.md_winding2_type_comboBox.setEnabled(status)
        self.md_winding2_turns_lineEdit.setEnabled(status)
        self.md_winding2_implicit_litz_comboBox.setEnabled(status)
        self.md_winding2_strands_lineEdit.setEnabled(status)
        self.md_winding2_radius_lineEdit.setEnabled(status)
        self.md_winding2_fill_factor_lineEdit.setEnabled(status)
        self.md_winding2_strand_radius_comboBox.setEnabled(status)

        # set current shapes of winding 2
        self.md_winding2_ik1_lineEdit.setEnabled(status)
        self.md_winding2_ik2_lineEdit.setEnabled(status)
        self.md_winding2_ik3_lineEdit.setEnabled(status)
        self.md_winding2_ik4_lineEdit.setEnabled(status)
        self.md_winding2_ik5_lineEdit.setEnabled(status)
        self.md_winding2_ik6_lineEdit.setEnabled(status)
        self.md_winding2_ik7_lineEdit.setEnabled(status)
        self.md_winding2_ik8_lineEdit.setEnabled(status)
        self.md_winding2_pk1_lineEdit.setEnabled(status)
        self.md_winding2_pk2_lineEdit.setEnabled(status)
        self.md_winding2_pk3_lineEdit.setEnabled(status)
        self.md_winding2_pk4_lineEdit.setEnabled(status)
        self.md_winding2_pk5_lineEdit.setEnabled(status)
        self.md_winding2_pk6_lineEdit.setEnabled(status)
        self.md_winding2_pk7_lineEdit.setEnabled(status)
        self.md_winding2_pk8_lineEdit.setEnabled(status)

        self.md_isolation_s2s_lineEdit.setEnabled(status)
        self.md_isolation_p2s_lineEdit.setEnabled(status)
        self.md_isolation_s2core_lineEdit.setEnabled(status)


    def md_f1_enable(self, status: bool) -> None:
        self.md_winding1_ik1_lineEdit.setEnabled(status)
        self.md_winding1_pk1_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik1_lineEdit.setEnabled(False)
            self.md_winding2_pk1_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik1_lineEdit.setEnabled(status)
            self.md_winding2_pk1_lineEdit.setEnabled(status)

    def md_f2_enable(self, status: bool) -> None:
        self.md_winding1_ik2_lineEdit.setEnabled(status)
        self.md_winding1_pk2_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik2_lineEdit.setEnabled(False)
            self.md_winding2_pk2_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik2_lineEdit.setEnabled(status)
            self.md_winding2_pk2_lineEdit.setEnabled(status)

    def md_f3_enable(self, status: bool) -> None:
        self.md_winding1_ik3_lineEdit.setEnabled(status)
        self.md_winding1_pk3_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik3_lineEdit.setEnabled(False)
            self.md_winding2_pk3_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik3_lineEdit.setEnabled(status)
            self.md_winding2_pk3_lineEdit.setEnabled(status)

    def md_f4_enable(self, status: bool) -> None:
        self.md_winding1_ik4_lineEdit.setEnabled(status)
        self.md_winding1_pk4_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik4_lineEdit.setEnabled(False)
            self.md_winding2_pk4_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik4_lineEdit.setEnabled(status)
            self.md_winding2_pk4_lineEdit.setEnabled(status)

    def md_f5_enable(self, status: bool) -> None:
        self.md_winding1_ik5_lineEdit.setEnabled(status)
        self.md_winding1_pk5_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik5_lineEdit.setEnabled(False)
            self.md_winding2_pk5_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik5_lineEdit.setEnabled(status)
            self.md_winding2_pk5_lineEdit.setEnabled(status)

    def md_f6_enable(self, status: bool) -> None:
        self.md_winding1_ik6_lineEdit.setEnabled(status)
        self.md_winding1_pk6_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik6_lineEdit.setEnabled(False)
            self.md_winding2_pk6_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik6_lineEdit.setEnabled(status)
            self.md_winding2_pk6_lineEdit.setEnabled(status)

    def md_f7_enable(self, status: bool) -> None:
        self.md_winding1_ik7_lineEdit.setEnabled(status)
        self.md_winding1_pk7_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik7_lineEdit.setEnabled(False)
            self.md_winding2_pk7_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik7_lineEdit.setEnabled(status)
            self.md_winding2_pk7_lineEdit.setEnabled(status)

    def md_f8_enable(self, status: bool) -> None:
        self.md_winding1_ik8_lineEdit.setEnabled(status)
        self.md_winding1_pk8_lineEdit.setEnabled(status)
        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor'] and status:
            self.md_winding2_ik8_lineEdit.setEnabled(False)
            self.md_winding2_pk8_lineEdit.setEnabled(False)
        else:
            self.md_winding2_ik8_lineEdit.setEnabled(status)
            self.md_winding2_pk8_lineEdit.setEnabled(status)

    def md_air_gap_1_enable(self, status: bool) -> None:
        self.md_air_gap_1_length_lineEdit.setEnabled(status)
        self.md_air_gap_1_position_lineEdit.setEnabled(status)

    def md_air_gap_2_enable(self, status: bool) -> None:
        self.md_air_gap_2_length_lineEdit.setEnabled(status)
        self.md_air_gap_2_position_lineEdit.setEnabled(status)

    def md_air_gap_3_enable(self, status: bool) -> None:
        self.md_air_gap_3_length_lineEdit.setEnabled(status)
        self.md_air_gap_3_position_lineEdit.setEnabled(status)

    def md_air_gap_4_enable(self, status: bool) -> None:
        self.md_air_gap_4_length_lineEdit.setEnabled(status)
        self.md_air_gap_4_position_lineEdit.setEnabled(status)

    def md_air_gap_5_enable(self, status: bool) -> None:
        self.md_air_gap_5_length_lineEdit.setEnabled(status)
        self.md_air_gap_5_position_lineEdit.setEnabled(status)

    def md_change_simulation_type(self, simulation_type_from_combo_box: str) -> None:
        """
        Action performed when signal of md_simulation_type_comboBox text has changed.
        Action will be enabling / disabling user inputs for not-used windings.

        :param simulation_type_from_combo_box:
        :type simulation_type_from_combo_box: str
        :return: None
        :rtype: None
        """
        if simulation_type_from_combo_box == self.translation_dict['inductor']:
            self.md_winding2_enable(False)

        elif simulation_type_from_combo_box == self.translation_dict['transformer']:
            # set winding definitions of winding 2 to editable
            self.md_winding2_enable(True)

        elif simulation_type_from_combo_box == self.translation_dict['integrated transformer']:
            # set winding definitions of winding 2 to editable
            self.md_winding2_enable(True)

    def md_winding1_change_litz_implicit(self, implicit_type_from_combo_box: str) -> None:
        if implicit_type_from_combo_box == self.translation_dict['implicit_litz_radius']:
            self.md_winding1_strands_lineEdit.setEnabled(True)
            self.md_winding1_fill_factor_lineEdit.setEnabled(True)
            self.md_winding1_strand_radius_comboBox.setEnabled(True)
            self.md_winding1_radius_lineEdit.setEnabled(False)
        if implicit_type_from_combo_box == self.translation_dict['implicit_strands_number']:
            self.md_winding1_strands_lineEdit.setEnabled(False)
            self.md_winding1_fill_factor_lineEdit.setEnabled(True)
            self.md_winding1_strand_radius_comboBox.setEnabled(True)
            self.md_winding1_radius_lineEdit.setEnabled(True)
        if implicit_type_from_combo_box == self.translation_dict['implicit_ff']:
            self.md_winding1_strands_lineEdit.setEnabled(True)
            self.md_winding1_fill_factor_lineEdit.setEnabled(False)
            self.md_winding1_strand_radius_comboBox.setEnabled(True)
            self.md_winding1_radius_lineEdit.setEnabled(True)

    def md_winding1_change_wire_type(self, wire_type_from_combot_box: str) -> None:
        self.md_winding1_change_litz_implicit(self.md_winding1_implicit_litz_comboBox.currentText())
        if wire_type_from_combot_box == self.translation_dict['litz']:
            self.md_winding1_strands_lineEdit.setEnabled(True)
            self.md_winding1_implicit_litz_comboBox.setEnabled(True)
            self.md_winding1_fill_factor_lineEdit.setEnabled(True)
            self.md_winding1_strand_radius_comboBox.setEnabled(True)
            self.md_winding1_radius_lineEdit.setEnabled(True)

        elif wire_type_from_combot_box == self.translation_dict['solid']:
            self.md_winding1_strands_lineEdit.setEnabled(False)
            self.md_winding1_implicit_litz_comboBox.setEnabled(False)
            self.md_winding1_fill_factor_lineEdit.setEnabled(False)
            self.md_winding1_strand_radius_comboBox.setEnabled(False)
            self.md_winding1_radius_lineEdit.setEnabled(True)



    def md_change_frequencies_1(self, status) -> None:
        self.md_f1_enable(False) if status == 0 else self.md_f1_enable(True)

    def md_change_frequencies_2(self, status) -> None:
        self.md_f2_enable(False) if status == 0 else self.md_f2_enable(True)

    def md_change_frequencies_3(self, status) -> None:
        self.md_f3_enable(False) if status == 0 else self.md_f3_enable(True)

    def md_change_frequencies_4(self, status) -> None:
        self.md_f4_enable(False) if status == 0 else self.md_f4_enable(True)

    def md_change_frequencies_5(self, status) -> None:
        self.md_f5_enable(False) if status == 0 else self.md_f5_enable(True)

    def md_change_frequencies_6(self, status) -> None:
        self.md_f6_enable(False) if status == 0 else self.md_f6_enable(True)

    def md_change_frequencies_7(self, status) -> None:
        self.md_f7_enable(False) if status == 0 else self.md_f7_enable(True)

    def md_change_frequencies_8(self, status) -> None:
        self.md_f8_enable(False) if status == 0 else self.md_f8_enable(True)

    def md_redraw_input_signals(self):

        winding1_frequency_list = []
        winding1_amplitude_list = []
        winding1_phi_rad_list = []

        winding2_frequency_list = []
        winding2_amplitude_list = []
        winding2_phi_rad_list = []

        if self.md_fk1_checkBox.isChecked():
            winding1_frequency_list.append(1 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik1_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk1_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(1 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik1_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk1_lineEdit.text()))
        if self.md_fk2_checkBox.isChecked():
            winding1_frequency_list.append(2 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik2_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk2_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(2 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik2_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk2_lineEdit.text()))
        if self.md_fk3_checkBox.isChecked():
            winding1_frequency_list.append(3 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik3_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk3_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(3 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik2_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk2_lineEdit.text()))
        if self.md_fk4_checkBox.isChecked():
            winding1_frequency_list.append(4 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik4_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk4_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(4 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik4_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk4_lineEdit.text()))
        if self.md_fk5_checkBox.isChecked():
            winding1_frequency_list.append(5 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik5_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk5_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(5 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik5_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk5_lineEdit.text()))
        if self.md_fk6_checkBox.isChecked():
            winding1_frequency_list.append(6 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik6_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk6_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(6 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik6_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk6_lineEdit.text()))
        if self.md_fk7_checkBox.isChecked():
            winding1_frequency_list.append(7 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik7_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk7_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(7 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik7_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk7_lineEdit.text()))
        if self.md_fk8_checkBox.isChecked():
            winding1_frequency_list.append(8 * float(self.md_base_frequency_lineEdit.text()))
            winding1_amplitude_list.append(float(self.md_winding1_ik8_lineEdit.text()))
            winding1_phi_rad_list.append(float(self.md_winding1_pk8_lineEdit.text()))
            if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
                winding2_frequency_list.append(8 * float(self.md_base_frequency_lineEdit.text()))
                winding2_amplitude_list.append(float(self.md_winding2_ik8_lineEdit.text()))
                winding2_phi_rad_list.append(float(self.md_winding2_pk8_lineEdit.text()))



        fmt.plot_fourier_coefficients(winding1_frequency_list, winding1_amplitude_list, winding1_phi_rad_list, figure_directory =  "./md_winding_1.png")
        pixmap = QPixmap("./md_winding_1.png")
        self.md_graphic_winding_1.setPixmap(pixmap)
        self.md_graphic_winding_1.setMask(pixmap.mask())
        self.md_graphic_winding_1.show()
        if self.md_simulation_type_comboBox.currentText() != self.translation_dict['inductor']:
            fmt.plot_fourier_coefficients(winding2_frequency_list, winding2_amplitude_list, winding2_phi_rad_list, figure_directory = "./md_winding_2.png")
            pixmap = QPixmap("./md_winding_2.png")
            self.md_graphic_winding_2.setPixmap(pixmap)
            self.md_graphic_winding_2.setMask(pixmap.mask())
            self.md_graphic_winding_2.show()




    def md_change_air_gap_count(self, air_gap_count_from_combo_box):
        self.md_air_gap_placement_method_comboBox.setEnabled(False)
        self.md_air_gap_1_enable(False)
        self.md_air_gap_2_enable(False)
        self.md_air_gap_3_enable(False)
        self.md_air_gap_4_enable(False)
        self.md_air_gap_5_enable(False)
        if int(air_gap_count_from_combo_box) >= 1:
            self.md_air_gap_1_enable(True)
            self.md_air_gap_placement_method_comboBox.setEnabled(True)
        if int(air_gap_count_from_combo_box) >= 2:
            self.md_air_gap_2_enable(True)
        if int(air_gap_count_from_combo_box) >= 3:
            self.md_air_gap_3_enable(True)
        if int(air_gap_count_from_combo_box) >= 4:
            self.md_air_gap_4_enable(True)
        if int(air_gap_count_from_combo_box) >= 5:
            self.md_air_gap_5_enable(True)

    def md_change_air_gap_placement(self, air_gap_placement_from_combo_box):
        if air_gap_placement_from_combo_box == self.translation_dict['manually']:
            md_air_gap_placement_text = 'Position'
        elif air_gap_placement_from_combo_box == self.translation_dict['percent']:
            md_air_gap_placement_text = 'Position in [%]'
        self.md_air_gap_1_position_label.setText(md_air_gap_placement_text)
        self.md_air_gap_2_position_label.setText(md_air_gap_placement_text)
        self.md_air_gap_3_position_label.setText(md_air_gap_placement_text)
        self.md_air_gap_4_position_label.setText(md_air_gap_placement_text)
        self.md_air_gap_5_position_label.setText(md_air_gap_placement_text)


    def md_action_run_simulation(self) -> None:
        """
        Run the simulation.

        :return: None
        :rtype: None
        """



        if self.md_simulation_type_comboBox.currentText() == self.translation_dict['inductor']:
            self.md_simulation_QLabel.setText('simulation startet...')

            geo = fmt.MagneticComponent(component_type="inductor")

            # -----------------------------------------------
            # Core
            # -----------------------------------------------

            geo.core.update(type="EI",
                            core_h=float(self.md_core_height_lineEdit.text()),
                            core_w=float(self.md_core_width_lineEdit.text()),
                            window_h=float(self.md_window_height_lineEdit.text()),
                            window_w=float(self.md_window_width_lineEdit.text()))

            # -----------------------------------------------
            # Air Gaps
            # -----------------------------------------------

            air_gap_count = int(self.md_air_gap_count_comboBox.currentText())
            air_gap_heigth_array = []
            air_gap_position_array = []
            air_gap_position_tag_array = []

            if air_gap_count >= 1:
                md_air_gap_1_height = float(self.md_air_gap_1_length_lineEdit.text())
                md_air_gap_1_position = float(self.md_air_gap_1_position_lineEdit.text())
                air_gap_heigth_array.append(md_air_gap_1_height)
                air_gap_position_array.append(md_air_gap_1_position)
                air_gap_position_tag_array.append(0)
            if air_gap_count >= 2:
                md_air_gap_2_height = float(self.md_air_gap_2_length_lineEdit.text())
                md_air_gap_2_position = float(self.md_air_gap_2_position_lineEdit.text())
                air_gap_heigth_array.append(md_air_gap_2_height)
                air_gap_position_array.append(md_air_gap_2_position)
                air_gap_position_tag_array.append(0)
            if air_gap_count >= 3:
                md_air_gap_3_height = float(self.md_air_gap_3_length_lineEdit.text())
                md_air_gap_3_position = float(self.md_air_gap_3_position_lineEdit.text())
                air_gap_heigth_array.append(md_air_gap_3_height)
                air_gap_position_array.append(md_air_gap_3_position)
                air_gap_position_tag_array.append(0)
            if air_gap_count >= 4:
                md_air_gap_4_height = float(self.md_air_gap_4_length_lineEdit.text())
                md_air_gap_4_position = float(self.md_air_gap_4_position_lineEdit.text())
                air_gap_heigth_array.append(md_air_gap_4_height)
                air_gap_position_array.append(md_air_gap_4_position)
                air_gap_position_tag_array.append(0)
            if air_gap_count >= 5:
                md_air_gap_5_height = float(self.md_air_gap_5_length_lineEdit.text())
                md_air_gap_5_position = float(self.md_air_gap_5_position_lineEdit.text())
                air_gap_heigth_array.append(md_air_gap_5_height)
                air_gap_position_array.append(md_air_gap_5_position)
                air_gap_position_tag_array.append(0)

            if air_gap_count == 0:
                geo.air_gaps.update(method="percent",
                                    n_air_gaps=0,
                                    air_gap_h=[],
                                    position_tag=[],
                                    air_gap_position=[])

            elif self.md_air_gap_placement_method_comboBox.currentText() == self.translation_dict["percent"] and air_gap_count >= 1:
                geo.air_gaps.update(method="percent",
                                    n_air_gaps=air_gap_count,
                                    air_gap_h=air_gap_heigth_array,
                                    position_tag=air_gap_position_tag_array,
                                    air_gap_position=air_gap_position_array)
            elif self.md_air_gap_placement_method_comboBox.currentText() == self.translation_dict["manually"] and air_gap_count >= 1:
                geo.air_gaps.update(method="manually",
                                    n_air_gaps=air_gap_count,
                                    air_gap_h=air_gap_heigth_array,
                                    position_tag=air_gap_position_tag_array,
                                    air_gap_position=air_gap_position_array)

            # -----------------------------------------------
            # Conductors
            # -----------------------------------------------

            if self.md_winding1_scheme_comboBox.currentText() == self.translation_dict["square"]:
                scheme = 'square'
            elif self.md_winding1_scheme_comboBox.currentText() == self.translation_dict["hexa"]:
                scheme = 'hexa'

            if self.md_winding1_type_comboBox.currentText() == self.translation_dict['solid']:
                self.md_simulation_QLabel.setText('setze conductors')
                geo.update_conductors(n_turns=[[int(self.md_winding1_turns_lineEdit.text())]],
                                      conductor_type=['solid'],
                                      conductor_radii=[float(self.md_winding1_radius_lineEdit.text())],
                                      winding=["primary"],
                                      scheme=[scheme],
                                      core_cond_isolation=[float(self.self.md_isolation_p2p_lineEdit.text())],
                                      cond_cond_isolation=[float(self.self.md_isolation_p2core_lineEdit.text())])
            elif self.md_winding1_type_comboBox.currentText() == self.translation_dict['litz']:
                litz_para_type = ''
                if self.md_winding1_implicit_litz_comboBox.currentText() == self.translation_dict['implicit_litz_radius']:
                    litz_para_type = "implicit_litz_radius"
                elif self.md_winding1_implicit_litz_comboBox.currentText() == self.translation_dict[
                    'implicit_ff']:
                    litz_para_type = 'implicit_ff'
                elif self.md_winding1_implicit_litz_comboBox.currentText() == self.translation_dict[
                    'implicit_strands_number']:
                    litz_para_type = 'implicit_strands_number'

                geo.update_conductors(n_turns=[[int(self.md_winding1_turns_lineEdit.text())]],
                                      conductor_type=['litz'],
                                      conductor_radii=[float(self.md_winding1_radius_lineEdit.text())],
                                      winding=["primary"],
                                      scheme=[scheme],
                                      litz_para_type=[litz_para_type],
                                      ff=[float(self.md_winding1_fill_factor_lineEdit.text())],
                                      strands_numbers=[float(self.md_winding1_strands_lineEdit.text())],
                                      strand_radii=[float(self.md_winding1_strand_radius_comboBox.text())],
                                      core_cond_isolation=[float(self.md_isolation_p2p_lineEdit.text())],
                                      cond_cond_isolation=[float(self.md_isolation_p2core_lineEdit.text())])

            # -----------------------------------------------
            # Simulation
            # -----------------------------------------------

            geo.single_simulation(freq=int(self.md_base_frequency_lineEdit.text()), current=[int(self.md_winding1_ik1_lineEdit.text())])

            # -----------------------------------------------
            # Read back results
            # -----------------------------------------------

            self.md_simulation_QLabel.setText('simulation fertig.')

            # log_path = geo.path + "/" + geo.path_res + 'result_log_electro_magnetic.json'
            # simulation_results = str(fmt.read_results_log(log_path))
            # print(simulation_results)
            # self.md_simulation_output_textBrowser.setText(simulation_results)

            #geo.core
            geo.visualize_geometry()
            #geo.onelab_client
            #gmsh.write('simulation.jpg')


        elif self.md_simulation_type_comboBox.currentText() == 'transformer':
            pass

        elif self.md_simulation_type_comboBox.currentText() == 'integrated transformer':
            pass


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if isinstance(child, QtWidgets.QSpacerItem):
            layout.removeItem(child)   # for spacer item
        elif child.widget() or child:   # child for comboBoxType and child.widget() for custom class types
            child.widget().deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainWindow()
    mainWindow.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window....')