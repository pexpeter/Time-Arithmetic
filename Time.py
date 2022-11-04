class Time:
    def __init__(self,day,hour,minute,second):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second   
    def convert_to_seconds(self):
        daytosec= self.day * 24 * 60 *60
        hrtosec = self.hour * 60 * 60
        mintosec = self.minute * 60
        
        print(str(self.day) + " days to seconds is:", daytosec, " \n")
        print(str(self.hour) + " hours to seconds:", hrtosec, " \n")
        print(str(self.minute) + " minutes to seconds:", mintosec, " \n")
        
    def convert_to_minutes(self):
        daytomin= self.day * 24 * 60
        hrtomin = self.hour * 60
        sectomin = self.second // 60
        
        print( str(self.day) + " days to minutes is:", daytomin, " \n")
        print(str(self.hour) + " hours to minutes is:", hrtomin, " \n")
        print(str(self.second) + " seconds to minutes is:", sectomin, " \n")
        
    def convert_to_hours(self):
        daytohr= self.day * 24
        mintohr = self.minute / 60
        sectohr = self.second / (60 * 60)
                
        print( str(self.day) + " days to hours is:", round(daytohr,1), " \n")
        print(str(self.minute) + " minutes to hours is:", round(mintohr,1), " \n")
        print(str(self.second) + " seconds to hours is:", round(sectohr,1), " \n")
        
    def convert_to_days(self):
        hrtoday = self.hour / 24
        mintoday = self.minute / (60 * 60)
        sectoday = self.second / (24 *60 *60)
        
        print(str(self.hour) + " hours to days is:", round(hrtoday,1), " \n")
        print(str(self.minute) + " minutes to days is:", round(mintoday,1), " \n")
        print(str(self.second) + " seconds to days is:", round(sectoday,1), " \n")
        