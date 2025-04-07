p=[]
i=[]
def Add_employee(p:list,i:list):
    """Функция для добавления работника и его зарплаты
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
     """Del emp
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
    """
    """
    v=input("Vali märk: > (Kasvav) või < (Kahanev)")
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i
def same_salary(p: list, i: list):
    """Näita töötajad kellelt on võrdne palk
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
        print("0")

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

def tax(p: list, i: list):
    """Reduce selected employee's salary by 20%"""
    print("\nCurrent employees and salaries:")
    for idx, (name, salary) in enumerate(zip(i, p), 1):
        print(f"{idx}. {name}: {salary}$")
    
    try:
        choice = int(input("\n Valige töötaja (1-5): ")) - 1
        if 0 <= choice < len(i):
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
    choice = int(input)
    