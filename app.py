from donations_pkg import homepage
from donations_pkg import user

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    homepage.show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    user_choice = input("Please choose an option: ")

    if user_choice == "1":
        username = input("\nPlease type your username: ")
        password = input("Please type your password: ")
        authorized_user = user.login(database, username, password)
        
    
    elif user_choice == "2":
        username = input("\nPlease register your username: ")
        password = input("Please create a password: ")
        authorized_user = user.register(database, username) 
       
        
        if authorized_user != "":
            database[username] = password 
       
    elif user_choice == "3":
        if authorized_user == "":
            print("\nYou are not logged in")
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)

    elif user_choice == "4":
        homepage.show_donations(donations)
    
    elif user_choice == "5":
        print("\nGoodbye")
        break
