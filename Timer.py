class Time:
    """" Time class that takes time in days, hours, minutes and seconds, changes a time format to preffered format, 
    substracts time from another and displays time in a given format.
    
    Attributes:
        day(integer)      representing number of days.
        hour(float)   representing number of hours.
        minute(float) representing number of minutes.
        second(integer)   representing number of seconds.
    """
    
    
    def __init__(self,day,hour,minute,second):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second 
        
    def convert_to_preffered_format(self,comm):
        """Function to convert one time format to another.
        Args:
            comm (string): preffered time conversion
        Returns:
            float: converted time format
        """
        if comm=="to_sec":
            daytosec = self.day * 24 * 60 *60
            hrtosec = self.hour * 60 * 60
            mintosec = self.minute * 60
            print("{} days to seconds is:    {} seconds".format(self.day,daytosec))
            print("{} hours to seconds is:   {} seconds".format(self.hour,hrtosec ))
            print("{} minutes to seconds is: {} seconds".format(self.minute,mintosec))
        elif comm == "to_min":
            daytomin= self.day * 24 * 60
            hrtomin = self.hour * 60
            sectomin = self.minute / 60
            print("{} days to minutes is:    {} minutes".format(self.day,daytomin))
            print("{} hours to minutes is:   {} minutes".format(self.hour,hrtomin))
            print("{} seconds to minutes is: {} minutes".format(self.second,sectomin))
        elif comm == "to_hr":
            daytohr= self.day * 24
            mintohr = self.minute / 60
            sectohr =round(self.second / (60 * 60),1)
            print("{} days to hours is:    {} hours".format(self.day,daytohr))
            print("{} minutes to hours is: {} hours".format(self.minute , mintohr ))
            print("{} seconds to hours is: {} hours".format(self.second, sectohr ))
        elif comm == "to_day":
            hrtoday = self.hour / 24
            mintoday = self.minute / (60 * 60)
            sectoday = self.second / (24 *60 *60)
            print("{} hours to days is:   {} days".format(self.hour, hrtoday))
            print("{} minutes to days is: {} days".format(self.minute, mintoday))
            print("{} seconds to days is: {} days".format(self.second, sectoday))
        else:
            print("The function is not available in the program. Kindly check your command.")
            
            
    def time_to_substract(self,dy,hr,mins,sec):
        """Function to Substract Time(dy,hr,mins,sec) from Time(day,hour,minute,second).
        Args:
            dy (integer):  time in days to be substracted.
            hr (float):    time in hours to be substracted.
            mins (float):  time in minutes to be substracted.
            sec (integer): time in seconds to be substracted.
        Returns:
            float/integer: the time remaining after substraction.
        """
        self.dy=dy
        self.hr=hr
        self.min=mins
        self.sec=sec
        subday = self.day - self.dy 
        subhr = self.hour - self.hr 
        submin = self.minute - self.min
        subsec = self.second - self.sec
        print("The time after substraction is {} days {} hours {} minutes {} seconds".format(subday,subhr,submin,subsec))
        
        
    def display_time(self):
        """Function to display time in seconds or days,hours,minutes and seconds.
        
        Args:
            None
            
        Returns:
            float/integer: The time in time in seconds and, days,hours,minutes and seconds.
        """
        timeinsec = (self.day * 24 * 3600) + (self.hour * 3600) + (self.minute *60) + self.second
        print("The Time is {} days {} hours {} minutes and {} seconds".format(self.day,self.hour,self.minute,self.second)) 
        print("The Time is equivalent to {} seconds ".format(timeinsec))