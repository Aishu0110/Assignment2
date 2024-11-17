def split_bill():
    print("Welcome To The Split wise calculator")
    
    tot_bill = float(input("What is the total bill : "))
    percent_tip = int(input("What % tip would you like to give : "))
    no_of_ppl = int(input("How many people are splitting the bill : "))

    if tot_bill < 0 or percent_tip < 0 or no_of_ppl <= 0:
        print("Please enter positive values for the bill, tip, and number of people.")
        return
    
    tip_amount = "%.2f" % (percent_tip / 100 * tot_bill)
    total_bill_with_tip = tot_bill + float(tip_amount)
    payment_per_person = "%.2f" % (total_bill_with_tip / no_of_ppl)
    
    print(f"Tip amount: ${tip_amount}")
    print(f"Total bill including tip: ${total_bill_with_tip:.2f}")
    print(f"Each person owes: ${payment_per_person}")

split_bill() 
