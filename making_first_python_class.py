class Admission:
    def __init__(self):
        self.name = input(f'Enter your name:')
        self.address = input(f'Enter your address:')
        self.bd = int(input(f'Enter your Birth Day  :'))
        self.bm = int(input(f'Enter your Birth Month:'))
        self.by = int(input(f'Enter your Birth Year :'))
        self.ssc_gpa = float(input(f'Enter your Ssc GPA:'))
        self.hsc_gpa = float(input(f'Enter your Hsc GPA:'))
        self._year = 0
        self._month = 0
        self._date = 0
        self.wiver = 0

    def cal_age(self):
        cd = 9
        cm = 8
        cy = 2023

        month = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

        if self.bd > cd:
            cm = cm - 1
            cd = cd + month[self.bm-1]

        if self.bm > cm:
            cy = cy - 1
            cm = cm + 12

        self._date = cd - self.bd
        self._month = cm - self.bm
        self._year = cy - self.by

    def cal_wiver(self):
        if self.ssc_gpa == 5.00 and self.hsc_gpa == 5.00:
            self.wiver = 100

        elif 4.50 <= self.ssc_gpa <= 5.00 :
            self.wiver = 60
            if 4.50 <= self.hsc_gpa < 5.00:
              self.wiver = 60 
            elif 4.00 <= self.hsc_gpa < 4.50:
              self.wiver = 40
            elif 3.50 <= self.hsc_gpa < 4.00:
              self.wiver = 30
            elif self.hsc_gpa < 3.50 :
              self.wiver = 10

        elif 4.00 <= self.ssc_gpa <= 4.49 :
            self.wiver = 40
            if 4.00 <= self.hsc_gpa < 4.50:
              self.wiver = 40
            elif 3.50 <= self.hsc_gpa < 4.00:
              self.wiver = 30
            elif self.hsc_gpa < 3.50 :
              self.wiver = 10

        elif 3.50 <= self.ssc_gpa < 4.00 :
            self.wiver = 30
            if 3.50 <= self.hsc_gpa < 4.00:
              self.wiver = 30
            elif self.hsc_gpa < 3.50 :
              self.wiver = 10

        else:
            self.wiver = 10

    def show(self):
        print("=========   Admission Info  =========")
        print(f"Name          : {self.name}")
        print(f"Address       : {self.address}")
        print(f"Age           : {self._year} Year {self._month} Month {self._date} Day")
        print(f"Getting Wiver : {self.wiver}")




ad = Admission()
ad.cal_age()
ad.cal_wiver()
ad.show()
