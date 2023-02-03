"""
Version: 0a
Tecnocoli - @07/2020
Author: Jeferson Coli - jcoli@tecnocoli.com.br
SPEED SENSOR SIMULATOR - camshafts and crankshafts - Arduino Uno/Nano
Function db_controls
"""

from datetime import datetime
import time
from time import sleep
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QMessageBox
from functions.gen_pattern import start_pat, edit_pat

import logging
from serial.tools.list_ports import comports
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
text_date = datetime.now().strftime('%d-%m-%Y')
scanner_file = 'injector-' + text_date+'.log'
handler = logging.FileHandler(scanner_file)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def tableWheel_clicked_db(input):
    if input.debug:
        logger.info('tableWheel_clicked_db')

    record = input.modelWheel.record(input.tableWheel.currentIndex().row())
    input.lineEdit_name.setText(record.value("name"))
    input.lineEdit_scaler.setText(str(record.value("rpmScaler")))
    input.lineEdit_dentes.setText(str(record.value("teeth")))
    input.textEdit_pattern.setText(record.value("pattern"))
    input.pattern = record.value("pattern")
    # logger.info("edit pat: " + str(input.pattern) + " - " + str(len(input.pattern)))
    if record.value("revolution") == 1:
        input.rb_1rev.setChecked(True)
    else:
        input.rb_2rev.setChecked(True)
    input.lineEdit_desc_curta.setText(record.value("short_desc"))
    input.lineEdit_desc_longa.setText(record.value("long_desc"))
    input.lineEdit_edges.setText(str(record.value("edges")))
    input.append_text_ptd_datetime("new: " + record.value("name"))



def btnw_insert(input):
    input.btnw_cancel.setEnabled(True)
    input.btnw_update.setEnabled(False)
    input.btnw_delete.setEnabled(True)
    input.btnw_new.setEnabled(True)
    input.btnw_Insert.setEnabled(False)
    input.btnw_edit.setEnabled(True)
    input.tableWheel.setEnabled(True)
    input.btn_cp_pattern.setEnabled(True)
    try:
        input.append_text_ptd_datetime("insert")
        query = QSqlQuery()
        query.prepare("INSERT INTO WheelPattern (name, pattern, edges, rpmscaler, short_desc, long_desc, teeth, revolution ) "
                      "VALUES (:name, :pattern, :edges, :rpmscaler, :short_desc, :long_desc, :teeth, :revolution)")

        # ("UPDATE WheelPattern SET name = :name, pattern = :pattern, teeth = :teeth, rpmscaler = :rpmscaler,"
        #  " short_desc = :short_desc, long_desc = :long_desc,  edges = :edges, "
        #  " revolution = :revolution WHERE id = ") + str(prov_id));
        edges = 0
        rev = 0
        if input.rb_1rev.isChecked():
            edges = int(int(input.lineEdit_dentes.text()) * 1 * 2)
            logger.info("rb1 ")
            rev = 1
            logger.info(query.lastError())
        else:
            edges = int(int(input.lineEdit_dentes.text()) * 2 * 2)
            logger.info("rb2 ")
            rev = 2
            logger.info(query.lastError())
        rpm_scaller = float(float(input.lineEdit_dentes.text()) / 120.0)
        rpm_scaller = float("{:.2f}".format(rpm_scaller))
        query.bindValue(":name", input.lineEdit_name.text())
        query.bindValue(":short_desc", input.lineEdit_desc_curta.text())
        query.bindValue(":long_desc", input.lineEdit_desc_longa.text())
        query.bindValue(":teeth", int(input.lineEdit_dentes.text()))
        query.bindValue(":rpmscaler", rpm_scaller)
        query.bindValue(":edges", edges)
        query.bindValue(":revolution", rev)
        query.bindValue(":pattern", input.textEdit_pattern.toPlainText())
        query.exec_()
        input.lineEdit_name.setEnabled(False)
        input.lineEdit_dentes.setEnabled(False)
        input.textEdit_pattern.setEnabled(False)
        input.rb_1rev.setEnabled(False)
        input.rb_2rev.setEnabled(False)
        input.lineEdit_desc_curta.setEnabled(False)
        input.lineEdit_desc_longa.setEnabled(False)
        input.btn_cp_pattern.setEnabled(False)
        input.flag_new = False
        input.initializedModelWheel()
        input.initializedModelChoose()
        input.tab_bar.setTabEnabled(2, False)
        input.tab_bar.setTabEnabled(0, True)


    except Exception as e:
        logger.info("Error update " + str(e))
        # logger.info("Connected " + str(dig))


