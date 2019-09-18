#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QMessageBox, QStackedWidget
from PyQt5.QtCore import Qt
from todo import TODOManager, TODO
from widgets import ManageTODOs, ViewTODO
import sys


def initUI(manager):
  # Create application
  app = QApplication(sys.argv)

  # Create all widgets
  manage = ManageTODOs()
  main = QStackedWidget()

  # Add widgets to main widget
  main.addWidget(manage)

  # Create callbacks for the widgets
  def newTODO():
    name, ok = QInputDialog.getText(main, 'New TODO', 'Enter the name of your new TODO:')
    if ok:
      try:
        manager.add(TODO(name))
      except ValueError:
        message = QMessageBox(parent=main)
        message.setIcon(QMessageBox.Warning)
        message.setText('A TODO with that name already exists')
        message.setWindowTitle('Warning')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()

  def renameTODO(name):
    if name is None:
      message = QMessageBox(parent=main)
      message.setIcon(QMessageBox.Warning)
      message.setText('You must select a TODO to rename.')
      message.setWindowTitle('Warning')
      message.setStandardButtons(QMessageBox.Ok)
      message.exec_()
    else:
      newName, ok = QInputDialog.getText(main, 'Rename TODO', 'Enter the new name of your TODO:')
      if ok:
        try:
          manager.rename(name, newName)
        except ValueError:
          message = QMessageBox(parent=main)
          message.setIcon(QMessageBox.Warning)
          message.setText('A TODO with that name already exists.')
          message.setWindowTitle('Warning')
          message.setStandardButtons(QMessageBox.Ok)
          message.exec_()

  def viewTODO(name):
    if name is None:
      message = QMessageBox(parent=main)
      message.setIcon(QMessageBox.Warning)
      message.setText('You must select a TODO to view.')
      message.setWindowTitle('Warning')
      message.setStandardButtons(QMessageBox.Ok)
      message.exec_()
    else:
      view = ViewTODO(name)



  def deleteTODO(name):
    if name is None:
      message = QMessageBox(parent=main)
      message.setIcon(QMessageBox.Warning)
      message.setText('You must select a TODO to delete.')
      message.setWindowTitle('Warning')
      message.setStandardButtons(QMessageBox.Ok)
      message.exec_()
    else:
      manager.remove(name)
      


  # Set callbacks for the widgets
  manage.setNewCallback(newTODO)
  manage.setRenameCallback(renameTODO)
  manage.setViewCallback(viewTODO)
  manage.setDeleteCallback(deleteTODO)

  # Set callbacks for the TODOManager
  manager.attach(lambda: manage.update(manager))

  # Show main widget
  main.show()
  
  # Run the program until it is exited
  sys.exit(app.exec_())

if __name__ == '__main__':
  manager = TODOManager()
  initUI(manager)
