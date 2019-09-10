#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from widgets import ManageTODOs
import sys

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = ManageTODOs()
  main.show()
  sys.exit(app.exec_())
