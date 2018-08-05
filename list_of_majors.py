from req import *
from major import*
######### MAJORS ########

#Cs Major
pre = req(["cs1", "cs10"], "cs pre-recs", 2)
t = req(["cs30", "cs31", "cs35", "cs39", "cs40", "cs49"], "30-49", 2)
f = req(["cs50", "cs51", "cs52", "cs55", "cs56", "cs57", "cs58", "cs59", "cs60", "cs61", "cs63", "cs65", "cs67", "cs69", "cs69.08"], "50-69", 2)
s = req(["cs71", "cs73", "cs74", "cs75", "cs76", "cs77", "cs78", "cs81", "cs83", "cs84", "cs86", "cs87", "cs89"], "70-89", 2)
c = req(["cs98", "cs99"], "culminating experience", 1)
electives = req(["cs30", "cs31", "cs35", "cs39", "cs40", "cs49","cs50", "cs51", "cs52", "cs55", "cs56", "cs57", "cs58", "cs59", "cs60", "cs61", "cs63", "cs65", "cs67", "cs69", "cs69.08","cs71", "cs73", "cs74", "cs75", "cs76", "cs77", "cs78", "cs81", "cs83", "cs84", "cs86", "cs87", "cs89", "math22"], "cs electives", 3)

m = major([pre, t, f, s, electives, c], "CS Major!")

######### MINORS ########

#AAAS minor
pre = req(["aaas10", "aas11"], "aaas pre-recs", 2)
l = req(["aaas12", "aas13", "aas14", "aas15", "aas16", "aas17", "aas18", "aas19", "aas23", "aas25", "aas26", "aas31", "aas34", "aas35", "aas39.01", "aas39.02", "aas40", "aas42", "aas44", "aas46", "aas50", "aas52", "aas53", "aas54", "aas56", "aas60", "aas61", "aas62", "aas63", "aas65", "aas67", "aas68", "aas80.05", "aas80.06", "aas80.07","aas80.08", "aas80.09", "aas80.10", "aas81.01", "aas81.05", "aas81.07", "aas82.01", "aas82.05","aas83.02", "aas83.05","aas83.06", "aas83.07", "aas86.04", "aas87.05", "aas87.06", "aas87.07", "aas87.08", "aas87.09", "aas87.11", "aas88.02", "aas88.07", "aas88.08", "aas88.11", "aas88.12", "aas88.13", "aas88.14", "aas88.15", "aas88.16", "aas88.17", "aas88.18", "aas89", "aas90.01", "aas90.02", "aas90.07", "aas90.08", "aas97", "aas98", "aas99"], "aaas electives", 4)

aaas = major([pre, l], "AAAS MINOR")

#ANTH minor
pre = req(["anth01"], "anth pre-recs", 1)
l = req(["anth01"], "anth pre-recs", 1)
major_list = [m]