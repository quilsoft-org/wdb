# Esto usa fork que segun dice esta depreciado

# import os

# from wdb import set_trace as wtf

# print("Forking")

# pid = os.fork()

# if pid == 0:
#     print("In children")
#     wtf()
#     print("Children dead")
# else:
#     print("In parent")
#     wtf()
#     print("Parent dead")

# print("The End")

from multiprocessing import Process
from wdb import set_trace as wtf

def child():
    print("In child")
    wtf()
    print("Child dead")

print("Forking")

p = Process(target=child)
p.start()

print("In parent")
wtf()
p.join()

print("Parent dead")
print("The End")
