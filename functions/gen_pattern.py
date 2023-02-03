"""
Version: 0a
Tecnocoli - @07/2020
Author: Jeferson Coli - jcoli@tecnocoli.com.br
SPEED SENSOR SIMULATOR - camshafts and crankshafts - Arduino Uno/Nano
Function gen_pattern
"""

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

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
page = 0


def start_pat(input, teeth):
    if input.debug:
        logger.info('start pat')
    input.pattern_pt = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    input.pattern_p = ""
    input.line_gen_edges.setText(str(teeth))
    if len(input.line_gen_edges.text()) > 0 :
        input.edges = int(input.line_gen_edges.text())
        if int(input.edges/10) == (input.edges/10):
            input.max_pages = int(input.edges/10)
        else:
            input.max_pages = int(input.edges / 10)+1
        input.edges_last_page = input.edges-((input.max_pages-1)*10)
        if input.debug:
            input.append_text_ptd_datetime("edges changed: " + str(input.edges) + " - " + str(input.max_pages)
                                       + " - " + str(input.edges_last_page))
        input.btn_clear_pat.setEnabled(True)
        input.btn_gen_pat.setEnabled(True)
        # input.btn_prior_pat.setEnabled(True)
        input.btn_next_pat.setEnabled(True)
        input.line_gen_edges.setEnabled(False)
        input.page_pattern = 1
        input.lbl_pag.setText(str(input.page_pattern))
        input.textEdit_gen_pattern.setPlainText("")

        for x in range(0, 10):
            for i in range(1, 5):
                objectName = "cb" + str(x) + "0" + str(i)
                propertyName = "enabled"
                # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
                input.findChild(QObject, objectName).setProperty(propertyName, True)
                objectName = "cb" + str(x) + "1" + str(i)
                input.findChild(QObject, objectName).setProperty(propertyName, True)
        for i in range(1, 5):
            objectName = "cb" + "00" + str(i) + "_t"
            propertyName = "enabled"
            # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
            input.findChild(QObject, objectName).setProperty(propertyName, True)
            objectName = "cb" + "01" + str(i) + "_t"
            input.findChild(QObject, objectName).setProperty(propertyName, True)


def edit_pat(input, teeth, pattern):
    logger.info("edit pat: " + str(pattern) + " - " + str(len(pattern)) + " - " + str(teeth))
    input.pattern_pt = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    input.pattern_p = ""
    input.line_gen_edges.setText(str(teeth))
    if len(input.line_gen_edges.text()) > 0 :
        input.edges = int(input.line_gen_edges.text())
        if int(input.edges/10) == (input.edges/10):
            input.max_pages = int(input.edges/10)
        else:
            input.max_pages = int(input.edges / 10)+1
        input.edges_last_page = input.edges-((input.max_pages-1)*10)
        # logger.info("edit pat 2: " + str(input.max_pages))
        pattern_temp = (pattern.split(","))
        pattern_temp2 = " "
        for i in range(0, len(pattern_temp) - 1):
            pattern_temp2 = pattern_temp2 + (pattern_temp[i]) + ","
            # if input.debug:
            #     logger.info("gen_pattern_pt 1 " + str(pattern_temp[i]))
            #     logger.info("gen_pattern_pt 2 " + str(pattern_temp2))
        for i in range(1, input.max_pages + 1):
            # if input.debug:
            b = int(i * 40)
            a = b - 40 + 1
            # logger.info("gen_pattern_pt 3 " + str(i) + " -a:" + str(a) + " -b:" + str(b))
            input.pattern_p = pattern_temp2[a:b]
            # logger.info("gen_pattern_pt 4 " + str(input.pattern_p))
            input.pattern_pt[i - 1] = input.pattern_p
            # logger.info("gen_pattern_pt 4 " + str(input.pattern_p))
            # logger.info("gen_pattern_pt 5 " + str(input.pattern_pt))
            # logger.info("gen_pattern_pt 6 " + str(input.input.pattern_pt[i - 1]))

        # if input.debug:
        #     logger.info("edges changed: " + str(input.edges) + " - " + str(input.max_pages)
        #                                + " - " + str(input.edges_last_page))
        for i in range(1, 5):
            objectName = "cb" + "00" + str(i) + "_t"
            propertyName = "enabled"
            # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
            input.findChild(QObject, objectName).setProperty(propertyName, True)
            objectName = "cb" + "01" + str(i) + "_t"
            input.findChild(QObject, objectName).setProperty(propertyName, True)

        # input.btn_clear_pat.setEnabled(True)
        input.btn_gen_pat.setEnabled(True)
        # input.btn_prior_pat.setEnabled(True)
        input.btn_next_pat.setEnabled(True)
        input.line_gen_edges.setEnabled(False)
        input.page_pattern = 1
        input.lbl_pag.setText(str(input.page_pattern))
        input.textEdit_gen_pattern.setPlainText(str(pattern))
        # if input.debug:
        #     logger.info("=================================")
        #     logger.info("PATTERN: " + (str(pattern)))
        page_control_prior(input)


