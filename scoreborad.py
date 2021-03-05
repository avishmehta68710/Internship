from datetime import datetime
ipl_teams = ["Royal Challengers Banglore","Chennai Super Kings","Mumbai Indians","Kolkata Knight Riders","Sunrisers Hydrabad","Delhi Capitals","Rajasthan Royals","Kings XI Punjab"]
ipl_grounds = ["Banglore","Chennai","Mumbai","Kolkata","Hyderabad","Delhi","Jaipur","Punjab"]

sunday = []
saturday = []
i = 0
while i<len(ipl_teams):
    if (i%2 == 0):
        sunday.append([ipl_teams[i],ipl_teams[i+1],ipl_grounds[i]])
    i += 2
j = 0
sunday_swap = []
while j<len(ipl_teams):
    sunday_swap.append([ipl_teams[j],ipl_teams[j+1],ipl_grounds[ipl_teams.index(ipl_teams[j+1])]])
    j += 2
sunday += sunday_swap
saturday = sunday[::-1]
#print("sat",saturday)
#print("sun",sunday)

match1 = []
match2 = []
match3 = []
match4 = []
match5 = []
match6 = []
match7 = []
match1_swap = []
match2_swap = []
match3_swap = []
match4_swap = []
match5_swap = []
match6_swap = []
match7_swap = []
count = 0
for i in range(0,len(ipl_teams)):
    try:
        
        match2.append([ipl_teams[i],ipl_teams[i+2],ipl_grounds[i]])
        match1.append([ipl_teams[i],ipl_teams[i+3],ipl_grounds[i]])
        match3.append([ipl_teams[i],ipl_teams[i+4],ipl_grounds[i]])
        match4.append([ipl_teams[i],ipl_teams[i+5],ipl_grounds[i]])
        match5.append([ipl_teams[i],ipl_teams[i+6],ipl_grounds[i]])
        match6.append([ipl_teams[i],ipl_teams[i+7],ipl_grounds[i]])
    except:
        pass

    # print("m1",match1)
    # print("m2",match2)
    # print("m3",match3)
    # print("m4",match4)
    # print("m5",match5)
    # print("m6",match6)


for i in range(0,len(ipl_teams)):
    try:
        match1_swap.append([ipl_teams[i],ipl_teams[i+2],ipl_grounds[ipl_teams.index(ipl_teams[i+2])]])
        match2_swap.append([ipl_teams[i],ipl_teams[i+3],ipl_grounds[ipl_teams.index(ipl_teams[i+3])]])
        match3_swap.append([ipl_teams[i],ipl_teams[i+4],ipl_grounds[ipl_teams.index(ipl_teams[i+4])]])
        match4_swap.append([ipl_teams[i],ipl_teams[i+5],ipl_grounds[ipl_teams.index(ipl_teams[i+5])]])
        match5_swap.append([ipl_teams[i],ipl_teams[i+6],ipl_grounds[ipl_teams.index(ipl_teams[i+6])]])
        match6_swap.append([ipl_teams[i],ipl_teams[i+7],ipl_grounds[ipl_teams.index(ipl_teams[i+7])]])
    except:
        pass

#print(match1)

day1 = []
day1 += match1
day1 += match1_swap


day2 = []
day2 += match2
day2 += match2_swap

#print(day2)

day3 = []
day3 += match3
day3 += match3_swap

#print(day3)
# sums = 0
day4 = []
even = []
odd = []
for i in range(len(match4)):
    try:
        if (i%2 == 0):
            even.append(match4[i])
        else:
            odd.append(match4[i])
    except:
        pass
day4 = even+odd

day4_swap = []
even = []
odd = []
for i in range(len(match4_swap)):
    try:
        if (i%2 == 0):
            even.append(match4_swap[i])
        else:
            odd.append(match4_swap[i])
    except:
        pass
day4_swap = even+odd
day4 += day4_swap

#print(day4)

day5 = []
even = []
odd = []
for i in range(len(match5)):
    try:
        if (i%2 == 0):
            even.append(match5[i])
        else:
            odd.append(match5[i])
    except:
        pass
