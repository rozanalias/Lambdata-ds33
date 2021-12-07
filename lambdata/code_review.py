''' IN style_example.py FILE '''

# What would you say if you were working with someone and this is the code they gave you?

import math
import sys
import pandas as pd


def exampl_1():
      ''' THIS IS NOT A LONG COMMENT '''
      some_tuple = (1, 2, 'b', 'a')
      some_variable = pd.DataFrame({"long":['LONG CODE LINES'],
                                   "other":[math.pi, 100,200, 300, 999],
                                  "data": [44, 555, 222, 3, 3, 4, 4, 5, 5, 5, 5]})
      return some_tuple, some_variable

def example_2():
      '''this the 2nd example''' 
  
      has_key = 'deprecated'
    
      return has_key
      
      
  
class Example3():
      def __init__(self, bar):
            self.bar = bar
            
      def n_bar(self):
            if self.bar == 1 :
              self.bar = self.bar * self.bar 
            else:
              print('many')
            return (sys.path, self.bar)