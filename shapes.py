"""
This program calculates the area and perimeter of a given shape.
Shapes: 'rectangle', 'triangle'.
"""

shape = input("Enter a shape (rectangle/triangle): ")

# User input is 'rectangle': 
if shape == 'rectangle':
    # Ask user for a height and width of the rectangle
    i1 = input ('Enter the width of the rectangle: ')
    i1 = int(i1)
    i2 = input ('Enter the height of the rectangle: ')
    i2 = int (i2)
    # Check that the height and the width are positive
    while i1 < 0:
        i1 = int(input('Enter the width of the rectangle: '))
    while i2 < 0:
        i2 = int(input('Enter the height of the rectangle: '))
    # Calculate area and perimeter:
    x = i1 * i2
    y = i1 + i1 + i2 + i2
    print ('The area of the rectangle is:', x)
    print ('The perimeter of the rectangle is:', y)



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













