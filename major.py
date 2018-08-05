from req import *

class major():
    def __init__(self, list, name):
        self.list = list
        self.name = name

    # see if each requirement is satisfied

    def satisfied(self, l, c):
        string = "You're close to a " + str(self.name) + "!\n\nYou need:\n"
        i = 0

        # check each group of reqs
        for x in self.list:
            (l, count) = x.satisfied(l)

            # keep a running total of more classes needed
            i += count
            if (i > c):
                break
            string += (str(count) + " more class in " + str(x.name) + "\n")


        # if the number needed to take is in the input range, tell student how close they are
        string += ("\nTotal: " + str(i) + " more classes\n")
        if (i <= c):
            print string




pre = req(["cs1", "cs10"], "cs pre-recs", 2)
t = req(["cs30", "cs31", "cs35", "cs39", "cs40", "cs49"], "30-49", 2)
f = req(["cs50", "cs51", "cs52", "cs55", "cs56", "cs57", "cs58", "cs59", "cs60", "cs61", "cs63", "cs65", "cs67", "cs69", "cs69.08"], "50-69", 2)
s = req(["cs71", "cs73", "cs74", "cs75", "cs76", "cs77", "cs78", "cs81", "cs83", "cs84", "cs86", "cs87", "cs89"], "70-89", 2)
c = req(["cs98", "cs99"], "culminating experience", 1)
electives = req(["cs30", "cs31", "cs35", "cs39", "cs40", "cs49","cs50", "cs51", "cs52", "cs55", "cs56", "cs57", "cs58", "cs59", "cs60", "cs61", "cs63", "cs65", "cs67", "cs69", "cs69.08","cs71", "cs73", "cs74", "cs75", "cs76", "cs77", "cs78", "cs81", "cs83", "cs84", "cs86", "cs87", "cs89", "math22"], "cs electives", 3)

m = major([pre, t, f, s, electives, c], "CS Major!")

major_list = [m]

#for i in major_list:
 #   i.satisfied(["cs1", "cs10", "cs30", "cs31", "math22", "cs86"], 6)