def btnw_edit(input):
    input.btnw_cancel.setEnabled(True)
    input.btnw_update.setEnabled(True)
    input.btnw_delete.setEnabled(False)
    input.btnw_new.setEnabled(False)
    input.btnw_Insert.setEnabled(False)
    input.btnw_edit.setEnabled(False)
    input.tableWheel.setEnabled(False)
    input.btn_cp_pattern.setEnabled(True)
    input.append_text_ptd_datetime("edit")
    input.lineEdit_name.setEnabled(True)
    input.lineEdit_dentes.setEnabled(True)
    input.rb_1rev.setEnabled(True)
    input.rb_2rev.setEnabled(True)
    input.lineEdit_desc_curta.setEnabled(True)
    input.lineEdit_desc_longa.setEnabled(True)
    input.tab_bar.setTabEnabled(0, False)
    input.tab_bar.setTabEnabled(2, False)



def cp_pattern(input):
    input.rb_1rev.setEnabled(False)
    input.rb_2rev.setEnabled(False)
    input.lineEdit_dentes.setEnabled(False)
    teeth = int(input.lineEdit_dentes.text())
    if input.flag_new:
        start_pat(input, teeth)
    else:
        edit_pat(input, teeth, input.pattern)
    input.tab_bar.setTabEnabled(3, False)
    input.tab_bar.setTabEnabled(1, False)
    input.tab_bar.setTabEnabled(2, True)
    # input.btn_cp_pattern.setEnabled(False)
    # input.setTabEnabled(3, False)
    input.tab_bar.setCurrentIndex(2)
    if input.debug:
        logger.info('cp_pattern')


    # input.textEdit_pattern.setText(input.textEdit_gen_pattern.toPlainText())


def btnw_update(input):
    input.btnw_cancel.setEnabled(True)
    input.btnw_update.setEnabled(False)
    input.btnw_delete.setEnabled(True)
    input.btnw_new.setEnabled(True)
    input.btnw_Insert.setEnabled(False)
    input.btnw_edit.setEnabled(True)
    input.tableWheel.setEnabled(True)

    try:
        if input.debug:
            logger.info('update')
        record = input.modelWheel.record(input.tableWheel.currentIndex().row())
        prov_id = int(record.value("id"))
        input.append_text_ptd_datetime\
            ("update: " + str(record.value("id")))
        query = QSqlQuery()
        if input.debug:
            logger.info('update 1')
        # query.prepare("UPDATE WheelPattern SET name = :name, pattern = :pattern,"
        #               " edges = :edges, rpmscaller = :rpmscaller WHERE id = :id ");
        #query.prepare(("UPDATE WheelPattern SET name = :name, pattern = :pattern, edges = :edges WHERE id = ") + str(prov_id));
        query.prepare(
            ("UPDATE WheelPattern SET name = :name, pattern = :pattern, teeth = :teeth, rpmscaler = :rpmscaler,"
             " short_desc = :short_desc, long_desc = :long_desc,  edges = :edges, "
             " revolution = :revolution WHERE id = ") + str(prov_id));
        edges = 0
        rev = 0
        if input.rb_1rev.isChecked():
            edges = int(int(input.lineEdit_dentes.text()) * 1 * 2)
            logger.info("rb1 ")
            rev = 1
            logger.info(query.lastError())
        else:
            edges = int(int(input.lineEdit_dentes.text()) * 2 * 2)
            logger.info("rb2 ")
            rev = 2
            logger.info(query.lastError())
        rpm_scaller = float(float(input.lineEdit_dentes.text())/120.0)
        rpm_scaller = float("{:.2f}".format(rpm_scaller))
        query.bindValue(":name", input.lineEdit_name.text())
        query.bindValue(":short_desc", input.lineEdit_desc_curta.text())
        query.bindValue(":long_desc", input.lineEdit_desc_longa.text())
        query.bindValue(":teeth", int(input.lineEdit_dentes.text()))
        query.bindValue(":rpmscaler", rpm_scaller)
        query.bindValue(":edges", edges)
        query.bindValue(":revolution", rev)
        query.bindValue(":pattern", input.textEdit_pattern.toPlainText())

        if input.debug:
            logger.info('update 2')
            logger.info('update 2 :' + str(rpm_scaller) + " - " + str(edges))
            logger.info(query.lastError())
        # query.bindValue(":id ", prov_id)
        query.exec_()
        if input.debug:
            logger.info("update "+str(record.value("id"))+ " - " + str(prov_id))
            logger.info(query.lastError())
        input.tableWheel.update()
        if input.debug:
            logger.info("update "+str(record.value("id"))+ " - " + str(prov_id))
            logger.info(query.lastError())
        input.lineEdit_name.setEnabled(False)
        input.lineEdit_dentes.setEnabled(False)
        input.textEdit_pattern.setEnabled(False)
        input.rb_1rev.setEnabled(False)
        input.rb_2rev.setEnabled(False)
        input.lineEdit_desc_curta.setEnabled(False)
        input.lineEdit_desc_longa.setEnabled(False)
        input.btn_cp_pattern.setEnabled(False)
        input.initializedModelWheel()
        input.initializedModelChoose()
        input.tab_bar.setTabEnabled(0, True)
        if input.debug:
            logger.info("update finish")
    except Exception as e:
        logger.info("Error update " + str(e))
        # logger.info("Connected " + str(dig))


