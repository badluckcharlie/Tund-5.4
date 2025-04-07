
import module1
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
while True:
    print("\nCurrent Data:")
    print("Töötajad:", inimesed)
    print("Palgad:", palgad)
    
    print("\nValikud:")
    print("1 - Lisa töötaja")
    print("2 - Kustuta töötaja")
    print("3 - Näita kõrgest palk")
    print("4 - Näita väiksem palk")
    print("5 - Soorteri palgad")
    print("6 - Näita võrdsed palgad")
    print("0 - Exit")
    print("11 - Näita palg käibemaksuga")
    
    try:
        choice = int(input("Vali: "))
    except ValueError:
        print("Please enter a number!")
        continue
        
    if choice == 1:
        module1.Add_employee(palgad, inimesed)
    elif choice == 2:
        module1.Del_Employee(palgad, inimesed)
    elif choice == 3:
        module1.Top_Salary(palgad, inimesed)
    elif choice == 0:
        print("Exit")
        break
    elif choice == 5:
        module1.Sorteerimine(palgad, inimesed)
    elif choice== 4:
        module1.Lowest_Salary(palgad, inimesed)
    elif choice== 6:
        module1.same_salary(palgad, inimesed)
    elif choice== 11:
        module1.tax(palgad, inimesed)
    else:
        print("Error.")