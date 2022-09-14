import time
import datetime
import quote 
#THIS IS THE MASTER DASHBOARD


# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  (Year % 100 != 0) and (Year % 4 == 0)):   
    return True 
  # Else it is not a leap year  
  else:  
    return False  


def main():
    tomorrow = datetime.datetime.today + datetime.timedelta(days=1)
    days = 0
    new_year = time.localtime(time.time).tm_year + 1
    if(time.localtime(time.time()).tm_year == new_year):
        if CheckLeap(time.localtime(time.time()).tm_year):
            days_in_year = 366
        else:
            days_in_year = 365

    while True:

        # Get the current day:
        localtime = time.asctime(time.localtime(time.time()))
        if 0 <= time.localtime(time.time()).tm_hour <= 12:
            print("Good Morning")
        
        elif 12 <= time.localtime(time.time()).tm_hour <= 19:
            print("Good Afternoon")
        else:
            print("Good Evening")

        print("The current time is: ", localtime)
    
        # If it is a new day:
        if(datetime.datetime.today == tomorrow):
            tomorrow = datetime.datetime.today + datetime.timedelta(days=1)
            # Update Daily Events
            # increment the day counter by 1
            days +=1
            # Check to make sure you do not exceed the total number of days in a year
            if(time.localtime(time.time()).tm_year == new_year):
                if CheckLeap(time.localtime(time.time()).tm_year):
                    days_in_year = 366
                else:
                    days_in_year = 365
            if days > days_in_year:
                days = 0

            # Get the Quote of the Day
            quote.get_quote(days)

