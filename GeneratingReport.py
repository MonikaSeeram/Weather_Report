from scraping_weatherReport import web_scrap

# Defining the function for calling web_scrap function
def main():
    try:
        web_scrap() # calling the function to generating weather report of locations according to the user choice
        print("📡.....................")

    except:
        print("...oops🤭...")
        print("location not found ")


