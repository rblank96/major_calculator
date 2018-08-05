import copy

class req():
    # each requirement has a name, list of possible classes, and amount of them that each student must take to fullfill req
    def __init__(self, list, name, num):
        self.num = num
        self.list = list
        self.name = name

    # given a list of classes, will return how many more the student must take, and an updated list that takes out the classes used for this requirement
    def satisfied(self, l1):
        l2 = copy.deepcopy(l1)
        count = self.num

        to_remove = []

        for x in l2:

            if self.list.__contains__(x):
                count -= 1
                to_remove.append(x)

        for y in to_remove:
            l2.remove(y)

        if count < 0:
            count = 0

        return l2, count



