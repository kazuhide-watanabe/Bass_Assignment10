#*********************************
# Name: Kazuhide Watanabe, Cheikh Abdoul
# email:  watanake@mail.uc.edu
#         abdoulch@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  11/14/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: Group project where we build a URL, receive results from a server, parse the results, and extract some interesting data.
# Brief Description of what this module does: In this module we created a class that includes functions to handle API calls, fetching data, and parsing character data.   
# Citations: In class notes, Bill Nicholson 
# Anything else that's relevant: This funtion was completed and troubleshooted by Cheikh and Kazu.
#**********************************

#API.py

import json
import requests

class API:
    """A class to handle API calls to fetch comic data and parse character appearances"""

    def __init__(self, url):
        """
        Initialize the API Class with a URL
        @param url String: API endpoint URL
        """
        self.url = url

    def fetchData(self):
        """
        Fetches data from the API and returns it as a Python dictionary
        @return dict: The JSON data from the API response as a dictionary
        """
        response = requests.get(self.url)
        json_string = response.content
        data = json.loads(json_string)
        return data

    def extractData(self, data):
        """
        Extracts comic titles and counts character appearances.
        @param data dict: The API data containing information on characters and about the comic
        @return list: A list containing comic titles
        @return dict: A dictionary with the key as the character name and the value as the number of appearances
        """
        extractedData = []
        characterCounts = {}

        # Looping through each comic item 
        for item in data.get("data", {}).get("results", []):
            # Adding the comic title
            title = item.get("title", "Unknown Title")
            extractedData.append({"title": title})

            # Counting the number of character appearances
            for character in item.get("characters", {}).get("items", []):
                characterName = character.get("name", "Unknown Character")
                if characterName in characterCounts:
                    characterCounts[characterName] += 1
                else:
                    characterCounts[characterName] = 1

        return extractedData, characterCounts



