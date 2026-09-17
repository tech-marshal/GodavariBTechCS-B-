pin = 1234
balance = 0.0
otp = 4500
mobile = 9876543210

userPin = int(input("Enter your PIN : "))
if pin == userPin:
    print("----------------------------------")
    print("--- Login success ---")
    print("----------------------------------")
    while True: # --> infinite while loop(always runnable)
        print("----------------------------------")
        print("--- ATM ---")
        print("----------------------------------")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Check Balance")
        print("4. Display user pin")
        print("5. change user pin : ")
        print("6. exit")
        print("----------------------------------")
        ch = int(input("Enter choice : "))
        otp = otp + 5 # microservice

        print("----------------------------------")
        match(ch):
            case 1:
                bal = float(input("Enter amount : "))
                balance = balance + bal
                print("----------------------------------")
                print("--- Deposit success ---")
                print("----------------------------------")

            case 2:
                balw = float(input("Enter amount to withdrawl : "))
                if balw > balance:
                    print("insufficient funda...")
                    print("----------------------------------")
                else:
                    balance = balance - balw
                    print("--- Withdrawl success ---")
                    print("----------------------------------")
            case 3:
                print("Available balance : ", balance)
                print("----------------------------------")

            case 4:
                uPin = int(input("Enter your pin : "))
                if uPin == pin:
                    print("--- Pin matched ---")
                    print("user pin : ",pin)
                    print("----------------------------------")
                else:
                    print("--- invalid pin pls try again ---")
                    print("----------------------------------")

            case 5:
                usPin = int(input("Enter old pin : "))
                if usPin == pin:
                    print("--- pin matched success ---")
                    print("----------------------------------")
                    userMob = int(input("Enter your mobile number : "))
                    if userMob == mobile:
                        print("--- Mobile number matched ---")
                        print("----------------------------------")
                        userOTP = int(input(f"Enter otp received at {mobile} .. enter  : "))
                        if userOTP == otp:
                            print("OTP varificarion success")
                            print("----------------------------------")
                            newPin = int(input("Enter new pin : "))
                            pin = newPin
                            print("--- Pin update success ---")
                        else:
                            print("invalid otp please try again...")
                            print("----------------------------------")

                else:
                    print("--- invalid pin ---")
                    print("----------------------------------")

            case 6:
                print("logout... please visit again!!!")
                break


else:
    print("invalid pin... please try again!!!")pin = 1234
balance = 0.0
otp = 4500
mobile = 9876543210

userPin = int(input("Enter your PIN : "))
if pin == userPin:
    print("----------------------------------")
    print("--- Login success ---")
    print("----------------------------------")
    while True: # --> infinite while loop(always runnable)
        print("----------------------------------")
        print("--- ATM ---")
        print("----------------------------------")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Check Balance")
        print("4. Display user pin")
        print("5. change user pin : ")
        print("6. exit")
        print("----------------------------------")
        ch = int(input("Enter choice : "))
        otp = otp + 5 # microservice

        print("----------------------------------")
        match(ch):
            case 1:
                bal = float(input("Enter amount : "))
                balance = balance + bal
                print("----------------------------------")
                print("--- Deposit success ---")
                print("----------------------------------")

            case 2:
                balw = float(input("Enter amount to withdrawl : "))
                if balw > balance:
                    print("insufficient funda...")
                    print("----------------------------------")
                else:
                    balance = balance - balw
                    print("--- Withdrawl success ---")
                    print("----------------------------------")
            case 3:
                print("Available balance : ", balance)
                print("----------------------------------")

            case 4:
                uPin = int(input("Enter your pin : "))
                if uPin == pin:
                    print("--- Pin matched ---")
                    print("user pin : ",pin)
                    print("----------------------------------")
                else:
                    print("--- invalid pin pls try again ---")
                    print("----------------------------------")

            case 5:
                usPin = int(input("Enter old pin : "))
                if usPin == pin:
                    print("--- pin matched success ---")
                    print("----------------------------------")
                    userMob = int(input("Enter your mobile number : "))
                    if userMob == mobile:
                        print("--- Mobile number matched ---")
                        print("----------------------------------")
                        userOTP = int(input(f"Enter otp received at {mobile} .. enter  : "))
                        if userOTP == otp:
                            print("OTP varificarion success")
                            print("----------------------------------")
                            newPin = int(input("Enter new pin : "))
                            pin = newPin
                            print("--- Pin update success ---")
                        else:
                            print("invalid otp please try again...")
                            print("----------------------------------")

                else:
                    print("--- invalid pin ---")
                    print("----------------------------------")

            case 6:
                print("logout... please visit again!!!")
                break


else:
    print("invalid pin... please try again!!!")
