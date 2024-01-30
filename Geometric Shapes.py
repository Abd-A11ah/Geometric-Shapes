#!/usr/bin/env python
# coding: utf-8

# #### Geometric Shapes----------------------------------------------------:

# In[1]:


print('  Geometric Shapes: ')
print(' A_Circle: \n B_Square: \n C_Rectangle: \n D_Triangle: \n E_Parallelogram: \n F_Rhombus: \n G_Trapezoid: ')
Choice = str(input('Enter Your Choise: \n'))

##### Circle ----------------------------------:
if Choice=='A' or Choice=='a':
    print('Hi, I’m Circle ^_^')
    PA1=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA1 == 1:
        print('Perimeter of Circle: ')
        R = float(input('input the radius of a circle: '))
        def Perimeter(R):
            per_Circle=2*math.pi*R
            return (per_Circle)
        print(f'Perimeter of Circle = 2*π*r: {(Perimeter(R))}')  
    elif PA1 == 2:
        print('Area of Circle: ')
        R = float(input('input the radius of a circle: '))
        def Area(R):
            Area_Circle=math.pi*R**2
            return (Area_Circle)
        print(f'Area of Circle = π*r*r: {(Area(R))}')
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('1')

##### Square ------------------------------------:
elif Choice=='B' or Choice=='b':
    print('Hi, I’m Square ^_^')
    PA2=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA2 == 1:
        print('Perimeter of Square: ')
        Side = float(input('input the Side of a Square: '))
        def Perimeter(Side):
            per_Square=4*Side
            return (per_Square)
        print(f'Perimeter of Square = 4*Side: {Perimeter(Side)}')
    elif PA2 == 2:
        print('Area of Square: ')
        Side = float(input('input the Side of a Square: '))
        def Area(Side):
            Area_Square=Side**2
            return (Area_Square)
        print(f'Area of Square = Side*Side: {Area(Side)}')
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('2')

##### Rectangle ----------------------------------:
elif Choice=='C' or Choice=='c':
    print('Hi, I’m Rectangle ^_^')
    PA3=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA3 == 1:
        print('Perimeter of Rectangle: ')
        Length = float(input('input the Length of a Rectangle: '))
        Width = float(input('input the Width of a Rectangle: '))
        def Perimeter(Length,Width):
            per_Rectangle=2*(Length+Width)
            return (per_Rectangle)
        print(f'Perimeter of Rectangle = 2*(Length+Width): {Perimeter(Length,Width)}')
    elif PA3 == 2:
        print('Area of Rectangle: ')
        Length = float(input('input the Length of a Rectangle: '))
        Width = float(input('input the Width of a Rectangle: '))
        def Area(Length,Width):
            Area_Rectangle=Length*Width
            return (Area_Rectangle)
        print(f'Area of Rectangle = Length*Width: {Area(Length,Width)}')
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('3')

##### Triangle ----------------------------------:
elif Choice=='D' or Choice=='d':
    print('Hi, I’m Triangle ^_^')
    PA4=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA4 == 1:
        print('PerChoice==dimeter of Triangle: ')
        Side1 = float(input('input the Side1 of a Triangle: '))
        Side2 = float(input('input the Side2 of a Triangle: '))
        Side3 = float(input('input the Side3 of a Triangle: '))
        def Perimeter(Side1,Side2,Side3):
            per_Triangle=Side1+Side2+Side3
            return (per_Triangle)
        print(f'Perimeter of Triangle = Side1+Side2+Side3: {Perimeter(Side1,Side2,Side3)}')
    elif PA4 == 2:
        print('Area of Triangle: ')
        Height = float(input('input the Height of a Triangle: '))
        Base = float(input('input the Base of a Triangle: '))
        def Area(Height,Base):
            Area_Triangle=(1/2)*(Height*Base)
            return (Area_Triangle)
        print(f'Area of Triangle = (1/2)*(Height*Base): {Area(Height,Base)}')    
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('4')

