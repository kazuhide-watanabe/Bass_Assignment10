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

class API(object):
    """description of class"""
    def APIDemo(self):
        response = requests.get('http://gateway.marvel.com/v1/public/comics?ts=1&apikey=852bbd6c4a0be23725334834ddd7a9d1&hash=9806a1850d28d061c97b858e691cad1e')
        json_string = response.content

        parsed_json = json.loads(json_string) # Now we have a python dictionary

        #print(parsed_json)
        #print(parsed_json['data'][0]['description'])
        #print(parsed_json['data'][0]['directionsInfo'])
    
        # total = int(parsed_json['total']) # The number of parks that were returned

        # for park in parsed_json['data']:
            # print(park['description'])
        print(parsed_json)

#import requests
import json


class API:
    """Handles API calls, data parsing, and CSV writing."""

    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        """Fetches data from the API and returns it as a Python dictionary."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error fetching data:" + e)
            return {}

    def extract_data(self, data):
        """Extracts and formats specific data from the JSON response."""
        extracted_data = []
        # Replace with actual field extraction based on the JSON structure
        for item in data.get("data", {}).get("results", []):
            extracted_data.append({
                "title": item.get("title"),
                "description": item.get("description", "No description available")
            })
        return extracted_data

    def write_to_csv(self, data, filename="output.csv"):
        """Writes extracted data to a CSV file."""
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "description"])
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print("Data written to " + filename)


