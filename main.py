import os# To create a directory and to fetch the contents .
from generating_weatherReport import* # imports all from the generating_weatherReport module

#Iterating and calling the main function which was imported from generating_weatherReport module
choice = True
while (choice):
    main()
    choice = input("Do you want to search for weather of another location [yes/no]:").lower()
    if choice == 'yes':
        choice = True
    elif choice == 'no':
        choice = False

weather.add_run("\n--------------- Thanks For Visiting 👋 ---------------")
File_name = input("Enter the file name: ")
doc.save(f'{File_name}.docx')  # saves the word document with output
os.system(f'{File_name}.docx')# it directly open the document
