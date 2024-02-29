from datetime import datetime

class student:
    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__class = classification
        self.__age = None
        self.__registration = None

    def calc_age(self):
        today = datetime.now()
        self.__age = today.year - self.__dob.year

    def registration(self):
        senior_dates = "4/1 thru 4/3"
        junior_dates = "4/4 thru 4/6"
        sophomore_dates = "4/7 thru 4/9"
        freshmen_dates = "4/10 thru 4/12"

        if self.__class == 'Senior':
            self.__registration = senior_dates
        elif self.__class == 'Junior':
            self.__registration = junior_dates
        elif self.__class == 'Sophomore':
            self.__registration = sophomore_dates
        elif self.__class == 'Freshmen':
            self.__registration = freshmen_dates
        
    def get_age(self):
        return self.__age
    
    def get_registration(self):
        return self.__registration
