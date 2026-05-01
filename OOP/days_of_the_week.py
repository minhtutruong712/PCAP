import datetime as dt
class WeekDayError(Exception):
    def __init__(self):        
        super().__init__("Sorry, I can't serve your request.")  
    
	

class Weeker:
    list_day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):        
        if day not in Weeker.list_day: 
            raise WeekDayError()
        else:
            self.__day = dt.datetime.strptime(day, '%a')

    def __str__(self):
        return dt.datetime.strftime(self.__day, "%a")
        

    def add_days(self, n):
        self.__day = self.__day + dt.timedelta(days=n)

    def subtract_days(self, n):
        self.__day = self.__day + dt.timedelta(days=-n)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
