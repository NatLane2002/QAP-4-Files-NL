"""
Description: QAP 4 Python Program

Author: Nathaniel Lane
Date: March 16th, 2023
"""

#Comment like a pro

#Import datetime library
import datetime

#Import time library
import time

#Import format values module as FV
import FormatValues as FV

#Get current date
CurDate = datetime.date.today()

#Valid set of characters
ValidChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")

#Define a set of valid digits
ValidDig = set("1234567890")

#Create a list of valid Canadian provinces
CanadianProvinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

#Read data from the OSICDef.dat file (defaults file) 
f = open("OSICDef.dat", "r")

NEXT_POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PROCESSING_FEE = float(f.readline())

f.close()

#Get information from user and validate it

#Tell user what the program is
print()
print("=======================================")
print("----One Stop Insurance Company Form----")
print("=======================================")

#Put the program in a while loop so that it will continue to run over and over again
while True:
    #Customer's first name
    while True:
        print()
        CusFirstName = input("Customer's first name or enter 'END' (The program will not properly save if you don't exit the program from this input): ").title()
        if CusFirstName == 'End':
            break
        elif CusFirstName == '' or CusFirstName[0] == ' ':
            print()
            print("Must enter the customer's first name")
        elif set(CusFirstName).issubset(ValidChar):
            break
        else:
            print()
            print("Invalid characters - please reenter")

    if CusFirstName == 'End':
        break
        
    #Customer's last name
    while True:
        print()
        CusLastName = input("Customer's last name: ").title()
        if CusLastName == '' or CusLastName[0] == ' ':
            print()
            print("Must enter the customer's last name")
        elif set(CusLastName).issubset(ValidChar):
            break
        else:
            print()
            print("Invalid characters - please reenter")

    #Concatanate customer first and last name to create full name
    CusFullName = CusFirstName + ' ' + CusLastName

    #Customer's address
    while True:
        print()
        CusStrAdd = input("Customer's street address: ").title()
        if CusStrAdd == '' or CusStrAdd[0] == ' ':
            print()
            print("Must enter the customer's street address")
        else:
            break

    #Customer's city
    while True:
        print()
        CusCity = input("Customer's city: ").title()
        if CusCity == '' or CusCity[0] == ' ':
            print()
            print("Must enter the customer's current city of residence")
        elif set(CusCity).issubset(ValidChar):
            break
        else:
            print()
            print("Invalid characters - please reenter")

    #Customer's province
    while True:
        print()
        CusProv = input("Customer's province (Canadian): ").upper()
        if CusProv in CanadianProvinces:
            break
        else:
            print()
            print(f"{CusProv} is not a valid Canadian province - please reenter")

    #Customer's postal code
    while True:
        print()
        CusPosCode = input("Customer's postal code (A1A1A1): ").upper()
        if len(CusPosCode) != 6:
            print()
            print("Postal code must be 6 characters - please reenter")
        elif CusPosCode[0].isalpha() and CusPosCode[2].isalpha() and CusPosCode[4].isalpha() and CusPosCode[1].isdigit() and CusPosCode[3].isdigit() and CusPosCode[5].isdigit():
            break
        else:
            print()
            print("Invalid postal code, must be formatted (A1A1A1) - please reenter")

    #Customer's phone number
    while True:
        print()
        CusPhoneNum = input("Enter customer's phone number (9999999999): ")
        if len(CusPhoneNum) != 10:
            print()
            print("Phone number must be 10 digits - please reenter")
        elif set(CusPhoneNum).issubset(ValidDig) and len(CusPhoneNum) == 10:
            CusPhoneNum = (f"({CusPhoneNum[:3]}) {CusPhoneNum[3:6]}-{CusPhoneNum[6:]}") #Formats the phone number to make it look more realistic
            break
        else:
            print()
            print("Invalid phone number - please reenter")

    #Number of cars being insured
    while True:
        print()
        InsuredCarsNum = input("Number of cars being insured: ")
        try:
            InsuredCarsNum = int(InsuredCarsNum)
            if InsuredCarsNum < 1:
                print()
                print("Cannot enter a number less than 1 - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    #Options for extra liability
    while True:
        print()
        ExtraLiabilityOpt = input("Extra liability (Y / N): ").upper()
        if ExtraLiabilityOpt == 'Y':
            ExtraLiabilityCost = EXTRA_LIABILITY_COV * InsuredCarsNum
            break
        elif ExtraLiabilityOpt == 'N':
            ExtraLiabilityCost = 0
            break
        elif ExtraLiabilityOpt == '' or ExtraLiabilityOpt[0] == ' ':
            print()
            print("Must choose an option")
        else:
            print()
            print("Invalid option - please reenter")

    #Optional glass coverage
    while True:
        print()
        GlassCovOpt = input("Glass coverage (Y / N): ").upper()
        if GlassCovOpt == 'Y':
            GlassCovCost = GLASS_COV * InsuredCarsNum
            break
        elif GlassCovOpt == 'N':
            GlassCovCost = 0
            break
        elif GlassCovOpt == '' or GlassCovOpt[0] == ' ':
            print()
            print("Must choose an option")
        else:
            print()
            print("Invalid option - please reenter")

    #Optional loaner car
    while True:
        print()
        LoanerCarOpt = input("Loaner car (Y / N): ").upper()
        if LoanerCarOpt == 'Y':
            LoanerCarCost = LOANER_CAR_COV * InsuredCarsNum
            break
        elif LoanerCarOpt == 'N':
            LoanerCarCost = 0
            break
        elif LoanerCarOpt == '' or LoanerCarOpt[0] == ' ':
            print()
            print("Must choose an option")
        else:
            print()
            print("Invalid option - please reenter")

    #Options for ways to pay
    while True:
        print()
        PaymentOpt = input("Pay in full or monthly payments (F / M): ").upper()
        if PaymentOpt == 'F':
            break
        elif PaymentOpt == 'M':
            break
        elif PaymentOpt == '' or PaymentOpt[0] == ' ':
            print()
            print("Must choose an option")
        else:
            print()
            print("Invalid option - please reenter")

    #Calculations

    #Insurance premiums calculation
    InsurancePremiumCost = ((InsuredCarsNum - 1) * (BASIC_PREM * 0.75)) + BASIC_PREM

    #Total extra costs calculation
    TotalExtraCosts = ExtraLiabilityCost + GlassCovCost + LoanerCarCost

    #Total insurance premiums calculation
    InsurancePremiumTotal = InsurancePremiumCost + TotalExtraCosts

    #HST calculation
    HST = InsurancePremiumTotal * HST_RATE
    
    #Total cost calculation
    TotalCost = InsurancePremiumTotal + HST

    #Calculate the customer's payments
    TotalCostDsp = FV.FDollar2(TotalCost)
    if PaymentOpt == 'F':
        CusPayment = TotalCost
        NextPaymentDate = '       N/A'
    if PaymentOpt == 'M':
        CusPayment = (TotalCost + MONTHLY_PROCESSING_FEE) / 8
        #Calculate next payment date
        NextPaymentDate = datetime.date(CurDate.year, CurDate.month + 1, 1)

    #Create heading and footing
    Heading = ("One Stop Insurance Company")
    Footing = ("Thanks for your Business!")

    #Format all necessary values using the function 'FV'
    ExtraLiabilityCostDsp = FV.FDollar2(ExtraLiabilityCost)
    GlassCovCostDsp = FV.FDollar2(GlassCovCost)
    LoanerCarCostDsp = FV.FDollar2(LoanerCarCost)
    InsurancePremiumCostDsp = FV.FDollar2(InsurancePremiumCost)
    TotalExtraCostsDsp = FV.FDollar2(TotalExtraCosts)
    InsurancePremiumTotalDsp = FV.FDollar2(InsurancePremiumTotal)
    HSTDsp = FV.FDollar2(HST)
    CusPaymentDsp = FV.FDollar2(CusPayment)

    #Display all information to user
    print()
    print(f" ------------------------------------------")
    print(f"{Heading:^45s}")
    print(f" ------------------------------------------")
    print(f" Name:           {CusFullName:>25s}")
    print()
    print(f" Customer Address")
    print(f" ----------------                          ")
    print(f"                 {CusStrAdd:>25s}          ")
    print(f"          {CusCity:>20s}, {CusProv:>2s}, {CusPosCode:>6s}")
    print(f" ------------------------------------------")
    print(f" Phone Number:             {CusPhoneNum:>15s}  ")
    print(f" Insured Cars:             {InsuredCarsNum:>15d}             ")
    print()
    print(f" Customer Options                    Costs")
    print(f" ----------------                    -----")
    print(f" Extra Liability: {ExtraLiabilityOpt:>1s}, {ExtraLiabilityCostDsp:>21}")
    print(f" Glass Coverage:  {GlassCovOpt:>1s}, {GlassCovCostDsp:>21}")
    print(f" Loaner Coverage: {LoanerCarOpt:>1s}, {LoanerCarCostDsp:>21}")
    print()
    print(f" Customer Costs")
    print(f" --------------                            ")
    print(f" Insurance Premium:        {InsurancePremiumCostDsp:>15}")
    print(f" Total Extra Costs:        {TotalExtraCostsDsp:>15}")
    print(f" Insurance Premiums Total: {InsurancePremiumTotalDsp:>15}")
    print(f" HST:                      {HSTDsp:>15}")
    print(f" ------------------------------------------")
    print(f" Total Cost:               {TotalCostDsp:>15} ")
    print(f" ------------------------------------------")
    print(f" Payment Plan: {PaymentOpt}, {CusPaymentDsp:>24}")
    print(f" Next Payment Date:             {NextPaymentDate}")
    print(f" ------------------------------------------")
    print(f"{Footing:^45s}")
    print(f" ------------------------------------------")
    print()

    #Write all information to the file called 'Policies.dat'
    file = open("Policies.dat", "a")
    
    file.write("{}, ".format(str(NEXT_POL_NUM)))
    file.write("{}, ".format(str(CurDate)))
    file.write("{}, ".format(str(CusFirstName)))
    file.write("{}, ".format(str(CusLastName)))
    file.write("{}, ".format(str(CusStrAdd)))
    file.write("{}, ".format(str(CusCity)))
    file.write("{}, ".format(str(CusProv)))
    file.write("{}, ".format(str(CusPosCode)))
    file.write("{}, ".format(str(CusPhoneNum)))
    file.write("{}, ".format(str(InsuredCarsNum)))
    file.write("{}, ".format(str(ExtraLiabilityOpt)))
    file.write("{}, ".format(str(GlassCovOpt)))
    file.write("{}, ".format(str(LoanerCarOpt)))
    file.write("{}, ".format(str(PaymentOpt)))
    file.write("{}\n".format(str(TotalCostDsp)))

    file.close()

    #Increment the policy number by 1
    NEXT_POL_NUM += 1

#Outside of the program loop

#Update the defaults file with the new values
f = open("OSICDef.dat", "w")

f.write("{}\n".format(str(NEXT_POL_NUM)))
f.write("{}\n".format(str(BASIC_PREM)))
f.write("{}\n".format(str(ADD_CAR_DISCOUNT)))
f.write("{}\n".format(str(EXTRA_LIABILITY_COV)))
f.write("{}\n".format(str(GLASS_COV)))
f.write("{}\n".format(str(LOANER_CAR_COV)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(MONTHLY_PROCESSING_FEE)))

f.close()

#Give the user a message that the program is saved successfully
print()
print("Saving information...")
time.sleep(2)
print()
print("Policy information processed and saved.")
print()
exit()