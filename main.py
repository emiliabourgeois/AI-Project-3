import sys
import re
import BIFparser
import GibbsSampling
import Node

childlittle = [["lowerBodyO2","<5"],
        ["RUQO2","12+"],
        ["CO2Report",">=7.5"],
        ["XrayReport","Asy/Patchy"]]
childmoderate = [["lowerBodyO2", "<5"],
        ["RUQO2", "12+"],
        ["CO2Report", ">=7.5"],
        ["XrayReport", "Asy/Patchy"],
        ["GruntingReport", "yes"],
        ["LVHreport","yes"],
        ["Age", "11-30_days"]]
winb = [["Problem1", "No_Output"]]
winc = [["Problem2", "Too_Long"]]
wind = [["Problem3","No"]]
wine = [["Problem4", "No"]]
winf = [["Problem5", "No"]]
wing = [["Problem6", "Yes"]]
AlarmLittle = [["HRBP", "HIGH"],
               ["CO","LOW"],
               ["BP","HIGH"]]
AlarmModerate = [["HRBP", "HIGH"],
        ["CO","LOW"],
        ["BP","HIGH"],
        ["HRSAT", "LOW"],
        ["HREKG","LOW"],
        ["HISTORY","TRUE"]]
HailfinderLittle = [["R5Fcst", "XNIL"],
        ["N34StarFcst","XNIL"],
        ["MountainFcst","XNIL"],
        ["AreaMoDryAir","VeryWet"]]
HailfinderModerate = [["R5Fcst", "XNIL"],
        ["N34StarFcst","XNIL"],
        ["MountainFcst","XNIL"],
        ["AreaMoDryAir","VeryWet"],
        ["CombVerMo","Down"],
        ["AreaMeso_ALS","Down"],
        ["CurPropConv","Strong"]]
InsuranceLittle = [["Age","Adolescent"],
        ["GoodStudent","False"],
        ["SeniorTrain","False"],
        ["DrivQuality","Poor"]]
InsuranceModerate = [["Age","Adolescent"],
        ["GoodStudent","False"],
        ["SeniorTrain","False"],
        ["DrivQuality","Poor"],
        ["MakeModel","Luxury"],
        ["CarValue","FiftyThou"],
        ["DrivHist","Zero"]]

def main():
        filenames = ["alarm.bif", "child.bif", "hailfinder.bif", "insurance.bif", "win95pts.bif"]
        reports = [["HYPOVOLEMIA", "LVFAILURE", "ERRLOWOUTPUT"], ["Disease"], ["SatContMoist", "LLIW"], ["MedCost","ILiCost", "PropCost"], ["Problem1", "Problem2", "Problem3", "Problem4", "Problem5", "Problem6"]]
        evidence = [[[], AlarmLittle, AlarmModerate], [[], childlittle, childmoderate], [[], HailfinderLittle, HailfinderModerate], [[], InsuranceLittle, InsuranceModerate], [[], winb, winc, wind, wine, winf, wing]]
        X = None
        evi = True
        for f in range(len(filenames)):
                bn = BIFparser.parseBIF(filenames[f])
                for q in evidence[f]:
                        for r in reports[f]:
                                for n in bn:
                                        if n.name.casefold() in r.casefold():
                                                X = n
                                for n in bn:
                                        n.value = 0
                                dist, decisions, ev = (GibbsSampling.GB(X, bn, q))
                                if evi:
                                        if len(ev) > 0:
                                                print("---------")
                                                print("Evidence")
                                                print("--------")
                                                for e in ev:
                                                        print(e[0] + ": " + e[1])
                                        else:
                                                print("-------------")
                                                print("Evidence: N/A")
                                        evi = False
                                print("-------------------")
                                print("Report: " + X.name)
                                print("-------------------")
                                c = 0
                                for s in X.states:
                                        print(s + " " + str("{0:0.4f}".format(dist[c])))
                                        c += 1
                        evi = True



main()