day5 = even+odd

day5_swap = []
even = []
odd = []
for i in range(len(match5_swap)):
    try:
        if (i%2 == 0):
            even.append(match5_swap[i])
        else:
            odd.append(match5_swap[i])
    except:
        pass
day5_swap = even+odd
day5 += day5_swap

day6 = []
day6 += match6
day6 += match6_swap


final_match = []
final_match += day1[:2]
final_match += [day6[1]]
final_match += day1[2:]
final_match += day2[:-2]
final_match += [day6[0]]
final_match += day2[-2:]
final_match += day3
final_match += day4
final_match += day5


def scoreborad():
    #print(matches)
    print("Total Matches ",56)

    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    times = ["2:00","7:00"]
        
    today = datetime.now()
    current_day = today.strftime("%A") # gives the current day
    current_year = (today.year) # gives the current year
    current_month = (today.month) # gives the current month
    current_date = (today.day) # gives the current date
   # print("current_date",current_date)  
    #print("current_date",current_date)   

    count = current_date
    curr = current_day
    cur = days.index(curr)
    ans = days.index(curr)
    index = 0
    index_sat = 0
    index_final = 0
    j = 0
    satu = []
    sun = []
    fins = []
    dates = list(range(1,32))
    dates_index = 0
    while True:
        if (len(final_match) == 0 or dates_index>=30):
            break
        try:
            if (current_month>12):
                current_year += 1
                current_month = 1
            if (cur>6):
                cur = 0
                current_day = "Sunday"
            if (days[cur] == "Sunday"):
                k = 0
                while k<len(sunday):
                    if sunday[k][0] != satu[-1][0] and sunday[k][0] != satu[-1][1] and sunday[k][1] != satu[-1][0] and sunday[k][1] != satu[-1][1] and sunday[k][0] != satu[-2][0] and sunday[k][0] != satu[-2][1] and sunday[k][1] != satu[-1][0] and sunday[k][1] != satu[-1][1]:
                        TeamA = sunday[k][0]
                        TeamB = sunday[k][1]
                        print("-"*30)
                        print("Team A VS TeamB",sunday[k][0]," VS ",sunday[k][1])
                        print("Ground ",sunday[k][2])
                        print("Time ",times[0])
                        sun.append([sunday[k][0],sunday[k][1],sunday[k][2]])
                        sunday.remove(sunday[k])
                        break
                    k += 1
                print("Date ",str(dates[dates_index])+"/"+str(current_month)+"/"+str(current_year))
                print("Day ",days[cur])
                print("-"*30)
                m = 0
                while m<len(sunday):
                    if sunday[m][0] != satu[-1][0] and sunday[m][0] != satu[-1][1] and sunday[m][1] != satu[-1][0] and sunday[m][1] != satu[-1][1] and sunday[m][0] != satu[-2][0] and sunday[m][0] != satu[-2][1] and sunday[m][1] != sun[-1][0] and sunday[m][1] != sun[-1][1]:
                        print("Team A VS TeamB",sunday[m][0]," VS ",sunday[m][1])
                        print("Ground ",sunday[m][2])
                        print("Time ",times[1])
                        sun.append([sunday[m][0],sunday[m][1],sunday[m][2]])
                        sunday.remove(sunday[m])
                        break
                    m += 1
                print("Date ",str(dates[dates_index])+"/"+str(current_month)+"/"+str(current_year))
                print("Day ",days[cur])
                cur += 1
                index = k
                j += 2
            if days[cur] == "Saturday":
                while k<len(saturday):
                    if saturday[k][0] != fins[-1][0] and saturday[k][1] != fins[-1][1] and saturday[k][0] != fins[-1][1] and saturday[k][1] != fins[-1][0]:
                        TeamA = saturday[k][0]
                        TeamB = saturday[k][1]
                        print("-"*30)
                        print("Team A VS TeamB ",saturday[k][0]," VS ",saturday[k][1])
                        print("Ground ",saturday[k][2])
                        print("Time ",times[0])
                        satu.append([saturday[k][0],saturday[k][1],saturday[k][2]])
                        saturday.remove(saturday[k])
                        break
                    k += 1
                print("Date ",str(dates[dates_index])+"/"+str(current_month)+"/"+str(current_year))
                print("Day ",days[cur])
                print("-"*30)
                m = 0
                while m<len(saturday):
                    if saturday[m][0] != fins[-1][0] and saturday[m][1] != fins[-1][1] and saturday[m][0] != satu[-1][0] and saturday[m][1] != satu[-1][1] and saturday[m][0] != fins[-1][1] and saturday[m][1] != fins[-1][0]:
                        print("-"*30)
                        print("Team A VS TeamB",saturday[m][0]," VS ",saturday[m][1])
                        print("Ground ",saturday[m][2])
                        print("Time ",times[1])
                        satu.append([saturday[m][0],saturday[m][1],saturday[m][2]])
                        saturday.remove(saturday[m])
                        break
                    m += 1
                print("Date ",str(dates[dates_index])+"/"+str(current_month)+"/"+str(current_year))
                print("Day ",days[cur])
                cur += 1
                index_sat = k
                j += 2
            else:
                Days = (days[cur])
                if (Days == "Wednesday"):
                    pass
                else:
                    if (len(sun)>1 and (days[cur] == "Monday" or days[cur] == "Friday")):
                        if days[cur] == "Monday":
                            dates_index += 1
                        o = 0
                        while o<len(final_match):
                            if final_match[o][0] != sun[-1][0] and final_match[o][0] != sun[-1][1] and final_match[o][0] != sun[-2][0] and final_match[o][0] != sun[-2][1] and final_match[o][1] != sun[-1][0] and final_match[o][1] != sun[-1][1] and final_match[o][1] != sun[-2][0] and final_match[o][1] != sun[-2][1] and final_match[o][0] != fins[-1][0] and final_match[o][1] != fins[-1][1] and final_match[o][0] != fins[-1][1] and final_match[o][1] != fins[-1][0]:
                                print("-"*30)
                                print("Team A VS TeamB",final_match[o][0]," VS ",final_match[o][1])
                                print("Ground ",final_match[o][2])
                                fins.append([final_match[o][0],final_match[o][1],final_match[o][2]])
                                final_match.remove(final_match[o])
                                break
                            o += 1
                    elif days[cur] == "Tuesday":
                        n = 0
                        while n<len(final_match):
                            if final_match[n][0] != fins[-1][0] and final_match[n][1] != fins[-1][0] and final_match[n][1] != fins[-1][1] and final_match[n][0] != fins[-1][1]:
                                print("-"*30)
                                print("Team A VS TeamB",final_match[n][0]," VS ",final_match[n][1])
                                print("Ground ",final_match[n][2])
                                fins.append([final_match[n][0],final_match[n][1],final_match[n][2]])
                                final_match.remove(final_match[n])
                                break
                            n += 1
                    elif days[cur] == "Wednesday":
                        n = 0
                        while n<len(final_match):
                            if final_match[n][0] != fins[-1][0] and final_match[n][1] != fins[-1][0] and final_match[n][1] != fins[-1][1] and final_match[n][0] != fins[-1][1]:
                                print("-"*30)
                                print("Team A VS TeamB ",final_match[n][0]," VS ",final_match[n][1])
                                print("Ground ",final_match[n][2])
                                fins.append([final_match[n][0],final_match[n][1],final_match[n][2]])
                                final_match.remove(final_match[n])
                                break
                            n += 1              
                    else:
                        print("-"*30)
                        print("Teams A VS TeamB",final_match[0][0]," VS ",final_match[0][1])
                        print("Ground ",final_match[0][2])
                        fins.append([final_match[0][0],final_match[0][1],final_match[0][2]])
                        final_match.remove(final_match[0])
                    print("Date ",str(dates[dates_index])+"/"+str(current_month)+"/"+str(current_year))
                    Time = (times[-1])
                    Ground = (final_match[-index_final-1][2])
                    print("Day ",Days)
                    print("Time ",Time)
                    print("-"*30)
                    j += 1
                cur += 1
            dates_index += 1            
        except:
            j += 1
scoreborad()
