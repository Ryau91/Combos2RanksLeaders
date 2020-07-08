def convert(result):
    if len(str(result)) != 9:
        min = result // 6000
        sec = int((result % 6000)/100)
        centisec = str(result)[-2:] #this is a string which is inconsistent...
        if min == 0:
            return (str(sec) + "." + centisec)
        else:
            return(str(min) + ":" + str(sec).zfill(2) + "." + centisec)

    else:
        difference = 99 - int(str(result)[0:2])
        timeInSeconds = int(str(result)[2:7])
        missed = int(str(result)[-2:])
        solved = difference + missed
        attempted = solved + missed

        mhours = timeInSeconds // 3600
        timeMinusHours = timeInSeconds % 3600
        mmins = timeMinusHours // 60
        msecs = timeMinusHours % 60
        if mhours == 0:
            return (str(solved) + "/" + str(attempted) + " " + str(mmins) + ":" + str(msecs).zfill(2))
        else:
            return(str(solved) + "/" + str(attempted) + " " + str(mhours) + ":" + str(mmins) + ":" + str(msecs).zfill(2))