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

#API.py

import json
import requests
import csv

class API:
    """Handles API calls, data parsing, and CSV writing."""

    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        """Fetches data from the API and returns it as a Python dictionary."""
        response = requests.get(self.url)
        json_string = response.content
        data = json.loads(json_string)
        return data

    def extract_data(self, data):
        """Extracts comic titles and counts character appearances."""
        extracted_data = []
        character_counts = {}

        # Loop through each comic item
        for item in data.get("data", {}).get("results", []):
            # Add the comic title
            title = item.get("title", "Unknown Title")
            extracted_data.append({"title": title})

            # Count each character's appearance
            for character in item.get("characters", {}).get("items", []):
                character_name = character.get("name", "Unknown Character")
                if character_name in character_counts:
                    character_counts[character_name] += 1
                else:
                    character_counts[character_name] = 1

        return extracted_data, character_counts