##### Paralllelogram ----------------------------------:
elif Choice=='E' or Choice=='e':
    print('Hi, I’m Parallelogram ^_^')
    PA5=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA5 == 1:
        print('Perimeter of Parallelogram: ')
        Side1 = float(input('input the Side1 of a Parallelogram: '))
        Side2 = float(input('input the Side2 Non-opposite Side1 of a Parallelogram: '))
        def Perimeter(Side1,Side2):
            per_Parallelogram=2*(Side1+Side2)
            return (per_Parallelogram)
        print(f'Perimeter of Parallelogram = 2*(Side1+Side2): {Perimeter(Side1,Side2)}')
    elif PA5 == 2:
        print('Area of Parallelogram: ')
        Height = float(input('input the Height of a Parallelogram: '))
        Base = float(input('input the Base of a Parallelogram: '))
        def Area(Height,Base):
            Area_Parallelogram=Height*Base
            return (Area_Parallelogram)
        print(f'Area of Parallelogram = Height*Base: {Area(Height,Base)}')
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('5')

##### Rhombus ------------------------------------:
elif Choice=='F' or Choice=='f':
    print('Hi, I’m Rhombus ^_^')
    PA2=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA2 == 1:
        print('Perimeter of Rhombus: ')
        Side = float(input('input the Side of a Rhombus: '))
        def Perimeter(Side):
            per_Rhombus=4*Side
            return (per_Rhombus)
        print(f'Perimeter of Rhombus = 4*Side: {Perimeter(Side)}')
    elif PA2 == 2:
        print('Area of Rhombus: ')
        diameter1 = float(input('input The first diameter1 of the rhombus: '))
        diameter2 = float(input('input The second diameter2 of the rhombus: '))
        def Area(diameter1,diameter2):
            Area_Rhombus=(1/2)*diameter1*diameter2
            return (Area_Rhombus)
        print(f'Area of Rhombus = (1/2)*diameter1*diameter2: {Area(diameter1,diameter2)}')
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('6')

##### Trapezoid ------------------------------------:
elif Choice=='G' or Choice=='g':
    print('Hi, I’m Trapezoid ^_^')
    PA2=int(input('what do you want? \n (1) Perimeter: \n (2) Area: \n'))
    if PA2 == 1:
        print('Perimeter of Trapezoid: ')
        Base1 = float(input('input The first Base1 of the Trapezoid: '))
        Base2 = float(input('input The second Base2 of the Trapezoid: '))
        Side1 = float(input('input The first Side1 of the Trapezoid: '))
        Side2 = float(input('input The second Side2 of the Trapezoid: '))
        def Perimeter(Base1,Base2,Side1,Side2):
            per_Trapezoid=Base1+Base2+Side1+Side2
            return (per_Trapezoid)
        print(f'Perimeter of Trapezoid = Base1+Base2+Side1+Side2: {Perimeter(Base1,Base2,Side1,Side2)}')
        ########========================================================
    elif PA2 == 2:
        Angled=str(input('Is the Trapezoid right-angled? \n Yes: \n No: \n'))
        if Angled=='Yes' or Angled=='yEs' or Angled=='yeS' or Angled=='YES' or Angled=='yes':
            print('Area of Trapezoid right-angled: ')
            Length = float(input('input the Length of a Rectangle: '))
            Width = float(input('input the Width of a Rectangle: '))
            Height = float(input('input the Height of a Triangle: '))
            Base = float(input('input the Base of a Triangle: '))
            def Area(Length,Width,Height,Base):
                Area_Trapezoid_right_angled=(Length*Width)+((1/2)*Base*Height)
                return (Area_Trapezoid_right_angled)
            print(f'Area of Trapezoid right-angled = (Length*Width)+((1/2)*Base*Height): {Area(Length,Width,Height,Base)}')
        elif Angled=='No' or Angled=='no' or Angled=='nO' or Angled=='NO':
            print('Area of Trapezoid: ')
            Height = float(input('input The Height of the Trapezoid: '))
            Base1 = float(input('input The first Base1 of the Trapezoid: '))
            Base2 = float(input('input The second Base2 of the Trapezoid: '))
            def Area(Height,Base1,Base2):
                Area_Trapezoid=Height*((1/2)*(Base1+Base2))
                return (Area_Trapezoid)
            print(f'Area of Trapezoid = Height*((1/2)*(Base1+Base2)): {Area(Height,Base1,Base2)}')
        else:
            print('Wrong in Write $_$ ')
    else:
        print('I’m Sorry, You chose a Mistake! *_*')
#     print('7')


else:
    print('Error in The Choice!')
    


# In[ ]:




