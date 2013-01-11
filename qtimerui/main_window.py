# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtimerui/main_window.ui'
#
# Created: Wed Jan  9 20:23:40 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(1006, 606)
        self.centralwidget = QtGui.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_from_label = QtGui.QCheckBox(self.centralwidget)
        self.date_from_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.date_from_label.setObjectName("date_from_label")
        self.horizontalLayout.addWidget(self.date_from_label)
        self.date_from = QtGui.QDateEdit(self.centralwidget)
        self.date_from.setCalendarPopup(True)
        self.date_from.setObjectName("date_from")
        self.horizontalLayout.addWidget(self.date_from)
        self.date_to_label = QtGui.QCheckBox(self.centralwidget)
        self.date_to_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.date_to_label.setObjectName("date_to_label")
        self.horizontalLayout.addWidget(self.date_to_label)
        self.date_to = QtGui.QDateEdit(self.centralwidget)
        self.date_to.setCalendarPopup(True)
        self.date_to.setObjectName("date_to")
        self.horizontalLayout.addWidget(self.date_to)
        self.actions = QtGui.QPushButton(self.centralwidget)
        self.actions.setMaximumSize(QtCore.QSize(100, 16777215))
        self.actions.setObjectName("actions")
        self.horizontalLayout.addWidget(self.actions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(512, 192))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.projects = QtGui.QTreeWidget(self.splitter)
        self.projects.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.projects.setObjectName("projects")
        self.timers = QtGui.QTreeWidget(self.splitter)
        self.timers.setProperty("showDropIndicator", False)
        self.timers.setAlternatingRowColors(True)
        self.timers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.timers.setRootIsDecorated(False)
        self.timers.setUniformRowHeights(True)
        self.timers.setAllColumnsShowFocus(True)
        self.timers.setObjectName("timers")
        self.verticalLayout.addWidget(self.splitter)
        mainwindow.setCentralWidget(self.centralwidget)
        self.actionStart = QtGui.QAction(mainwindow)
        self.actionStart.setObjectName("actionStart")
        self.actionPause = QtGui.QAction(mainwindow)
        self.actionPause.setObjectName("actionPause")
        self.actionStop = QtGui.QAction(mainwindow)
        self.actionStop.setObjectName("actionStop")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QtGui.QApplication.translate("mainwindow", "qTimer v0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.date_from_label.setText(QtGui.QApplication.translate("mainwindow", "From", None, QtGui.QApplication.UnicodeUTF8))
        self.date_to_label.setText(QtGui.QApplication.translate("mainwindow", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.actions.setText(QtGui.QApplication.translate("mainwindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.projects.headerItem().setText(0, QtGui.QApplication.translate("mainwindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.timers.setSortingEnabled(True)
        self.timers.headerItem().setText(0, QtGui.QApplication.translate("mainwindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.timers.headerItem().setText(1, QtGui.QApplication.translate("mainwindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.timers.headerItem().setText(2, QtGui.QApplication.translate("mainwindow", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.timers.headerItem().setText(3, QtGui.QApplication.translate("mainwindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.timers.headerItem().setText(4, QtGui.QApplication.translate("mainwindow", "Synced", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("mainwindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setToolTip(QtGui.QApplication.translate("mainwindow", "Create a new timer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setShortcut(QtGui.QApplication.translate("mainwindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("mainwindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setToolTip(QtGui.QApplication.translate("mainwindow", "Pause a running timer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("mainwindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setToolTip(QtGui.QApplication.translate("mainwindow", "Stop a running timer (so it cannot be resumed later)", None, QtGui.QApplication.UnicodeUTF8))
