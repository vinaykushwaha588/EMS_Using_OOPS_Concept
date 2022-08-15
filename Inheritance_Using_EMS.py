### Globally variable Declarations here
# BLL START HERE
class EMP:
    list_emp=[]     #statically LIST Declaire Here
    def __init__(self):
        self.id=0
        self.name=""
        self.type=""
    def __str__(self):
        return "ID :{0},NAME :{1},TYPE :{2},".format(self.id,self.name,self.type)

# Define Here Static Variable 
    @staticmethod
    def get_employee_type_by_id(emp_id):
        for e in EMP.list_emp:
            if e.id == emp_id:
                return e.type
        return False

    def add(self):
        EMP.list_emp.append(self)
    
    def search(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.id=e.id
                self.name=e.name
                self.type=e.type
                return True
        return False

    def modify(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.id=self.id
                e.name=self.name
                e.type=self.type
                return True
        return False
    
    def delete(self,emp_id):
        for i in range(len(EMP.list_emp)):
            if EMP.list_emp[i].id==emp_id:
                EMP.list_emp.pop(i)
                return True
        return False
## DEFINE DIRECTOR CLASS 
class DIR(EMP):
    def __init__(self):
        super().__init__()
        self.dir_special=""
        self.share=''
    def __str__(self):
        return super().__str__()+"Dir_Special :{0},Share :{1}".format(self.dir_special,self.share)
    
    def add(self):
        return super().add()

    def search(self, emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.dir_special=e.dir_special
                self.share=e.share
                super().search(emp_id)
                return True
        return False

    def modify(self, emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.dir_special=self.dir_special
                e.share=self.share
                super().modify(emp_id)
                return True
        return False

    def delete(self, emp_id):
        return super().delete(emp_id)

# DEFINE HERE MANAGER CLASS
class MGR(EMP):
    def __init__(self):
        super().__init__()
        self.mgr_special=""
        self.incentive=""

    def __str__(self):
        return super().__str__()+"MANAGER_SPECIAL :{0},INCENTIVE :{1}".format(self.mgr_special,self.incentive)

    def add(self):
        return super().add()

    def search(self, emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.mgr_special=e.mgr_special
                self.incentive=e.incentive
                super().search(emp_id)
                return True
        return False

    def modify(self, emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.mgr_special=self.mgr_special
                e.incentive=self.incentive
                super().modify(emp_id)
                return True
        return False

    def delete(self, emp_id):
        return super().delete(emp_id)

# DEFINE HERE TECHNICAL TRAINER CLASS HERE
class TT(EMP):
    def __init__(self):
        super().__init__()
        self.tt_special=''
        self.salary=''

    def __str__(self):
        return super().__str__()+"TT_Special :{0},Salary :{1}".format(self.tt_special,self.salary)

    def add(self):
        return super().add()
    
    def search(self, emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.tt_special=e.tt_special
                self.salary=e.salary
                super().search(emp_id)
                return True
        return False

    def modify(self, emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.tt_special=self.tt_special
                e.salary=self.salary
                super().modify(emp_id)
                return True
        return False

    def delete(self, emp_id):
        return super().delete(emp_id)

## BLL ends Here

# Define Here Show_all
def show_all_emp():
    for e in EMP.list_emp:
        print(e)

### PLL start Here
print('#---------------------------------------------------------------------#')
print("$---------------:-EMPLOYEE MANAGEMENT SYSTEM-:------------------------$")
print('#---------------------------------------------------------------------#')
while(True):
    print('''
             1> Add_Employyee
             2> Search_Employee
             3> Modify_Employee
             4> Delete_Employee
             5> ShowAll_Employee
             0> Exit ''')
    ch=input("Enter Your Choice :")    
    if ch=="1":
        while(True):
            print("1.Add_Director\n2.Add_Manager\n3.Add_Technical Trainer\n0.Exit")
            ch1=input("Enter Your Choice :")
            if ch1=='1':
                print("--------- Director Details Added Here--------")
                ob_dir=DIR()
                ob_dir.type='DIR'
                ob_dir.id=int(input("Enter DIR ID :"))
                ob_dir.name=input("Enter DIR Name :")
                ob_dir.dir_special=input("Enter DIR Speciality :")
                ob_dir.share=input("Enter DIR Share :")
                ob_dir.add()
                print("Director Added Successfully......")
            elif ch1=='2':
                print("--------- Manager Details Added Here--------")
                ob_mgr=MGR()
                ob_mgr.type='MGR'
                ob_mgr.id=int(input("Enter MGR ID :"))
                ob_mgr.name=input("Enter MGR Name :")
                ob_mgr.mgr_special=input("Enter MGR Speciality :")
                ob_mgr.incentive=input("Enter MGR Incentive :")
                ob_mgr.add()
                print("Manager Added Successfully......")

            elif ch1=='3':
                print("--------- Technical Trainer Details Added Here--------")
                ob_tt=TT()
                ob_tt.type='TT'
                ob_tt.id=int(input("Enter TT ID :"))
                ob_tt.name=input("Enter TT Name :")
                ob_tt.tt_special=input("Enter TT Speciality :")
                ob_tt.salary=input("Enter TT Salary :")
                ob_tt.add()
                print("Technical Trainer Added Successfully......")
            elif ch1=='0':
                print("Exit EMP Addition Part.. ")
                break
            else:
                print("Enter Wrong choice....\n You can Try Again")
    elif ch=='2':
        # Define Here Search EMP
        id=int(input("Enter EMP Id :"))
        type=EMP.get_employee_type_by_id(id)
        if type=='DIR':
            ob_dir=DIR()
            ob_dir.search(id)
            print(ob_dir)
        elif type=='MGR':
            ob_mgr=MGR()
            ob_mgr.search(id)
            print(ob_mgr)
        elif type=='TT':
            ob_tt=TT()
            ob_tt.search(id)
            print(ob_tt)
    elif ch=='3':
        # Define Here Modify EMP
        emp_id=int(input("Enter EMP Id :"))
        type=EMP.get_employee_type_by_id(emp_id)
        if type=='DIR':
            ob_dir=DIR()
            ob_dir.type='DIR'
            ob_dir.name=input("Enter Director Updated Name :")
            ob_dir.dir_special=input("Enter Director Updated Special :")
            ob_dir.share=input("Enter Director Updated Share :")
            check=ob_dir.modify(emp_id)
            if check==False:
                print("Id not Found")
            else:
                print("Director Data Updated Successfully...")
        elif type=='MGR':
            ob_mgr=MGR()
            ob_mgr.type="MGR"
            ob_mgr.name=input("Enter Manager Updated Name :")
            ob_mgr.mgr_special=input("Enter Manager Updated Special :")
            ob_mgr.incentive=input("Enter Manager Updated Incentive :")
            check=ob_mgr.modify(emp_id)
            if check==False:
                print("Id not Found")
            else:
                print('Manager Data Updated Successfully..')
        elif type=='TT':
            ob_tt=TT()
            ob_tt.type='TT'
            ob_tt.name=input("Enter Technical Trainer Updated Name :")
            ob_tt.tt_special=input("Enter Technical Trainer Special Updated :")
            ob_tt.salary=input("Enter Technical Trainer Salary Updated :")
            check=ob_tt.modify(emp_id)
            if check==False:
                print("Id not Found")
            else:
                print("Technical Trained Data Updated Successfull...")

    elif ch=='4':
        # Define Here Delete EMP
        emp_id=int(input("Enter EMP Id :"))
        type=EMP.get_employee_type_by_id(emp_id)
        if type=='DIR':
            ob_dir=DIR()
            check=ob_dir.delete(emp_id)
            if check==False:
                print('Id not Found ')
            else:
                print("Director Data Deleted Successfully...")
        elif type=='MGR':
            ob_mgr=MGR()
            check=ob_mgr.delete(emp_id)
            if check==False:
                print('Id Not Found')
            else:
                print('Manager Data Deleted Successfully..')
        elif type=='TT':
            ob_tt=MGR()
            check=ob_tt.delete(emp_id)
            if check==False:
                print("Id not Found")
            else:
                print("Technical Trained Data Deleted Successfull...")
    elif ch=='5':
        # Define Here Show All
        print('---------------------------- Show_All_Employee Details ------------------------')
        show_all_emp()

    elif ch=='0':
        print("Successfully Exit.......")
        break
    else:
        print("Enter Wrong choice....\n You can Try Again")