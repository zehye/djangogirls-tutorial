def print_self():
    print("I'm in_app")


from .in_app2 import print_self as print_app2
from . import in_app2
from app import in_app2
#print_self()
in_app2.print_self()
print_app2()
in_app2()