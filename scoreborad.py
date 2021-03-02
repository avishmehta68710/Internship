from datetime import datetime

def match_fixing():
    ipl_teams = ["Royal Challengers Banglore","Chennai Super Kings","Mumbai Indians","Kolkata Knight Riders","Sunrisers Hydrabad","Delhi Capitals","Rajasthan Royals","Kings XI Punjab"]
    ipl_grounds = ["Banglore","Chennai","Mumbai","Kolkata","Hyderabad","Delhi","Jaipur","Punjab"]

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
    for i in range(0,len(ipl_teams)):
        try:
            match1.append([ipl_teams[i],ipl_teams[i+1],ipl_grounds[i]])
            match2.append([ipl_teams[i],ipl_teams[i+2],ipl_grounds[i]])
            match3.append([ipl_teams[i],ipl_teams[i+3],ipl_grounds[i]])
            match4.append([ipl_teams[i],ipl_teams[i+4],ipl_grounds[i]])
            match5.append([ipl_teams[i],ipl_teams[i+5],ipl_grounds[i]])
            match6.append([ipl_teams[i],ipl_teams[i+6],ipl_grounds[i]])
            match7.append([ipl_teams[i],ipl_teams[i+7],ipl_grounds[i]])
        except:
            pass

    for i in range(0,len(ipl_teams)):
        try:
            match1_swap.append([ipl_teams[i],ipl_teams[i+1],ipl_grounds[ipl_teams.index(ipl_teams[i+1])]])
            match2_swap.append([ipl_teams[i],ipl_teams[i+2],ipl_grounds[ipl_teams.index(ipl_teams[i+2])]])
            match3_swap.append([ipl_teams[i],ipl_teams[i+3],ipl_grounds[ipl_teams.index(ipl_teams[i+3])]])
            match4_swap.append([ipl_teams[i],ipl_teams[i+4],ipl_grounds[ipl_teams.index(ipl_teams[i+4])]])
            match5_swap.append([ipl_teams[i],ipl_teams[i+5],ipl_grounds[ipl_teams.index(ipl_teams[i+5])]])
            match6_swap.append([ipl_teams[i],ipl_teams[i+6],ipl_grounds[ipl_teams.index(ipl_teams[i+6])]])
            match7_swap.append([ipl_teams[i],ipl_teams[i+7],ipl_grounds[ipl_teams.index(ipl_teams[i+7])]])
        except:
            pass

    day1 = []
    even = []
    odd = []
    for i in range(len(match1)):
        try:
            if (i%2 == 0):
                even.append(match1[i])
            else:
                odd.append(match1[i])
        except:
            pass
    day1 = even+odd

    day1_swap = []
    even = []
    odd = []
    for i in range(len(match1_swap)):
        try:
            if (i%2 == 0):
                even.append(match1_swap[i])
            else:
                odd.append(match1_swap[i])
        except:
            pass
    day1_swap = even+odd
    day1 += day1_swap
   # print(day1)

    day2 = []
    day2 += match2
    day2 += match2_swap
  #  print(day2)

    day3 = []
    day3 += match3
    day3 += match3_swap
   # print(day3)

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
    
   # print(day4)

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
   # print(day5)

    day6 = []
    even = []
    odd = []
    for i in range(len(match6)):
        try:
            if (i%2 == 0):
                even.append(match6[i])
            else:
                odd.append(match6[i])
        except:
            pass
    day6 = even+odd

    day6_swap = []
    even = []
    odd = []
    for i in range(len(match6_swap)):
        try:
            if (i%2 == 0):
                even.append(match6_swap[i])
            else:
                odd.append(match6_swap[i])
        except:
            pass
    day6_swap = even+odd

    day6 += day6_swap
   # print(day6)

    final_match = []
    final_match += day1
    final_match += day2
    final_match += day3
    final_match += day4
    final_match += day5
    final_match += day6
    temp = final_match[-6]
    final_match[-6] = final_match[-5]
    final_match[-5] = temp
    #print("final",final_match)
    #print(final_match[-6],final_match[-7])
    #print(len(final_match),final_match[-1])
    #final_match[-6],final_match[-5] = final_match[-5],final_match[-6]
    return final_match

def scoreborad():
    matches = match_fixing()
    #print(matches)
    print("Total Matches ",56)

    days = ["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
    times = ["2:00","7:00"]
        
    today = datetime.now()
    current_day = today.strftime("%A") # gives the current day
    current_year = (today.year) # gives the current year
    current_month = (today.month) # gives the current month
    current_date = (today.day) # gives the current date
        

    count = 0
    curr = current_day
    cur = days.index(curr)
    ans = days.index(curr)

    j = 0
    while j<len(matches):
        try:
            Date = str(current_date)+"/"+str(current_month)+"/"+str(current_year)
            current_date += 1
            if (current_date>31):
                current_month += 1
                current_date = 1
            if (current_month>12):
                current_year += 1
                current_month = 1
            if (cur>6):
                cur = 0
                current_day = "Sunday"
            if (days[cur] == "Sunday"):
                print("-"*30)
                TeamA = matches[j][0]
                TeamB = matches[j][1]
                Days = (days[cur])
                Time = (times[0])
                Ground = matches[j][2]
                print("Date: ",Date)
                print("Day ",Days)
                print("Teams ",TeamA+" VS "+TeamB)
                print("Ground ",Ground)
                print("Time ",Time)
                print("\n")
                TeamA = matches[j+1][0]
                TeamB = matches[j+1][1]
                Days = (days[cur])
                Ground = (matches[j+1][2])
                Time = (times[1])
                print("Date ",Date)
                print("Day ",Days)
                print("Teams ",TeamA+" VS "+TeamB)
                print("Ground ",Ground)
                print("Time ",Time)
                print("-"*30)
                cur += 1
                j += 2
            if days[cur] == "Saturday":
                TeamA = matches[j][0]
                TeamB = matches[j][1]
                Days = (days[cur])
                Ground = (matches[j][2])
                Time = (times[0])
                print("-"*30)
                print("Date ",Date)
                print("Day ",Days)
                print("Teams ",TeamA+" VS "+TeamB)
                print("Ground ",Ground)
                print("Time ",Time)
                print("-"*30)
                print("\n")
                TeamA = matches[j+1][0]
                TeamB = matches[j+1][1]
                Days = (days[cur])
                Ground = (matches[j+1][2])
                Time = (times[1])
                print("Date ",Date)
                print("Day ",Days)
                print("Teams ",TeamA+" VS "+TeamB)
                print("Ground ",Ground)
                print("Time ",Time)
                print("-"*30)
                cur += 1
                j += 2
            else:
                Days = (days[cur])
                if (Days == "Wednesday"):
                    #print(type(Days))
                    pass
                else:
                    TeamA = matches[j][0]
                    TeamB = matches[j][1]
                    Time = (times[-1])
                    Ground = (matches[j][2])
                    print("-"*30)
                    print("Date ",Date)
                    print("Day ",Days)
                    print("Teams ",TeamA+" VS "+TeamB)
                    print("Ground ",Ground)
                    print("Time ",Time)
                    j += 1
                cur += 1
        except:
            j += 1
scoreborad()