def clean_pat(input):
    input.max_pages = 1
    input.pattern_pt = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    input.pattern_p = ""
    input.textEdit_gen_pattern.setPlainText("")
    input.btn_clear_pat.setEnabled(False)
    input.btn_gen_pat.setEnabled(False)
    input.btn_prior_pat.setEnabled(False)
    input.btn_next_pat.setEnabled(False)
    input.line_gen_edges.setEnabled(True)

    for x in range(0, 10):
        for i in range(1, 5):
            objectName = "cb" + str(x) + "0" + str(i)
            propertyName = "enabled"
            # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
            input.findChild(QObject, objectName).setProperty(propertyName, False)
            objectName = "cb" + str(x) + "1" + str(i)
            input.findChild(QObject, objectName).setProperty(propertyName, False)
    for i in range(1, 5):
        objectName = "cb" + "00" + str(i) + "_t"
        propertyName = "enabled"
        # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
        input.findChild(QObject, objectName).setProperty(propertyName, False)
        objectName = "cb" + "01" + str(i) + "_t"
        input.findChild(QObject, objectName).setProperty(propertyName, False)
    clean_cb_pat(input)


def btn_gen_pattern(input):
    pattern = gen_pattern(input)
    input.pattern_pt[input.page_pattern - 1] = pattern;
    if input.debug:
        logger.info("gen_pattern_pt btn")
    gen_pattern_pt(input)
    input.tab_bar.setTabEnabled(1, True)
    input.tab_bar.setTabEnabled(2, False)
    input.tab_bar.setCurrentIndex(1)


def btn_next(input):
    pattern = gen_pattern(input)
    input.pattern_pt[input.page_pattern - 1] = pattern;
    if input.page_pattern < input.max_pages:
        input.page_pattern = input.page_pattern + 1
        input.lbl_pag.setText(str(input.page_pattern))
        page_control_next(input)
    if input.page_pattern == input.max_pages:
        input.btn_next_pat.setEnabled(False)
    input.btn_prior_pat.setEnabled(True)
    gen_pattern_pt(input)
    input.pattern_p = ""


def btn_prior(input):
    pattern = gen_pattern(input)
    input.append_text_ptd_datetime("prior button " + pattern)
    input.pattern_pt[input.page_pattern - 1] = pattern
    if input.page_pattern > 1:
        input.page_pattern = input.page_pattern - 1
        input.lbl_pag.setText(str(input.page_pattern))
        page_control_prior(input)
    if input.page_pattern == 1:
        input.btn_prior_pat.setEnabled(False)
    input.btn_next_pat.setEnabled(True)
    gen_pattern_pt(input)
    input.pattern_p = ""


def gen_pattern(input):
    if input.debug:
        logger.info("gen_pattern")
    input.pattern_p = ""
    if input.page_pattern == input.max_pages:
        for x in range(0, input.edges_last_page):
            edge0 = 0
            edge1 = 0
            for i in range(1 , 5):
                objectName = "cb" + str(x) + "0" + str(i)
                propertyName = "checked"
                cbCheck = bool(input.findChild(QObject, objectName).property(propertyName))
                if cbCheck:
                    edge0 = edge0 + (2 ** (i - 1))
                objectName = "cb" + str(x) + "1" + str(i)
                cbCheck = bool(input.findChild(QObject, objectName).property(propertyName))
                if cbCheck:
                    edge1 = edge1 + (2 ** (i - 1))
            input.pattern_p = input.pattern_p + str(edge0) + ","
            input.pattern_p = input.pattern_p + str(edge1) + ","
            if input.debug:
                logger.info(input.pattern_p)
            # input.textEdit_gen_pattern.setPlainText(input.textEdit_gen_pattern.toPlainText() + str(edge0) + ",")
            # input.textEdit_gen_pattern.setPlainText(input.textEdit_gen_pattern.toPlainText() + str(edge1) + ",")
    else:
        for x in range(0, 10):
            edge0 = 0
            edge1 = 0
            for i in range(1, 5):
                objectName = "cb" + str(x) + "0" + str(i)
                propertyName = "checked"
                cbCheck = bool(input.findChild(QObject, objectName).property(propertyName))
                if cbCheck:
                    edge0 = edge0 + (2 ** (i - 1))
                objectName = "cb" + str(x) + "1" + str(i)
                cbCheck = bool(input.findChild(QObject, objectName).property(propertyName))
                if cbCheck:
                    edge1 = edge1 + (2 ** (i - 1))
            input.pattern_p = input.pattern_p + str(edge0) + ","
            input.pattern_p = input.pattern_p + str(edge1) + ","

    return input.pattern_p


