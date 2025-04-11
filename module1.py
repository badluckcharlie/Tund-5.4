p=[]
i=[]
def Add_employee(p:list,i:list):
    """Функция для добавления работника и его зарплаты. Добавляет имя и зарплату в существующий список.
    :type: str name - имя работника
    :type: float salary - зарплата работника
    """
    while True:
        try:
            name=input("Name: ")
            if name.isalpha():
                try:
                    salary=float(input("Salary: "))
                except:
                    print("Only numbers!")
                p.append(salary)
                i.append(name)
                print(f"Data is added. Name is {name} and his salary is: {salary}$")
                break
        except:
            print("Only letters!")
    p.append(salary)
    i.append(name)

def Del_Employee(p:list,i:list):
     """Убрать работника из списка. Проверяет есть ли работник в списке и если есть удаляет
     :type: name - имя
     """
     try:
         name=input("Name: ")
         if name.isalpha():
            k=i.count(name)
            if k>0:
                for j in range(k):
                    ind=i.index(name)
                    i.pop(ind)
                    p.pop(ind)
                    print("Data is deleted")
            else:
                print("Error! Data is not existing")
     except:
         print("Type only letters")

def Top_Salary(p:list,i:list):
     """Shows top salary
     :type: float max - максимальная зарплата из списка
     :type: int k - подсчет из спискa
     """
     top=max(p)
     print(f"Suurem palk on {top}")
     k=p.count(top)
     ind=p.index(top)
     for j in range(k):
             ind=p.index(top, ind)
             print(f"Saab kätte {i[ind]}")
             ind=ind+1
def Lowest_Salary(p:list,i:list):
     """Shows lowest salary
     """
     minimum=min(p)
     print(f"Väiksem palk on {minimum}")
     k=p.count(minimum)
     ind=p.index(minimum)
     for j in range(k):
         ind=p.index(minimum, ind)
         print(f"Saab kätte {i[ind]}")
         ind=ind+1
def Sorteerimine(p:list,i:list)-> any:
    """Сортировка работников по зарплате, с выбором по возрастанию или убыванию
    :type: määramata tüüp v ввод пользователя < или >, выбор между возрастанием и убиыванием
    """
    v=input("Vali märk: > (Kasvav) või < (Kahanev): ")
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i
def same_salary(p: list, i: list):
    """Näita töötajad kellelt on võrdne palk
    :type: list salary map - создает список из зарплат
    :type: float salary - зарплата работника
    :type: bool found - найдены ли работники с одинаковой зарплатой
    """
    salary_map = {}
    for name, salary in zip(i, p):
        if salary not in salary_map:
            salary_map[salary] = []
        salary_map[salary].append(name)
    found = False
    for salary, names in salary_map.items():
        if len(names) > 1:
            found = True
            print(f"\nPalk: {salary}$ | Mittu töötajad: {len(names)}")
            print("Nimed: ", ", ".join(names))
    
    if not found:
        print("0 tootajad sama palkaga")

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

def tax(p: list, i: list):
    """Убирает 20% от зарплаты выбранного работника, чтобы узнать что он получит после налога
    :param idx - пронумерованный список работников
    :param int choice - пользователь выбирает кого-то из работников по номеру
    :param original_salary - изначальная зарплата работника
    :param taxl_salary - преобразование зарплаты с учетом налога в 20%
    :param list [choice] - временный список для работы с нашим работником
    """
    print("\nCurrent employees and salaries:")
    for idx, (name, salary) in enumerate(zip(i, p), 1):
        print(f"{idx}. {name}: {salary}$")
    
    try:
        choice = int(input("\n Valige töötaja: ")) - 1
        if 0 < choice < len(i):
            original_salary = p[choice]
            tax_salary = original_salary * 0.8 
            p[choice] = round(tax_salary, 2)
            
            print(f"\n Töötaja: {i[choice]}:")
            print(f"Ilma KMta: {original_salary}$")
            print(f"KMga: {p[choice]}$")
        else:
            print("Number puudub järjendis!")
    except ValueError:
        print("Viga!")

def N_Salary(p: list, i: list):
    """Shows people that are paid less and more than selected figure
    """
    try:
        salary = float(input("Enter salary to compare: "))
        less = []
        more = []
        for i in range(len(inimesed)):
             if palgad[i] < salary:
                less.append(inimesed[i])
             elif palgad[i] > salary:
                  more.append(inimesed[i])
        print("\nEmployees earning less:", ", ".join(less) if less else "None")
        print("Employees earning more:", ", ".join(more) if more else "None")  
    except ValueError:
        print("Please enter a valid number!")
 
def Bonus_Salary(p: list, i: list):
    """Своя функция по выбору. Добавляет прибавку к зарплате выбранному работнику, позволяя выбрать процент на какой зарплата увеличится
    :param int choice: выбор работника из существующих
    :param float bonus: выбор размера бонуса в процентах
    :param float bonus_to: нахождение доли для дальнейших рассчетов
    :param float bonus_salary: итоговая зарплата в которую включен бонус
    :param idx int: нумерованный список работников
    """
    for idx, (name, salary) in enumerate(zip(i, p), 1):
            print("\nCurrent employees and salaries:")
            print(f"{idx}. {name}: {salary}$")
    try:
        choice = int(input("Valige töötaja: ")) - 1
        bonus = float(input("Kirjutage mittu protsentis palk tõuseb: "))
        if 0 <= choice < len(i) and bonus > 0:
            original_salary = p[choice]
            bonus_to = bonus / 100
            bonus_salary = original_salary * bonus_to + original_salary
            print(f"New salary is: {bonus_salary}$")
        else:
            print("Valige eksisteeriv töötaja ja valige bonus rohkem kui 0")


    except:
        print("Error!")

def palgaotsing(p:list, i:list):
    """
    :param i: Inimiste nimekiri
    :param p: Palkade nimikiri
    :rtype:none
    """
    nimi=input("Sisesta nimi mida sa sooviks: ")
    leitud=False
    for j in range(len(i)):
        if i[j]==nimi:
            print(f"{nimi} palk on: {p[j]}")
    if leitud==False:
        print(f"{nimi} kohta andmeid ei leitud")
