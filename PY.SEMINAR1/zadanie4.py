# программа, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y)

a = int(input("Введите номер четверти: "))
if a ==1 :
    print ("x = {0.1; 100},  y = {0.1;100}" )
else :
    if a == 2 :
        print ("x = {0.1; 100},  y = {-0.1;-100}" )
    else :
        if a == 3 :
            print ("x = {-0.1; -100},  y = {-0.1;-100}" )
        else :
            if a == 4 :
                print ("x = {-0.1; -100},  y = {0.1;100}" )