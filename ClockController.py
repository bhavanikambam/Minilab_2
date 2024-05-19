from Displays import LCDDisplay
from Button import *
from Clock import *

class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min, and day
        LCD display to show the time
    """

    def __init__(self): 
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [
            Button(10, 'white', buttonhandler=self),
            Button(11, 'red', buttonhandler=self),
            Button(12, 'yellow', buttonhandler=self),
            Button(13, 'blue', buttonhandler=self)
        ]

    def showTime(self):
        year, month, date, hour, minute, sec, wd, yd = self._clock.getTime()
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        months_of_year = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        day_str = days_of_week[wd]
        month_str = months_of_year[month - 1]
        
        self._display.showText(f'{hour:02d}:{minute:02d}:{sec:02d}\n{month_str} {date:02d} {day_str}')

    def buttonPressed(self, name):                 
        if name == 'white':
            month = self._clock.getMonth()
            self._clock.setMonth(1 if month == 12 else month + 1)

        elif name == 'red':
            year = self._clock.getTime()[0]
            month, date = self._clock.getMonth(), self._clock.getDate()
            if date == self._clock.getDaysInMonth(month, year):
                self._clock.setDate(1)
                self._clock.setMonth(1 if month == 12 else month + 1)
            else:
                self._clock.setDate(date + 1)
            
            day = self._clock.getDay()
            self._clock.setDay(0 if day == 6 else day + 1)

        elif name == 'yellow':
            hour = self._clock.getHour()
            if hour == 23:
                self._clock.setHour(0)
                self.buttonPressed('red')  # Increment date and day after 24 hours
            else:
                self._clock.setHour(hour + 1)

        elif name == 'blue':
            minute = self._clock.getMinute()
            if minute == 59:
                self._clock.setMinute(0)
                self.buttonPressed('yellow')  # Increment hour after 60 minutes
            else:
                self._clock.setMinute(minute + 1)

    def buttonReleased(self, name):
        pass
