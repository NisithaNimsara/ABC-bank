custnum_list=[ ]
accnum_list=[ ]
nic_list=[ ]
fname_list=[ ]
lname_list=[ ]
bdate_list=[ ]
padd_list=[ ]
phnum_list=[ ]
bbalance_list=[ ]
#----------------------------------------------------------------------------------------------------------------------
def customerinput ():               # -1- customer detail input function
    print(" ")
    print("                        ""ABC Bank")
    print("                   ""Add a new customer")
    print(" ")
    try:
        bnk_acc_num = int(input("Bank Account Number       - "))
        test = str(bnk_acc_num)
        if (len(test) == 10):
            nic = str(input("NIC                       - "))
            test = str(nic)
            if (len(test) == 10):
                f_name = input("First Name                - ")
                test = str(f_name)
                if (len(test) < 11):
                    l_name = input("Last Name                 - ")
                    test = str(l_name)
                    if (len(test) < 16):
                        birth_date = str(input("Birth Date                - "))
                        test = str(birth_date)
                        if (len(test) < 18):
                            pmnt_add = input("Permanent Address         - ")
                            test = str(pmnt_add)
                            if (len(test) < 16):
                                ph_num = str(input("Phone Number              - "))
                                test = str(ph_num)
                                if (len(test) == 10):
                                    bank_balance = float(0)
                                else:
                                    print("_________________________________________________________________________")
                                    print("Phone Number must be 10 Digit.")
                                    trycustomerin()
                            else:
                                print("_________________________________________________________________________")
                                print("Permanent Address maximum of 15 characters.")
                                trycustomerin()
                        else:
                            trycustomerin()
                    else:
                        print("_________________________________________________________________________")
                        print("Lasa Name maximum of 15 characters.")
                        trycustomerin()
                else:
                    print("_________________________________________________________________________")
                    print("First Name maximum of 10 characters.")
                    trycustomerin()
            else:
                print("_________________________________________________________________________")
                print("NIC must be 10 digits.")
                trycustomerin()
        else:
            print("_________________________________________________________________________")
            print("Account Number must be 10 digits.")
            trycustomerin()

        print(" ")
        answer = input("Do you want to save the account (Yes/No)? ").lower()
        print(" ")

        if (answer == str("yes")):
            cindex = len(custnum_list)
            if (cindex < 5):
                cust_count = 1
                accnum_list.append(bnk_acc_num)
                nic_list.append(nic)
                fname_list.append(f_name)
                lname_list.append(l_name)
                bdate_list.append(birth_date)
                padd_list.append(pmnt_add)
                phnum_list.append(ph_num)
                custnum_list.append(cust_count)
                bbalance_list.append(bank_balance)
                print("_________________________________________________________________________")
                print("       ""Account Added")
                print("_________________________________________________________________________")
                main()
            else:
                print("_________________________________________________________________________")
                print("Accounts Reach Maximum Amount ! ")
                print("_________________________________________________________________________")
                main()
        else:
            main()
            print(" ")
    except ValueError:
        print("_________________________________________________________________________")
        print("Something went wrong!.")
        print("_________________________________________________________________________")
        ansin = input("Do you want to Try Again (Yes/No)?")
        if (ansin == str("yes")):
            print("_________________________________________________________________________")
            customerinput()
        elif (ansin == str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            main()

# ----------------------------------SPECIAL FUNCTION FOR CUSTOMER INPUT-------------------------------------------------
def trycustomerin ():
    print(" ")
    print("You input WRONG charater count.")
    print("_________________________________________________________________________")
    ansinty = input("Do you want to Try Again (Yes/No)?").lower()
    if (ansinty == str("yes")):
        print("_________________________________________________________________________")
        customerinput()
    elif (ansinty == str("no")):
        print("_________________________________________________________________________")
        main()
    else:
        print("_________________________________________________________________________")
        main()

# ----------------------------------------------------------------------------------------------------------------------

def viewdetails ():                        # -2- view single customer detail function
    print(" ")
    print("                        ""ABC Bank")
    print("             ""View details of a customer ")
    print(" ")
    bnk_acc_num = int(input("Bank Account Number - "))
    print(" ")
    try:
        find_acc_num = accnum_list.index(bnk_acc_num)
        print("NIC                 - ", nic_list[find_acc_num])
        print("Phone Number        - ", phnum_list[find_acc_num])
        print("First Name          - ", fname_list[find_acc_num])
        print("Last Name           - ", lname_list[find_acc_num])
        print("Bank Balance        - ",'Rs.' ,bbalance_list[find_acc_num])
        print(" ")
        answer = input("Do you want to view another account details (Yes/No)? ").lower()
        if (answer == str("yes")):
            print("_________________________________________________________________________")
            viewdetails()

        elif (answer== str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            print("Invalid input. Please enter Yes or No.")
            print("_________________________________________________________________________")
            ansvdd = input("Do you want to Try Again (Yes/No)?").lower()
            if (ansvdd == str("yes")):
                print("_________________________________________________________________________")
                viewdetails()
            elif (ansvdd == str("no")):
                print("_________________________________________________________________________")
                main()
            else:
                print("_________________________________________________________________________")
                main()

    except ValueError:
        print("_________________________________________________________________________")
        print("Account number not found.")
        print("_________________________________________________________________________")
        ansvd = input("Do you want to Try Again (Yes/No)?").lower()
        if (ansvd == str("yes")):
            print("_________________________________________________________________________")
            viewdetails()
        elif (ansvd == str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            main()

def viewall ():                    # -3- View all customers details function
    print(" ")
    print("                        ""ABC Bank")
    print("             ""View Details of all the customers")
    print(" ")
    lindex = len(custnum_list)
    vd_count = 0
    while (vd_count < lindex):
        print("Account No.  -", accnum_list[vd_count])
        print("NIC          -", nic_list[vd_count])
        print("First Name   -", fname_list[vd_count])
        print("Last Name    -", lname_list[vd_count])
        print("Bank Balance -", 'Rs.', bbalance_list[vd_count])
        print(" ")
        vd_count = vd_count + 1
    answer = input("Do you want to update the account details (Yes/No)? ").lower()
    if (answer == 'yes'):
        print("_________________________________________________________________________")
        update()
    elif (answer == 'no'):
        print("_________________________________________________________________________")
        main()
    else:
        print("_________________________________________________________________________")
        print("Invalid Answer!!")
        print("_________________________________________________________________________")
        main()

def deposit ():                                # -4- Deposit function
    print(" ")
    print("                        ""ABC Bank")
    print("             ""Deposit Money to a given account")
    print(" ")
    try:
        deposit_num = int(input("Bank Account Number - "))
        print(" ")
        dep_amount = float(input("Deposit Amount      – "))
        print(" ")
        answer = input("Do you want to save (Yes/No)?").lower()
        if (answer == str("yes")):

            finddep_num = accnum_list.index(deposit_num)
            updated_damount = bbalance_list[finddep_num] + dep_amount
            bbalance_list[finddep_num] = updated_damount
            print("_________________________________________________________________________")
            print("       ""Your new balance - ", 'Rs.', bbalance_list[finddep_num])
            deposit_num = 0
            dep_amount = 0
            updated_damount = 0
            print("_________________________________________________________________________")
            main()
        elif (answer == str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            print("Invalid input. Please input Yes or No.")
            print("_________________________________________________________________________")
            ansdd = input("Do you want to Try Again (Yes/No)?").lower()
            if (ansdd == str("yes")):
                print("_________________________________________________________________________")
                deposit()
            elif (ansdd == str("no")):
                print("_________________________________________________________________________")
                main()
            else:
                print("_________________________________________________________________________")
                main()
    except ValueError:
        print("_________________________________________________________________________")
        print("Account number not found.")
        print("_________________________________________________________________________")
        ansd=input("Do you want to Try Again (Yes/No)?").lower()
        if (ansd == str("yes")):
            print("_________________________________________________________________________")
            deposit()
        elif (ansd == str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            main()

def withdraw():                                   # -5- Withdraw function
    print(" ")
    print("                        ""ABC Bank")
    print("             ""Withdraw money from a given account")
    print(" ")
    try:
        withdraw_num = int(input("Bank Account Number - "))
        print(" ")
        with_amount = float(input("Withdraw Amount     – "))
        print(" ")
        answer = input("Do you want to save (Yes/No)?").lower()
        if (answer == str("yes")):
            findwithd_num = accnum_list.index(withdraw_num)
            if (with_amount > bbalance_list[findwithd_num]):
                print("_________________________________________________________________________")
                print("       ""Insufficient Balance!!")
                print("_________________________________________________________________________")
                answw = input("Do you want to Try Again (Yes/No)?").lower()
                if (answw == str("yes")):
                    print("_________________________________________________________________________")
                    withdraw()
                elif (answw == str("no")):
                    print("_________________________________________________________________________")
                    main()
                else:
                    print("_________________________________________________________________________")
                    main()
            else:
                updated_wamount = bbalance_list[findwithd_num] - with_amount
                bbalance_list[findwithd_num] = updated_wamount
                print("_________________________________________________________________________")
                print("       ""Your new balance - ", 'Rs.', bbalance_list[findwithd_num])
                withdraw_num = 0
                with_amount = 0
                updated_wamount = 0
                print("_________________________________________________________________________")
                main()
        elif (answer == str("no")):
            print("_________________________________________________________________________")
            main()

        else:
            print("Invalid input. Please input Yes or No.")
            print("_________________________________________________________________________")
            answw = input("Do you want to Try Again (Yes/No)?").lower()
            if (answw == str("yes")):
                print("_________________________________________________________________________")
                withdraw()
            elif (answw == str("no")):
                print("_________________________________________________________________________")
                main()
            else:
                print("_________________________________________________________________________")
                main()

    except ValueError:
        print("_________________________________________________________________________")
        print("Account number not found.")
        print("_________________________________________________________________________")
        answ = input("Do you want to Try Again (Yes/No)?").lower()
        if (answ == str("yes")):
            print("_________________________________________________________________________")
            withdraw()
        elif (answ == str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            main()

def update ():                                  # -6- Details update function
    print(" ")
    print("                        ""ABC Bank")
    print("                 ""Update Customer Details")
    print(" ")
    try:
        bnk_acc_num = int(input("Bank Account Number    - "))
        test = str(bnk_acc_num)
        if (len(test) == 10):
            print(" ")
            find_acc_num = accnum_list.index(bnk_acc_num)
            n_nic = str(input("NIC                    - "))
            test = str(n_nic)
            if (len(test) == 10):
                n_f_name = input("First Name             - ")
                test = str(n_f_name)
                if (len(test) < 11):
                    n_l_name = input("Last Name              - ")
                    test = str(n_l_name)
                    if (len(test) < 16):
                        n_birth_date = str(input("Birth Date             - "))
                        test = str(n_birth_date)
                        if (len(test) < 18):
                            n_pmnt_add = input("Permanent Address      - ")
                            test = str(n_pmnt_add)
                            if (len(test) < 16):
                                n_ph_num = str(input("Phone Number           - "))
                                test = str(n_ph_num)
                                if (len(test) == 10):
                                    print(" ")
                                    answer = input("Do you want to save the new details (Yes/No)? ").lower()
                                else:
                                    print("_________________________________________________________________________")
                                    print("Phone Number must be 10 Digit.")
                                    trycustomerup()
                            else:
                                print("_________________________________________________________________________")
                                print("Permanent Address maximum of 15 characters.")
                                trycustomerup()
                        else:
                            trycustomerup()
                    else:
                        print("_________________________________________________________________________")
                        print("Last Name maximum of 15 characters.")
                        trycustomerup()
                else:
                    print("_________________________________________________________________________")
                    print("First Name maximum of 10 characters.")
                    trycustomerup()
            else:
                print("_________________________________________________________________________")
                print("NIC must be 10 Digit.")
                trycustomerup()
        else:
            print("_________________________________________________________________________")
            print("Bank Account number must be 10 Digit.")
            trycustomerup()

        if (answer == str("yes")):
            nic_list[find_acc_num] = n_nic
            fname_list[find_acc_num] = n_f_name
            lname_list[find_acc_num] = n_l_name
            bdate_list[find_acc_num] = n_birth_date
            padd_list[find_acc_num] = n_pmnt_add
            phnum_list[find_acc_num] = n_ph_num
            print("_________________________________________________________________________")
            print("       ""Account Updated")
            print("_________________________________________________________________________")
            main()
        elif answer == "no":
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            print("Invalid input. Please enter Yes or No.")
            print("_________________________________________________________________________")
            ansu = input("Do you want to Try Again (Yes/No)?").lower()
            if (ansu == str("yes")):
                print("_________________________________________________________________________")
                update()
            elif (ansu == str("no")):
                print("_________________________________________________________________________")
                main()
            else:
                print("_________________________________________________________________________")
                main()

    except ValueError:
        print("_________________________________________________________________________")
        print("something went wrong!!")
        print("_________________________________________________________________________")
        ansup = input("Do you want to Try Again (Yes/No)?").lower()
        if (ansup == str("yes")):
            print("_________________________________________________________________________")
            update()
        elif (ansup == str("no")):
            print("_________________________________________________________________________")
            main()
        else:
            print("_________________________________________________________________________")
            main()
        update()

# ----------------------------------SPECIAL FUNCTION FOR CUSTOMER detail update-----------------------------------------
def trycustomerup ():
    print(" ")
    print("You input WRONG charater count.")
    print("_________________________________________________________________________")
    ansupty = input("Do you want to Try Again (Yes/No)?").lower()
    if (ansupty == str("yes")):
        print("_________________________________________________________________________")
        update()
    elif (ansupty == str("no")):
        print("_________________________________________________________________________")
        main()
    else:
        print("_________________________________________________________________________")
        main()

#-----------------------------------------------------------------------------------------------------------------------

def main():                                       # main manu function
    try:
        print(" ")
        print("                        ""ABC Bank")
        print("                       ""Main Manu")
        print(" ")
        print("1) Add a new customer")
        print("2) View details of a customer including his/her bank balance")
        print("3) View details of all the customers with their bank balances")
        print("4) Deposit money to a given account")
        print("5) Withdraw money from a given account")
        print("6) Update Customer Details")
        print("7) Exit")
        print(" ")
        your_choice = int(input("                                            ""Your Choice : "))

        print("_________________________________________________________________________")

        # 1-add a new customer
        if (your_choice == 1):
            customerinput()

        # 2-View details of a customer including his/her bank balance
        elif (your_choice == 2):
            viewdetails()

        # 3-View details of all the customers with their bank balances
        elif (your_choice == 3):
            viewall()

        # 4-Deposit Money to a given account
        elif (your_choice == 4):
            deposit()

        # 5 -Withdraw money from a given account
        elif (your_choice == 5):
            withdraw()

        # 6-Update Customer Details
        elif (your_choice == 6):
            update()

        # 7 -Exit
        elif (your_choice == 7):
            print("Good Day!!!")
            print("_________________________________________________________________________")
            exit()

        # if more than 7
        elif (your_choice > 7):
            print("Out of choice range, Try again!!")
            print("_________________________________________________________________________")
            main()
        # if less than 1
        elif (your_choice < 1):
            print("Out of choice range, Try again!!")
            print("_________________________________________________________________________")
            main()
    except ValueError:
        print("_________________________________________________________________________")
        main()

main()
