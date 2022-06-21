import pandas as pd

class User:
  """Serves as a person for tracking users"""
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def introduceSelf():
  """ Provides a general introduction
   :return: The person's introduction phrase
   :rtype: str
  """
    return 'My name is ' + self.name

  
  def addAge(years:int):
    return self.age +  years
