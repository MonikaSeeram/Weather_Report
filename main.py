from output import print # importing print function from output module
from GeneratingReport import main # importing main function


#Iterating and calling the main function which was imported from GeneratingReport module
choice = True
while (choice):
    main()
    choice = input("Do you want to search for weather of another location [yes/no]:").lower()
    if choice == 'yes':
        choice = True
    elif choice == 'no':
        choice = False

print() # calling the function to display the report on word document