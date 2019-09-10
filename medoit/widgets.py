#!/usr/bin/env python

from PyQt5.QtWidgets import QBoxLayout, QLabel, QListWidget, QPushButton, QWidget
from PyQt5.QtCore import Qt


class ManageTODOs(QWidget):

  def __init__(self):
    super().__init__()
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

  def setNewCallback(self, callback):
    self.new.clicked.connect(callback)

  def setViewCallback(self, callback):
    self.view.clicked.connect(callback)

  def setRenameCallback(self, callback):
    self.rename.clicked.connect(callback)

  def setDeleteCallback(self, callback):
    self.delete.clicked.connect(callback)
