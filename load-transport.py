def fun():

    #For load provider input

    veh_type=raw_input('provide the vehicle type\n')
    date=raw_input("enter the date in format dd-mm-yy\n")
    source=raw_input("enter the source city\n")
    destination=raw_input("enter the destination city\n")


    #for transporter input

    types_veh={}
    n=int(raw_input("enter total number of vehicle types\n"))
    for i in range(n):
        veh=raw_input("enter the vehicle types\n")
        m=int(raw_input("enter the total vehicle numbers of the type mentioned\n"))
        templ=[]
        for j in range(m):
            templ.append(raw_input("enter the vehicle numbers"))
        types_veh[veh]=templ
    loc={}
    l=int(raw_input("enter the number of available location\n"))
    for i in range(l):
        location=raw_input("enter the location name\n")
        t=int(raw_input("enter the total types of vehicles available in the mentioned location\n"))
        templ=[]
        for j in range(t):
            templ.append(raw_input("enter the type\n"))
        loc[location]=templ
    d=int(raw_input("enter the sample total number of dates of availability\n"))
    trans_date={}
    for i in range(d):
        dates=raw_input("enter the dates in format dd-mm-yy")
        t=int(raw_input("enter the number of vehicle types available on this date "+dates+"\n"))
        templ=[]
        for j in range(t):
            templ.append(raw_input("enter the types"))
        trans_date[dates]=templ

    print types_veh
    print trans_date
    print loc


    #operations start from here

    if veh_type in types_veh and source in loc and date in trans_date:
        print "congrats you can have the vehicle from "+source+" to "+destination
        print " with vehicle number "+str(types_veh[veh_type][0])
        del(types_veh[veh_type][0])
        return 0

    if veh_type not in types_veh:
        print"please select the type of vehicle from the following:\n"
        for k in types_veh.iterkeys():
            print(k)
        print"input 1 if vehicle not found\n"
        chosen=(raw_input("\n"))
        if chosen=='1':
            print"sorry the mentioned combination not available"
            return 0
        print"choose from available dates for the vehicle type mentioned :\n"
        for k in trans_date.iterkeys():
            if chosen in trans_date[k]:
                print(k)
        print"input 1 if date not found\n"
        dt=raw_input("\n")
        if dt=='1':
            print"sorry the mentioned combination not available"
            return 0
        print "choose from the available locations for the vehicle type mentioned:\n"
        for k in loc.iterkeys():
            if chosen in loc[k]:
                print (k)
        print"input 1 if location not found\n"
        lc=(raw_input())
        if lc=='1':
            print"sorry the mentioned combination not available"
            return 0
        print "congrats you can have the vehicle from " + lc + " to " + destination
        print " with vehicle number " + str(types_veh[chosen][0])+" and date "+dt
        del (types_veh[chosen][0])
        return 0

    if date not in trans_date:
        print"choose from available dates for the vehicle type mentioned :\n"
        for k in trans_date.iterkeys():
            if veh_type in trans_date[k]:
                print(k)
        print"input 1 if date not found\n"
        dt = raw_input("\n")
        if dt=='1':
            print"sorry the mentioned combination not available"
            return 0
        print "choose from the available locations for the vehicle type mentioned:\n"
        for k in loc.iterkeys():
            if veh_type in loc[k]:
                print k
        print"input 1 if location not found\n"
        lc = (raw_input())
        if lc=='1':
            print"sorry the mentioned combination not available"
            return 0
        print "congrats you can have the vehicle from " + lc + " to " + destination
        print " with vehicle number " + str(types_veh[veh_type][0]) + " and date " + dt
        del (types_veh[veh_type][0])
        return 0

    if source not in loc:
        print "choose from the available locations for the vehicle type mentioned:\n"
        for k in loc.iterkeys():
            if veh_type in loc[k]:
                print k
        print"input 1 if location not found\n"
        lc = (raw_input())
        if lc=='1':
            print"sorry the mentioned combination not available"
            return 0
        print "congrats you can have the vehicle from " + source + " to " + destination
        print " with vehicle number " + str(types_veh[veh_type][0]) + " and date " + date
        del (types_veh[veh_type][0])
        return 0
if __name__=="__main__":
    fun()


