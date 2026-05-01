import datetime as dt
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__time = dt.datetime.strptime(":".join([str(hours), str(minutes), str(seconds)]), "%H:%M:%S")

    def __str__(self):
        return dt.datetime.strftime(self.__time, "%H:%M:%S")

    def next_second(self):
        self.__time = self.__time + dt.timedelta(seconds=1)

    def prev_second(self):
        self.__time = self.__time + dt.timedelta(seconds=-1)


timer = Timer()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)