### 4th May 2022
# Module in Python 

# like libraries in C- program or packages in Java
# these are called Modukes in python 

# We make use of the modules in our program using keyword "import"

import platform     # platform module has method related to our sustem OS platform

tem = platform.system()
print(tem)

print(dir(platform))

# Sudan.py and UserModule.py files are used to demonstrate user defined modules 

from math import pi, sqrt         
# "from" is a keyword, "math" is a builtin module name, "import" is a keyword,
# "pi" is a variable constanr in the module maths, sqrt() is a function in the module math

print(f"\n{pi}")
print(sqrt(4))