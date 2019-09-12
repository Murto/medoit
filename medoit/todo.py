#!/usr/bin/env python

from observe import Observable


class TODOItem:

  def __init__(self, description, deadline=None):
    self.description = description
    self.deadline = deadline

class TODO(Observable):

  def __init__(self, name, items=list(), observers=set()):
    super().__init__(observers)
    self.name = name
    self.items = items
    self.notify()

  def add(item):
    self.items.append(item)
    self.notify()
  
  def remove(index):
    del self.items[index]
    self.notify()


class TODOManager(Observable):
    
  def __init__(self, todos=dict(), observers=set()):
    super().__init__(observers)
    self.todos = todos
    self.notify()

  def get(self, name):
    return self.todos[name]

  def add(self, todo):
    if todo.name in self.todos:
      raise ValueError()
    self.todos[todo.name] = todo
    self.notify()

  def remove(self, name):
    del self.todos[name]
    self.notify()

  def rename(self, name, newName):
    if not name in self.todos:
      raise ValueError()
    if newName in self.todos:
      raise ValueError()
    self.todos[newName] = self.todos[name]
    del self.todos[name]
    self.notify()
