#All the process in this format [proc name, PID, PPID] - Will work on getting the volatility output in this format since I will be parsing it for output using this.
allprocs =[["System",4,0],["smss.exe",208,4],["csrss.exe",296,288],["csrss.exe",344,324],["conhost",2246,344],["winlogon.exe",372,324],["wininit.exe",332,288],["lsass",444,332],["lsm",452,332],["services.exe",428,332],["svchost",568,428],["rundll32",2016,568],["svchost",628,428],["sppsvc",816,428],["svchost",856,428],["dwm",1476,856],["svchost",880,428],["svchost",916,428],["svchost",348,428],["svchost",504,428],["spoolsv",1076,428],["svchost",1104,428],["wlms",1264,428],["svchost",1736,428],["SearchIndexer",1800,428],["taskhost",1144,428],["svchost",1432,428],["explorer",1652,840],["regsvr32",1180,1652],["iexplore",1892,1652],["iexplore",2820,1892],["DumptIt",2860,1652]]

#Vars that hold dashes, spaces.
dashes = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
subProc = []
subProc2 = []
spaces = "                                                                                                                                                 "

#Padding for 1st sub process
endSpace = 29

#Starting loop for all process
for index in range(len(allprocs)):
    #Checking if this process has been shown on the screen already - that way a sub process doesnt appear as a main process
    first = 0
    if first == 0 and allprocs[index] not in subProc:
        print(str(allprocs[index]) + dashes[len((str(allprocs[index][0]))) +len((str(allprocs[index][2]))) + len((str(allprocs[index][2]))):18] + "-|")
        first = 1

    #Second loop to compare the PPID and PID of 2 process.
    for index2 in range(1,len(allprocs)):
        #Adding proccess to a list to know it was already printed.
        if allprocs[index][1] == allprocs[index2][2]:
            subProc.append(allprocs[index2])
            #If proccess already seen then will padd it more.
            if allprocs[index] in subProc:
                endSpace = 50
                subProc2.append(allprocs[index2])
                if allprocs[index] in subProc2:
                    endSpace = 70

            #Printing process's and reseting endSpace to default.
            print(spaces[0:endSpace] + "|__" + str(allprocs[index2]))
            endSpace = 28
