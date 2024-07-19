# This project aims at
#  i) simple input to get a data from user-preferably an employee/student  , view and  information 
#  ii) 
#  iii)

# from datetime import date, datetime
def close():
    pass


dct = {'ec114': 'nithin', 'ec115': 'muthu', 'ec116': 'nak', 'ec117': 'naveen', 'ec118': 'kumar'}
num_tpl = ('ec114','ec115','ec116','ec117','ec118')
class whattodo:
    no_attempts = 0
    
    def option() :
        if whattodo.no_attempts < 3:
            whattodo.no_attempts += 1 
            print('E - Exit current menu')
            print('U - Update any value')
            print('H - Goto home')
            print('D - Display current values')
            print('Enter the prompt')
            opt = input()
            opt = opt.upper()
            print(opt)
            print(f'Proceed with {opt} ? y - yes or n - -no')
            o = input()
            if o == 'Y' or o == 'y' :
                print('Now moving to ', opt)
                return opt 
            else:
                return whattodo.option()

        else:
            print('Too many attepts.4 ')
            print('Please retry')
            return None
            
            no_attempts = 0
        
    opt = classmethod(option)

class Details:
    student = ()
    name = None
    rollnum = None
    dob = None
    dept = None
    cgpa = None

    def __init__(self, name, roll, dob, dept, cgpa):
        self.name = name
        self.rollnum = roll
        self.dob = dob
        self.dept = dept
        self.cgpa = cgpa
        # self.age = get time - dob


    def addtodata(self):
        # self.student += list(self.name, self.rollnum, self.dept, self.dob)
        print(self.name, self.rollnum, self.dept, self.dob)
    

    def adduser(t0):
                      #t0 - rollnumber
        l_temp = []
        print('Enter name ,dept , dob ,cgpa')
        t1 = input()  #name
        t2 = input()  #dept
        t3 = input()  #dob
        t4 = input()        
        dct[t0] = t1
        l_temp = l_temp + list(t0) + list(t1) + list(t2) + list(t3) + list(t4)
        

        
        Details.student += tuple(l_temp)

    def __repr__(self):
        return Details.student
    

    new = classmethod(adduser)

class Login():

    student = ()
    name = None
    rollnum = None
    dob = None
    dept = None
    cgpa = None

    def login(self):
        print('Login Succesful')


def start(key):
    if key in num_tpl:
        print('Logging in', end=" ")
        print(dct[key])
        o = Login()
        o.login()
        choice = whattodo.option()
        
    else:
        print('No such user. Continue as new user ?')
        print(f'y - yes or n - -no')
        decision = input()
        decision = decision.lower()
        if decision=='y':
            print(f"Adding {key} as a new user")
            Details.adduser(key)


    
            


print('Enter any value to begin')
i = input()
print('Roll Num')
key = input()
start(key)



print()
print('*  *  *  * End of program *  *  *  * *  ')
print()


