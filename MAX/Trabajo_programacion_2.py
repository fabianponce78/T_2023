
business_client = 0
residential_client = 0
revenue = 0



###-------------------------------------------------------------------
def password_f():
    i=0
    password=""
    while password != "PASSWORD":
        password = (input("Enter your password: "))        
        if password != "PASSWORD":
            i= i+1
            print("\tYou entered the wrong password")
        if password == "PASSWORD":
            print("\tCorrect password")        
        if i == 3:
            print("\tYou entered the wrong password many times")
            exit()


###-------------------------------------------------------------------
def price_business (b):
    price = b * 60
    return price
###-------------------------------------------------------------------
def price_residential (a):
    price = a * 35
    return price

###-------------------------------------------------------------------


###-------------------------------------------------------------------
password_f()
###-------------------------------------------------------------------
while True:
    type_client= input("Enter your client type (residential or business): ")
        
    if type_client.lower() == "business" or type_client.lower() == "residential":             
        current_r = float(input("\nEnter your current reading: "))
        previous_r = float(input("Enter your previous reading: "))        
        quantity = current_r - previous_r
        
        if type_client.lower() == "business":
            total_bill_business = (price_business(quantity))
            print(f"The KW consumed is {quantity} and the client has to pay ${total_bill_business} because of the 0% discount")
            
            business_client += 1
            revenue += total_bill_business
            print('revenue =' , revenue)
            
        else:
            residential_client += 1
            
            if quantity >= 0 and quantity <= 399:
                price = quantity * 35
                dis = price * .40
                total_price = price - dis
                print(f"The price is ${price} and the 40% discount is ${dis}, the final cost is ${total_price}")
                revenue += total_price
            
            elif quantity >= 400 and quantity <= 799:
                price = quantity * 35
                dis = price * .25
                total_price = price - dis
                print(f"The price is ${price} and the 25% discount is ${dis}, the final cost is ${total_price}")
                revenue += total_price
                           
            elif quantity >= 800:
                total_bill_residential = (price_residential(quantity))
                print(f"The KW consumed is {quantity} and the client has to pay ${total_bill_residential} because of the 0% discount")
                revenue += total_bill_residential
            
    else:
        print("Invalid type of client.")
        
                            
    print("\nChoose an option: ")
    option = int(input("\t1. Continue\n\t2. Stop"))
    
                                            
    if option == 2:
        print(f"\n")
        print(f"\t The number of business clients were: {business_client}")
        print(f"\t The number of residential clients were: {residential_client}")
        print(f"\t The total revenue combined of both types of clients is: ${revenue}")
        print(f"\n")
        break
    
        