def page_control_next(input):
    pattern = (input.pattern_pt[input.page_pattern - 1]).split(",")
    if input.debug:
        logger.info("page control next: " + str(input.page_pattern) + " - " + str(len(pattern)) + " - "
                                   + input.pattern_pt[input.page_pattern - 1])
        logger.info("page control next: " + str(input.pattern_pt))
    for i in range(1, 5):
        propertyName = "checked"
        objectName1 = "cb" + "00" + str(i) + "_t"
        input.findChild(QObject, objectName1).setProperty(propertyName, False)
        objectName1 = "cb" + "01" + str(i) + "_t"
        input.findChild(QObject, objectName1).setProperty(propertyName, False)

    if input.page_pattern == input.max_pages:
        for x in range(input.edges_last_page, 10):
            for i in range(1, 5):
                objectName = "cb" + str(x) + "0" + str(i)
                propertyName = "enabled"
                # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
                input.findChild(QObject, objectName).setProperty(propertyName, False)
                objectName = "cb" + str(x) + "1" + str(i)
                input.findChild(QObject, objectName).setProperty(propertyName, False)

        for x in range(0, input.edges_last_page):
            if len(pattern) > 1:
                edge0 = pattern[x * 2];
                edge1 = pattern[(x * 2) + 1];
            else:
                edge0 = "0"
                edge1 = "0"
            for i in range(1, 5):
                bin_mask = 2 ** (i - 1)

                cb_check_0 = bin_mask & int(edge0)
                cb_check_1 = bin_mask & int(edge1)
                objectName = "cb" + str(x) + "0" + str(i)
                propertyName = "enabled"
                # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
                input.findChild(QObject, objectName).setProperty(propertyName, True)
                propertyName = "checked"
                if cb_check_0 > 0:
                    input.findChild(QObject, objectName).setProperty(propertyName, True)
                else:
                    input.findChild(QObject, objectName).setProperty(propertyName, False)
                objectName = "cb" + str(x) + "1" + str(i)
                propertyName = "enabled"
                input.findChild(QObject, objectName).setProperty(propertyName, True)
                propertyName = "checked"
                if cb_check_1 > 0:
                    input.findChild(QObject, objectName).setProperty(propertyName, True)
                else:
                    input.findChild(QObject, objectName).setProperty(propertyName, False)
                if input.debug:
                    logger.info("page control next: " + str(x) + " - " + str(i) + " - " + edge0 + " - "
                                               + edge1 + " - " + str(bin_mask) + " - " + str(cb_check_0)
                                               + " - " + str(cb_check_1))
    else:
        for x in range(0, 10):
            if len(pattern) > 1:
                edge0 = pattern[x * 2];
                edge1 = pattern[(x * 2) + 1];
            else:
                edge0 = "0"
                edge1 = "0"
            for i in range(1, 5):
                bin_mask = 2 ** (i - 1)
                cb_check_0 = bin_mask & int(edge0)
                cb_check_1 = bin_mask & int(edge1)
                objectName = "cb" + str(x) + "0" + str(i)
                propertyName = "enabled"
                # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
                input.findChild(QObject, objectName).setProperty(propertyName, True)
                propertyName = "checked"
                if cb_check_0 > 0:
                    input.findChild(QObject, objectName).setProperty(propertyName, True)
                else:
                    input.findChild(QObject, objectName).setProperty(propertyName, False)
                objectName = "cb" + str(x) + "1" + str(i)
                propertyName = "enabled"
                input.findChild(QObject, objectName).setProperty(propertyName, True)
                propertyName = "checked"
                if cb_check_1 > 0:
                    input.findChild(QObject, objectName).setProperty(propertyName, True)
                else:
                    input.findChild(QObject, objectName).setProperty(propertyName, False)
                if input.debug:
                    if input.debug:
                        logger.info("page control next: " + str(x) + " - " + str(i) + " - " + edge0 + " - "
                                               + edge1 + " - " + str(bin_mask) + " - " + str(cb_check_0)
                                               + " - " + str(cb_check_1))


