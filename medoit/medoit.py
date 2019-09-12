#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from todo import TODOManager, TODO
from widgets import ManageTODOs, NewTODODialog
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

if __name__ == '__main__':
  manager = TODOManager()
  app = QApplication(sys.argv)
  main = ManageTODOs(manager)
  def newTODODialogCallback():
    createNewTODODialog(manager)
  main.setNewCallback(lambda: createNewTODODialog(manager))
  main.show()
  sys.exit(app.exec_())
