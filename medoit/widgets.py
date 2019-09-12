#!/usr/bin/env python

from PyQt5.QtWidgets import QBoxLayout, QDialog, QLabel, QLineEdit, QListWidget, QPushButton, QWidget
from PyQt5.QtCore import Qt


class ManageTODOs(QWidget):

  def __init__(self, manager):
    super().__init__()
    self.manager = manager
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.todos = QListWidget()
    self.new = QPushButton('New')
    self.view = QPushButton('View')
    self.rename = QPushButton('Rename')
    self.delete = QPushButton('Delete')
    layout.addWidget(self.todos, alignment=Qt.AlignCenter)
    layout.addWidget(self.new, alignment=Qt.AlignCenter)
    layout.addWidget(self.view, alignment=Qt.AlignCenter)
    layout.addWidget(self.rename, alignment=Qt.AlignCenter)
    layout.addWidget(self.delete, alignment=Qt.AlignCenter)
    self.setLayout(layout)
    self.manager.attach(self.update)
    self.update()

  def update(self):
    self.todos.clear()
    print([todo.name for todo in self.manager.todos])
    self.todos.addItems([todo.name for todo in self.manager.todos])

  def setNewCallback(self, callback):
    self.new.clicked.connect(callback)

  def setViewCallback(self, callback):
    self.view.clicked.connect(callback)

  def setRenameCallback(self, callback):
    self.rename.clicked.connect(callback)

  def setDeleteCallback(self, callback):
    self.delete.clicked.connect(callback)


class NewTODODialog(QDialog):

  def __init__(self):
    super().__init__()
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.instructions = QLabel('Enter a name for your new TODO list:')
    self.name = QLineEdit()
    self.ok = QPushButton('OK')
    self.cancel = QPushButton('Cancel')
    layout.addWidget(self.instructions, alignment=Qt.AlignCenter)
    layout.addWidget(self.name, alignment=Qt.AlignCenter)
    layout.addWidget(self.ok, alignment=Qt.AlignCenter)
    layout.addWidget(self.cancel, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def setOKCallback(self, callback):
    self.ok.clicked.connect(lambda: callback(self.name.text()))

  def setCancelCallback(self, callback):
    self.cancel.clicked.connect(callback)