def page_control_prior(input):
    pattern = (input.pattern_pt[input.page_pattern-1]).split(",")
    if input.debug:
        logger.info("page control prior: " + str(input.page_pattern) + " - " + str(len(pattern)) + " - "
                                   + input.pattern_pt[input.page_pattern-1])
    for i in range(1, 5):
        propertyName = "checked"
        objectName1 = "cb" + "00" + str(i) + "_t"
        input.findChild(QObject, objectName1).setProperty(propertyName, False)
        objectName1 = "cb" + "01" + str(i) + "_t"
        input.findChild(QObject, objectName1).setProperty(propertyName, False)
    for x in range(0, 10):
        edge0 = pattern[x * 2];
        edge1 = pattern[(x * 2) + 1];
        for i in range(1, 5):
            bin_mask = 2 ** (i-1)
            cb_check_0 = bin_mask & int(edge0)
            cb_check_1 = bin_mask & int(edge1)
            objectName = "cb" + str(x) + "0" + str(i)
            propertyName = "enabled"
            # input.append_text_ptd_datetime("Hide: " + str(x) + " - " + str(i))
            input.findChild(QObject, objectName).setProperty(propertyName, True)
            propertyName = "checked"
            if cb_check_0 > 0:
                input.findChild(QObject, objectName).setProperty(propertyName, True)
            else:
                input.findChild(QObject, objectName).setProperty(propertyName, False)
            objectName = "cb" + str(x) + "1" + str(i)
            propertyName = "enabled"
            input.findChild(QObject, objectName).setProperty(propertyName, True)
            propertyName = "checked"
            if cb_check_1 > 0:
                input.findChild(QObject, objectName).setProperty(propertyName, True)
            else:
                input.findChild(QObject, objectName).setProperty(propertyName, False)
            if input.debug:
                input.append_text_ptd_datetime("page control prior: " + str(x) + " - " + str(i) + " - " + edge0 + " - "
                                           + edge1 + " - " + str(bin_mask) + " - " + str(cb_check_0)
                                           + " - " + str(cb_check_1))


def gen_pattern_pt(input):
    if input.debug:
        logger.info("gen_pattern_pt")
        # logger.info('gen_pattern_pt pages' + str(input.max_pages))
    input.textEdit_gen_pattern.setPlainText("")
    for i in range(0, input.max_pages):
        logger.info('gen_pattern_pt ' + str(input.max_pages) + " - " + str(i) + " - " + input.pattern_pt[i])
        last_char = str(input.pattern_pt[i])[-1]
        logger.info('gen_pattern_pt 1 ' + last_char)
        if ',' in last_char:
            logger.info('gen_pattern_pt 1a has ,')
        else:
            input.pattern_pt[i] = input.pattern_pt[i] + ','
        input.textEdit_gen_pattern.setPlainText(input.textEdit_gen_pattern.toPlainText()+input.pattern_pt[i])
        logger.info('gen_pattern_pt 2 ' + input.textEdit_gen_pattern.toPlainText())
        # input.append_text_ptd_datetime("gen_pattern_pt " + str(i))
    input.textEdit_pattern.setPlainText(input.textEdit_gen_pattern.toPlainText())
    input.pattern = input.textEdit_gen_pattern.toPlainText()
    logger.info('=======================================')
    logger.info('gen_pattern_pt PATTERN ' + str(input.pattern))






def clean_cb_pat(input):
    if input.debug:
        logger.info("clear cb pattern")
    # if (page == 0):
    for x in range(0, 10):
        edge0 = 0;
        edge1 = 0;
        for i in range(1, 5):
            objectName = "cb" + str(x) + "0" + str(i)
            propertyName = "checked"
            input.findChild(QObject, objectName).setProperty(propertyName, False)
            objectName = "cb" + str(x) + "1" + str(i)
            input.findChild(QObject, objectName).setProperty(propertyName, False)
            objectName1 = "cb" + "00" + str(i) + "_t"
            input.findChild(QObject, objectName1).setProperty(propertyName, False)
            objectName1 = "cb" + "01" + str(i) + "_t"
            input.findChild(QObject, objectName1).setProperty(propertyName, False)


def line_gen_edges_changed_pat(input):
    if input.debug:
        input.append_text_ptd_datetime("edges changed: ")


def cb000_t_clicked(input, edge, i):
    if input.debug:
        input.append_text_ptd_datetime("cb000_clicked: " + str(i) + " - " + str(edge))

    if edge == 0:
        if input.debug:
            input.append_text_ptd_datetime("cb000_clicked:  edge 0")
        objectName1 = "cb" + "00" + str(i) + "_t"
        propertyName = "checked"
        cbCheck = bool(input.findChild(QObject, objectName1).property(propertyName))

        for x in range(0, 10):
            objectName = "cb" + str(x) + "0" + str(i)
            propertyName = "checked"
            if cbCheck:
                input.findChild(QObject, objectName).setProperty(propertyName, True)
            else:
                input.findChild(QObject, objectName).setProperty(propertyName, False)

    if edge == 1:
        if input.debug:
            input.append_text_ptd_datetime("cb000_clicked:  edge 1")
        objectName1 = "cb" + "01" + str(i) + "_t"
        propertyName = "checked"
        cbCheck = bool(input.findChild(QObject, objectName1).property(propertyName))

        for x in range(0, 10):
            objectName = "cb" + str(x) + "1" + str(i)
            propertyName = "checked"
            if cbCheck:
                input.findChild(QObject, objectName).setProperty(propertyName, True)
            else:
                input.findChild(QObject, objectName).setProperty(propertyName, False)