def tableChoose_clicked_db(input):

    if input.debug:
        logger.info('tableWheel_clicked_db')
        input.append_text_ptd_datetime("tableChoose_clicked_db")
    record = input.modelChoose.record(input.tableWheel.currentIndex().row())

def btnw_cancel(input):
    input.btnw_cancel.setEnabled(True)
    input.btnw_update.setEnabled(False)
    input.btnw_delete.setEnabled(True)
    input.btnw_new.setEnabled(True)
    input.btnw_Insert.setEnabled(False)
    input.btnw_edit.setEnabled(True)
    input.tableWheel.setEnabled(True)
    input.btn_cp_pattern.setEnabled(False)
    
    input.lineEdit_name.setEnabled(False)
    input.lineEdit_dentes.setEnabled(False)
    input.textEdit_pattern.setEnabled(False)
    input.rb_1rev.setEnabled(False)
    input.rb_2rev.setEnabled(False)
    input.lineEdit_desc_curta.setEnabled(False)
    input.lineEdit_desc_longa.setEnabled(False)
    input.btn_cp_pattern.setEnabled(False)
    input.flag_new = False
    input.initializedModelWheel()
    input.initializedModelChoose()
    input.tab_bar.setTabEnabled(0, True)


def btnw_delete(input):
    if input.debug:
        logger.info("delete db")
    delete_msg_box = QMessageBox.question(input, 'Window Close', 'Tem certeza que deseja apagar esse padrão?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    # quit_msg_box = QMessageBox()
    # quit_msg_box.setText("Tem certeza que deseja fechar o aplicativo?")
    # quit_msg_box.addButton(QtWidgets.QStandardButton("Sim"), QtWidgets.QMessageBox.Yes)
    # quit_msg_box.addButton(QtWidgets.QPushButton("Não"), QtGui.QMessageBox.No)
    #
    # QMessageBox.Yes.setText("Sim")

    reply = delete_msg_box

    if reply == QMessageBox.Yes:
        try:
            record = input.modelWheel.record(input.tableWheel.currentIndex().row())
            prov_id = int(record.value("id"))
            query = QSqlQuery()
            query.prepare(
                ("delete from WheelPattern WHERE id = ") + str(prov_id));
            query.exec_()
        except Exception as e:
            logger.info("Error delete " + str(e))
            # logger.info("Connected " + str(dig))

        input.initializedModelWheel()
        input.initializedModelChoose()


def btnw_new(input):
    input.btnw_cancel.setEnabled(True)
    input.btnw_update.setEnabled(False)
    input.btnw_delete.setEnabled(False)
    input.btnw_new.setEnabled(False)
    input.btnw_edit.setEnabled(False)
    input.btnw_Insert.setEnabled(True)
    input.tableWheel.setEnabled(False)
    input.btn_cp_pattern.setEnabled(True)
    input.append_text_ptd_datetime("new")
    input.lineEdit_name.setText("")
    input.lineEdit_dentes.setText("")
    input.textEdit_pattern.setText("")
    input.lineEdit_desc_curta.setText("")
    input.lineEdit_desc_longa.setText("")
    input.lineEdit_name.setEnabled(True)
    input.lineEdit_dentes.setEnabled(True)
    input.rb_1rev.setEnabled(True)
    input.rb_2rev.setEnabled(True)
    input.lineEdit_desc_curta.setEnabled(True)
    input.lineEdit_desc_longa.setEnabled(True)
    input.flag_new = True
    input.tab_bar.setTabEnabled(0, False)


def teeth_changed(input):
    if input.rb_1rev.isChecked():
        edges = int(int(input.lineEdit_dentes.text()) * 1 * 2)
    else:
        edges = int(int(input.lineEdit_dentes.text()) * 2 * 2)
    rpm_scaller = float(float(input.lineEdit_dentes.text()) / 120.0)
    rpm_scaller = float("{:.2f}".format(rpm_scaller))
    input.lineEdit_scaler.setText(str(rpm_scaller))
    input.lineEdit_edges.setText(str(edges))




