import googlemaps
import json
import pprint
import xlsxwriter
import time

# MY API KEY
api = # your api key here

# Define the Client
gmaps = googlemaps.Client(key=api)

# Doing a simple nearby search where we specify the location. I am searching resuturant in CP delhi
# and scrapping details and reviews from it.
# in latitude/longitude format, along with a radius measured in meters
places_result = gmaps.places_nearby(location='28.633146,77.217429', radius=50, open_now=False, type='restaurant')

# wait for moving next page
time.sleep(3)

# PLace results with next page
place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])


# Fields want to get
fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']

# Now using loop to get rach place id from place results and scrap all details in it.

for place in places_result['results']:

    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = place['place_id']

    # define the fields you would liked return. Formatted as a list.
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']

    # make a request for the details.
    details = gmaps.place(place_id=my_place_id, fields=fields)
    try:
        website = details['result']['website']
    except KeyError:
        website = ""

    try:
        name = details['result']['name']
    except KeyError:
        name = ""

    try:
        address = details['result']['formatted_address']
    except KeyError:
        address = ""

    try:
        phone_number = details['result']['international_phone_number']
    except KeyError:
        phone_number = ""

    try:
        reviews = details['result']['reviews']
    except KeyError:
        reviews = []
    print("===================PLACE===================")
    print("Name:", name)
    print("Website:", website)
    print("Address:", address)
    print("Phone Number", phone_number)
    print("==================REVIEWS==================")
    for review in reviews:
        author_name = review['author_name']
        rating = review['rating']
        text = review['text']
        time = review['relative_time_description']
        profile_photo = review['profile_photo_url']
        print("Author Name:", author_name)
        print("Rating:", rating)
        print("Text:", text)
        print("Time:", time)
        print("Profile photo:", profile_photo)
        print("-----------------------------------------")

