from Counters import Time

class Clock:
    """
    Our implementation of the Clock class
    """

    def getTime(self):
        return Time.getTime()
    
    def setTime(self, time_info):
        Time.setTime(time_info)

    def getHour(self):
        """
        Return the current hour as an int.
        """
        time_info = Time.getTime()
        return time_info[3]

    def setHour(self, hour):
        """
        Set the RTC hour to the provided hour.
        """
        time_info = list(Time.getTime())  # Convert the tuple into a list
        time_info[3] = hour               # Update the hour
        Time.setTime(tuple(time_info))    # Save it back to the system

    def getMinute(self):
        """
        Return the current minute as an int.
        """
        time_info = Time.getTime()
        return time_info[4]
    
    def setMinute(self, minute):
        """
        Set the RTC minute to the provided minute.
        """
        time_info = list(Time.getTime())  # Convert the tuple into a list
        time_info[4] = minute             # Update the minute
        Time.setTime(tuple(time_info))    # Save it back to the system

    def getDate(self):
        """
        Return the current date as an int.
        """
        time_info = Time.getTime()
        return time_info[2]
    
    def setDate(self, date):
        """
        Set the RTC date to the provided date.
        """
        time_info = list(Time.getTime())  # Convert the tuple into a list
        time_info[2] = date               # Update the date
        Time.setTime(tuple(time_info))    # Save it back to the system
    
    def getMonth(self):
        """
        Return the current month as an int.
        """
        time_info = Time.getTime()
        return time_info[1]

    def setMonth(self, month):
        """
        Set the RTC month to the provided month.
        """
        time_info = list(Time.getTime())  # Convert the tuple into a list
        time_info[1] = month              # Update the month
        Time.setTime(tuple(time_info))    # Save it back to the system

    def getDay(self):
        """
        Return the current day of the week as an int (0=Monday, 6=Sunday).
        """
        time_info = Time.getTime()
        return time_info[6]

    def setDay(self, day):
        """
        Set the RTC day of the week to the provided day (0=Monday, 6=Sunday).
        """
        time_info = list(Time.getTime())  # Convert the tuple into a list
        time_info[6] = day                # Update the day of the week
        Time.setTime(tuple(time_info))    # Save it back to the system

    def getDaysInMonth(self, month, year):
        """
        Return the number of days in the given month of the given year.
        """
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            # Check for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 31
