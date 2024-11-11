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

import json
import requests

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


