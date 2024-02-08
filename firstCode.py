import json;
import sys

def add_function( *argv):
    total =0
    total = sum(argv)
   
    print("Python Version:")
    print(sys.version)
    print("Python Version Info:")
    print(sys.version_info)


    
    print(add_function(19,8))
    return total

print(add_function(5,6,7))
