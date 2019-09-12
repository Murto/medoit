#!/usr/bin/env python

import datetime


class TODOItem:

  def __init__(self, description, deadline=None):
    self.description = description
    self.deadline = deadline


class TODO:

  def __init__(self, name, items=list()):
    self.name = name
    self.items = items

  def add(item):
    self.items.append(item)
  
  def remove(index):
    del self.items[index]


class TODOManager:
    
  def __init__(self, todos=set()):
    self.todos = todos

  def addTODO(self, todo):
    self.todos

  def removeTODO(self, todo):
    todo.remove(todo)