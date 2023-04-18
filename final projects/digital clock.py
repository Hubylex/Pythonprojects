import time


hour = int(input('enter time(hours)'))
minute = int(input('enter time(minutes)'))
second = int(input('enter time(seconds)'))




def time_add():
        global second
        global minute
        global hour


        second += 1
        if  second == 60:
            minute += 1
            second = 0

        if  minute == 60:
            hour += 1
            minute = 0

        if hour == 24:
            hour = 0



def display():
    print(hour,':',minute,':',second)


while True:
    time.sleep(1)
    time_add()
    display()



