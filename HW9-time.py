from math import floor

def show_menu():
    print('1_ Sum')
    print('2_ Subtract')
    print('3_ Convert Time to Seconds')
    print('4_ Convert Seconds to Time')
    print('5_ Exit')

class Time:
    def __init__(self, h, m, s):
        self.hour= h
        self.minute= m
        self.second= s

    def show_time(self):
        print('Time=',self.hour,':',self.minute,':',self.second)

    def sum(self,guess):
        result= Time(None, None, None)
        result.hour= self.hour + guess.hour
        result.minute= self.minute + guess.minute
        result.second= self.second + guess.second
        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result
    
    def sub(self,guess):
        result= Time(None, None, None)
        result.hour= self.hour - guess.hour
        result.minute= self.minute - guess.minute
        result.second= self.second - guess.second
        if result.second < 0:
            result.second += 60
            result.minute -= 1
        if result.minute < 0:
            result.minute += 60
            result.hour -= 1
        return result

    def Time2Second(self):
        result= self.hour*3600 + self.minute*60 + self.second
        return result

    def Second2Time(T):
        result= Time(None, None, None)
        result. hour= floor(T/3600)
        result. minute= floor((T - result.hour*3600) / 60)
        result.second= T - result.hour*3600 - result.minute*60
        return result

while True:
    show_menu()
    choice=int(input("Select an option:"))
    if choice==4:
        c=Time.Second2Time(int(input('S: ')))
        c.show_time()
    elif choice==5:
        exit()

    else:
        t1= Time(int(input('h1: ')),int(input('m1: ')),int(input('s1: ')))
        t2= Time(int(input('h2: ')),int(input('m2: ')),int(input('s2: ')))

        if choice==1:
            a= t1.sum(t2)
            a.show_time()

        elif choice==2:
            b= t1.sub(t2)
            b.show_time()

        elif choice==3:
            c= t1.Time2Second()
            d= t2.Time2Second()
            print('Total time1=', c, 'seconds')
            print('Total time2= ',d, 'seconds')
