class SBI:
    __AccountNumber__ = 2456712345213 #--> Bank should set this
    __pin__ = 1234
    __Mobile__ = 9876543210
    __OTP__ = 648198
    __Balance__ = 0.0

    def Deposit(self,bal):
        self.__Balance__ += bal

    def Withdrawl(self,bal1):
        self.__Balance__ -= bal1

    def DisplayBalance(self):
        return self.__Balance__

    def userOTP(self):
        return self.__OTP__

    def userACCOUNTNUMBER(self):
        return self.__AccountNumber__

    def userMobile(self):
        return self.__Mobile__

    def USERPIN(self):
        return self.__pin__


sbi = SBI()

userPin = int(input("Please enter your pin : "))

print("------------------------------------------------")

if userPin == sbi.USERPIN():
    print("------------------------------------------------")
    print(f"Welcome {sbi.userACCOUNTNUMBER()} please proceed -->")
    print("------------------------------------------------")
    # --> Infinite while loop

    while True: # --> Infinite loop
        print("------------------------------------------------")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Display Balance")
        print("4. Diplay user pin")
        print("5. Update user pin")
        print("6. Exit")
        print("------------------------------------------------")
        choice = int(input("Please enter your choice : "))
        sbi.__OTP__ += 20 # --> Mocroservice
        print("------------------------------------------------")
        match(choice): # --> when python 3.10 was updated
            case 1:
                print("------------------------------------------------")
                Dbal = float(input("Enter amount to deposit : "))
                print("------------------------------------------------")
                sbi.Deposit(Dbal)
                print("--- Deposit sucess ---")
                print("------------------------------------------------")

            case 2:
                Wbal = float(input("Enter amount to withdrawl : "))
                if Wbal > sbi.DisplayBalance():
                    print("------------------------------------------------")
                    print("--- Insufficient Funds ---")
                else:
                    sbi.Withdrawl(Wbal)
                    print("--- Withdrawl success ---")
                    print("------------------------------------------------")

            case 3:
                print("------------------------------------------------")
                print("Available Balance : ", sbi.DisplayBalance())
                print("------------------------------------------------")

            case 4:
                print("------------------------------------------------")
                user_Mob = int(input("Enter your mobile number : "))
                print("------------------------------------------------")
                if user_Mob == sbi.userMobile():
                    print(f"--- Welcome {sbi.userACCOUNTNUMBER()} please preceed with OTP will received at {sbi.userMobile()} number")
                    print("------------------------------------------------")
                    user_OTP = int(input(f"Enter OTP that received at {sbi.userMobile()} : "))
                    print("------------------------------------------------")
                    if user_OTP == sbi.userOTP():
                        print("------------------------------------------------")
                        print("--- OTP Varifaction successfull ---")
                        print("------------------------------------------------")
                        print("User pin : ", sbi.__pin__)
                        print("------------------------------------------------")
                    else:
                        print("Invalid OTP... please check your mobile number...")
                        print("------------------------------------------------")

                else:
                    print("Invalid mobile number... please try again...")
                    print("------------------------------------------------")

            case 5:
                print("Defect found... please fix it")

            case 6:
                print("------------------------------------------------")
                print("Logout ... visit again...")
                break




else:
    print("------------------------------------------------")
    print("--- Invalid Pin!!! please try again ... ---")
    print("------------------------------------------------")
