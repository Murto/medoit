#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtCore import Qt
from todo import TODOManager, TODO
from widgets import ManageTODOs, NewTODODialog, ViewTODO
import sys


def createNewTODODialog(manager):
  dialog = NewTODODialog()
  def okCallback(name):
    if not any(name == todo.name for todo in manager.todos):
      manager.add(TODO(name))
      dialog.close()
  dialog.setOKCallback(okCallback)
  dialog.setCancelCallback(dialog.close)
  dialog.exec_()

def initUI(manager):
  app = QApplication(sys.argv)
  manage = ManageTODOs()
  main = QStackedWidget()
  main.addWidget(manage)
  main.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  manager = TODOManager()
  initUI(manager)
