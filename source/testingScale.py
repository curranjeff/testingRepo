import pandas as pd

class User:
  """Serves as an object for tracking users"""
  
  def __init__(self, name:str, age:int):
    """create a user

    Args:
        name (str): the user's full name
        age (int): the user's age in years
    """
    self.name = name
    self.age = age
    
  def introduceSelf(self):
    """give a quick introduction

    Returns:
        str: an introduction phrase
    """
    return 'My name is ' + self.name

  
  def addAge(self, years:int):
    """add the given years to the user's age

    Args:
        years (int): the number of years to add

    Returns:
        int: the user's age after given years
    """
    return self.age +  years
