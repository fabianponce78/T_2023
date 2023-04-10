def password_f():
    i=0
    password=""
    while password != "PASSWORD":
        password = (input("Enter your password: "))
        i= i+1
        if i == 3:
            print("You entered the wrong password many times")
            exit()
        if password != "PASSWORD":
            print("You entered the wrong password")
        if password == "PASSWORD":
            print("Correct password")


def price_business (b):
    price = b * 60
    return price

def price_residential (a):
    price = a * 35
    return price

business_client = 0
residential_client = 0
revenue = 0

password_f()
while True:
    type_client= input("Enter your client type (residential or business): ")
    current_r = float(input("Enter your current reading: "))
    previous_r = float(input("Enter your previous reading: "))
    
    quantity = current_r - previous_r
    
    if type_client.lower() == "business":
        total_bill_business = (price_business(quantity))
        print(f"The KW consumed is {quantity} and the client has to pay ${total_bill_business} because of the 0% discount")
        
        business_client += 1
        renevue += total_bill_business
    
    else:
        #-----------------------------------------------------------------------------------------
        #type_client.lower() == "residential" and quantity <= previous_r and quantity < 800:
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
            print("Invalid type of client")
        #-----------------------------------------------------------------------------------------        
        print("1. Continue\n2. Stop")
        option = int(input("Choose an option: "))
        
        if option == 2:
            print(f"The number of business clients were {business_client}")
            print(f"The number of residential clients were {residential_client}")
            print(f"The total revenue combined of both types of clients is ${revenue}")
            break