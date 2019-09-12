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
    
  def __init__(self, todos=set(), observers=set()):
    super().__init__(observers)
    self.todos = todos
    self.notify()

  def add(self, todo):
    self.todos.add(todo)
    self.notify()

  def remove(self, todo):
    self.todos.remove(todo)
    self.notify()
