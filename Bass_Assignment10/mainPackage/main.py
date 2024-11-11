#*********************************
# Name: Kazuhide Watanabe, Cheikh Abdoul
# email:  watanake@mail.uc.edu
#         abdoulch@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  11/07/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: Group project where we build a URL, receive results from a server, parse the results, and extract some data.
# Brief Description of what this module does:   
# Citations: In class notes, Bill Nicholson 
# Anything else that's relevant: This funtion was completed and troubleshooted by Cheikh and Kazu.
#**********************************

# main.py

from APIPackage.API import*

if __name__ == "__main__":
    # Set the API URL
    url = 'http://gateway.marvel.com/v1/public/comics?ts=1&apikey=852bbd6c4a0be23725334834ddd7a9d1&hash=9806a1850d28d061c97b858e691cad1e'
    api = API(url)

    # Fetch data from the API
    data = api.fetch_data()

    # Extract relevant data: comic titles and character counts
    extracted_data, character_counts = api.extract_data(data)

    # Print extracted comic titles
    print("Comic Titles:")
    for item in extracted_data:
        print(item["title"])

    # Print character counts
    print("\nCharacter Counts:")
    for character, count in character_counts.items():
        print(f"{character}: {count}")




