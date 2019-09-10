#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QWidget
import sys

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = QWidget()
  main.show()
  sys.exit(app.exec_())
