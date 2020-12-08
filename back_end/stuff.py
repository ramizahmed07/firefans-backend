import random
import os
from datetime import  datetime


def random_stuff():

    print(random.randint(10000,99999))


def key():
    stuff=os.urandom(10)
    print(stuff.decode("utf-8"))
    print(datetime.now())

key()