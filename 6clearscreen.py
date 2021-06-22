# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  

def clear():
  
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()