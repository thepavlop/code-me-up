shape = input(" enter a shape ")

if shape == 'rectangle':
    i1 = input ('enter an int ')
    i1= int(i1)
    i2= input ('enter an int ')
    i2= int (i2)
    while i1 < 0:
        i1 = int(input('enter an int '))
    while i2 < 0:
        i2 = int(input('enter an int '))
    x = i1 * i2
    y= i1+i1+i2+i2
    print ('the area is:', x)
    print ('the perimeter is:', y)



    elif shape == 'triangle':
    i3 = input ("enter an int ")
    i3= int(i3)
    i4 = input ("enter an int ")
    i4= int (i4)
    i5=input ("enter an int ")
    i5= int (i5)
    while i3 < 0:
        i3 = int(input('enter an int '))
    while i4 < 0:
        i4 = int(input('enter an int '))
    while i5 < 0:
        i5 = int(input('enter an int '))
    l= (i3 * i4) / 2
    e= i3+ i4+ i5
    print('the area is:', l)
    print('the perimeter is:', e)













