#All the process in this format [proc name, PID, PPID] - Will work on getting the volatility output in this format since I will be parsing it for output using this.
allprocs =[["System",4,0],["smss.exe",208,4],["csrss.exe",296,288],["csrss.exe",344,324],["conhost",2246,344],["winlogon.exe",372,324],["wininit.exe",332,288],["lsass",444,332],["lsm",452,332],["services.exe",428,332],["svchost",568,428],["rundll32",2016,568],["svchost",628,428],["sppsvc",816,428],["svchost",856,428],["dwm",1476,856],["svchost",880,428],["svchost",916,428],["svchost",348,428],["svchost",504,428],["spoolsv",1076,428],["svchost",1104,428],["wlms",1264,428],["svchost",1736,428],["SearchIndexer",1800,428],["taskhost",1144,428],["svchost",1432,428],["explorer",1652,840],["regsvr32",1180,1652],["iexplore",1892,1652],["iexplore",2820,1892],["DumptIt",2860,1652],["SMSS222",111,208],["SMMS333",123,4]]

#Sorting if neeeded.
#allprocs.sort(key = lambda allprocs: allprocs[1])

#print(allprocs)

#Vars that hold dashes, spaces.
dashes = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
subProc = []
subProc2 = []
subProc3 = []
spaces = "                                                                                                                                                 "

#Padding for 1st sub process
endSpace = 28

#Starting loop for all process
for index in range(len(allprocs)):
    endSpace = 29
    #Checking if this process has been shown on the screen already - that way a sub process doesnt appear as a main process
    first = 0
    if first == 0 and allprocs[index] not in subProc:
        print("FRIST" + str(allprocs[index]) + dashes[len((str(allprocs[index][0]))) +len((str(allprocs[index][2]))) + len((str(allprocs[index][2]))):18] + "-|")


    #Second loop to compare the PPID and PID of 2 process.
        for index2 in range(len(allprocs)):
            #Adding proccess to a list to know it fwas already printed.
            if allprocs[index][1] == allprocs[index2][2]:
                subProc.append(allprocs[index2])
                # Printing process's and reseting endSpace to default.
                print("SECOND" + spaces[0:endSpace] + "|__" + str(allprocs[index2]))

                in
                    if allprocs[index3][2] == allprocs[index2][1]:
                        print("Third" + spaces[0:endSpace] + "|" + spaces[0:endSpace] + "|__" + str(allprocs[index3]))

                        for index4 in range(len(allprocs)):
                            if allprocs[index4][2] == allprocs[index3][1]:
                                print("Fourth" + spaces[0:endSpace] + "|" + spaces[0:endSpace] + "|" + spaces[0:endSpace] + "|__" + str(
                                    allprocs[index4]))

            #

                # #If proccess already seen then will padd it more.
            if allprocs[index] in subProc:
                continue


def compPIDPPID():
    for index in range(len(allprocs)):
        if allprocs[index+1][2] == allprocs[index][1]:
            print("????" + spaces[0:endSpace] + "|__" + str(allprocs[index]))