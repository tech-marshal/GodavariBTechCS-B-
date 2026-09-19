"' --- Students records --- '"

class Student:
    firstName = ""
    lastName = ""
    branch = ""
    email = ""
    password = "123"

    def signUP(self):
        print("--- Enter details ---")
        print("-------------------------------------")
        fn = input("Enterv your first name : ")
        self.firstName = fn
        print("-------------------------------------")
        ln = input("Enter your last name : ")
        self.lastName = ln
        print("-------------------------------------")
        br = input("Enter your branch : ")
        self.branch = br
        print("-------------------------------------")
        em = input("Enter your email : ")
        self.email = em
        print("-------------------------------------")
        pswd=input("create password : ")
        self.password = pswdd
        print("-------------------------------------")
        print("--- Accoun created ----")
        print("-------------------------------------")

    def Login(self):
        em = input("Please enter your email(ID) : ")
        print("-------------------------------------")
        if self.email == em:
            print("--- Email matched success ---")
            print("-------------------------------------")
            pswd = input("Please enter your password : ")
            print("-------------------------------------")
            if self.password == pswd:
                print("--- Login Success ---")
                print("-------------------------------------")
            else:
                print("-------------------------------------")
                print("--- Invalid credentials ---")
                print("-------------------------------------")
        else:
            print("Invalid email ID... please try agaian!!!")
            print("-------------------------------------")

    def displayRecord(self):
        print("-------------------------------------")
        print("--- Student record ---")
        print("-------------------------------------")
        print("Student first name : ",self.firstName)
        print("Student last name : ", self.lastName)
        print("student branch : ". self.branch)
        print("-------------------------------------")

s = Student()

while True: # --> infinite while loop
    print("-------------------------------------")
    print("--- Student portal ---")
    print("-------------------------------------")
    print("1. SignUp")
    print("2. Login")
    print("3. Student Information")
    print("4. Logout")
    print("-------------------------------------")
    ch = int(input("Enter your choice : "))
    print("-------------------------------------")
    match(ch):
        case 1:
            s.signUP()
        case 2:
            if s.firstName == None:
                print("Please create account first...")
            else:
                s.Login()

        case 3:
            s.displayRecord()

        case 4:
            print("-------------------------------------")
            print(f"Logout success... hey {s.firstName} please visit agaian")
            braak
