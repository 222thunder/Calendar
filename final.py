def zeller(d,m,y):
    #zeller's congurence 
    import math
    from math import floor
    if m==1:
        m=13
        y=y-1
    elif m==2:
        m=14
        y=y-1

    q=d
    K= y%100
    J= floor (y/100)
    h = (q+ floor ( (13* (m+1)) /5) +K+ floor (K/4) +floor (J/4) -2*J) %7
    return h

def nday(d,m,y):
    #To find what day was on a particular date
    h1 = zeller(d,m,y)
    dict1 = {0: 'Saturday' , 1: 'Sunday' ,2: 'Monday', 3: 'Tuesday',4: 'Wednesday',5: 'Thursday' ,6: 'Friday'}
    l = dict1[h1]
    return l
    

def leap(y):
    #To chechk it's leap year or not
    if y%4==0:
        return "yes"
    else:
        return "no"
        
def calendar(m,y):
    #To print calendar of a particular month of any year
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    monthdays = {'January': 31, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
                 'September': 30, 'October': 31, 'November': 30, 'December': 31}

    if (y%4) == 0:
        monthdays['February'] = 29
    else:
        monthdays['February'] = 28
    
    r=zeller(1,m,y)
    r = (r + 7) % 7
    
    space = ' '
    print(space * 4 + months[m] + space + str(y))
    print("Su Mo Tu We Th Fr Sa")
    number = monthdays[months[m]]
    start_days = r - 1
    for i in range(1, number + 1):
        if i == 1:
            print((space * 3) * start_days, end='')
        if i < 10:
            print('', i, end=' ')
        elif i >= 10:
            print(i, end=' ')
        if (i + start_days) % 7 == 0:
            print('\n', end='')
    
def yearcalendar(y):
    for i in range (1,13):
        a = calendar(i,y)
        print(a)
        print('\n')
