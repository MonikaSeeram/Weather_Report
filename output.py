from scraping_weatherReport import*
import os


#defining the function to display the output in word document
def display():
    weather.add_run("\n--------------- Thanks For Visiting 👋 ---------------")
    File_name = input("Enter the file name: ")
    doc.save(f'{File_name}.docx')  # saves the word document with output
    os.system(f'{File_name}.docx')# it directly open the document
