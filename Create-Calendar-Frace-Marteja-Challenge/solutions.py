

'''
Create a calendar without using a calendar libraries

'''



def determine_the_day(year):


    last_two_digit_of_year = year[-2:]
    one_quarter_of_year = int(last_two_digit_of_year) // 4
    given_day = 1
    key_number = 1

    total = int(last_two_digit_of_year) + one_quarter_of_year + given_day + key_number
    total -= 1

    week_number = round(divmod(total,7)[1],0)


    return week_number







def leap_year(year):
    divisible_by_4 = divmod(int(year),4)[1]
    if year[-1] != "0" and divisible_by_4 == 0:
        return True
    elif year[-1] == "0":
        is_leap = divmod(int(year),400)[1]
        if is_leap == 0:
            return True
    
    return False






def calendar(year):

    months = {"January":31,"February":28,"March":31,
              "April":30,"May":31,"June":30,
              "July":31,"August":31,"September":30,
              "October":31,"November":30,"December":31}
    weeks = {1:"Sun",2:"Mon",3:"Tue",4:"Wed",5:"Thu",6:"Fri",7:"Sat"}
    leapyear = leap_year(year)
    
    start_day = determine_the_day(year)
    if leapyear:
        months["February"] = 29

    day_started = start_day
    for k,v in months.items():
        print(f"{k}  {year} ")
        current_month_value = v + 1
        for key, value in weeks.items():
            print(f" {value}",end=" ")
        print()
        weeks_counter = 0

        subracted_day = day_started
        
        for i in range(1,current_month_value+day_started):
            if day_started != 0:
                print(f"   ",end="  ")
                day_started -=1

            elif len(str(i-subracted_day)) == 2:
                print(f" {i-subracted_day}",end="  ")
            else:
                print(f"  {i-subracted_day}",end="  ")
            weeks_counter +=1
            if weeks_counter == 7:
                print()
                weeks_counter = 0
        day_started = weeks_counter
        
        print()



test = input("year: ")

calendar(test)