#!/usr/bin/env python


class Observable:

  def __init__(self, observers=set()):
    self.observers = observers

  def attach(self, observer):
    self.observers.add(observers)

  def detach(self, observer):
    self.observers.remove(observer)

  def notify(self):
    for observer in self.observers:
      observer()


class Observer:

  def __init__(self, observer):
    observer.registerObserver(self)

  def notify(self):
    raise NotImplementedError()
