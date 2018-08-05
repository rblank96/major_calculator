from major import *
from req import *


# sample test

#a student has taken these six classes and wants to know how close they are to each major within 7 classes

for i in major_list:
    i.satisfied(["cs1", "cs10", "cs30", "cs31", "math22", "cs86"], 7)