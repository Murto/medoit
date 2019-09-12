#!/usr/bin/env python

from PyQt5.QtWidgets import QBoxLayout, QDialog, QLabel, QLineEdit, QListWidget, QPushButton, QStackedWidget, QWidget
from PyQt5.QtCore import Qt


class ManageTODOs(QWidget):

  def __init__(self):
    super().__init__()
    self.todos = QListWidget()
    self.new = QPushButton('New')
    self.view = QPushButton('View')
    self.rename = QPushButton('Rename')
    self.delete = QPushButton('Delete')
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    layout.addWidget(self.todos, alignment=Qt.AlignCenter)
    layout.addWidget(self.new, alignment=Qt.AlignCenter)
    layout.addWidget(self.view, alignment=Qt.AlignCenter)
    layout.addWidget(self.rename, alignment=Qt.AlignCenter)
    layout.addWidget(self.delete, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def update(self, manager):
    self.todos.clear()
    self.todos.addItems([todo.name for todo in manager.todos])

  def setNewCallback(self, callback):
    self.new.clicked.connect(callback)

  def setViewCallback(self, callback):
    self.view.clicked.connect(lambda: callback(self.todos.currentItem()))

  def setRenameCallback(self, callback):
    self.rename.clicked.connect(lambda: callback(self.todos.currentItem()))

  def setDeleteCallback(self, callback):
    self.delete.clicked.connect(lambda: callback(self.todos.currentItem()))


class ViewTODO(QWidget):

  def __init__(self):
    super().__init__()
    self.title = QLabel('TODO')
    self.items = QListWidget()
    self.add = QPushButton('Add')
    self.remove = QPushButton('Remove')
    self.back = QPushButton('Back')
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    layout.addWidget(self.title, alignment=Qt.AlignCenter)
    layout.addWidget(self.items, alignment=Qt.AlignCenter)
    layout.addWidget(self.add, alignment=Qt.AlignCenter)
    layout.addWidget(self.remove, alignment=Qt.AlignCenter)
    layout.addWidget(self.back, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def update(self, todo):
    self.items.clear()
    self.items.addItems([item.description for item in todo.items])

  def setAddCallback(self, callback):
    self.add.clicked.connect(callback)

  def setRemoveCallback(self, callback):
    self.remove.clicked.connect(lambda: callback(self.items.currentItem()))
  
  def setBackCallback(self, callback):
    self.back.clicked.connect(callback)
