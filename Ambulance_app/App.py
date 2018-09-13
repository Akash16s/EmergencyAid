from firebase import firebase
import  googlemaps
from datetime import datetime
import webbrowser


firebase = firebase.FirebaseApplication('https://emergencyhospital-c9f88.firebaseio.com', None)
result = firebase.get('/Management/Ambulance', None)


a1 = result["A1"]
a2 = result["A2"]
a3 = result["A3"]
a4 = result["A4"]
ambulance = [a1, a2, a3, a4]

for n in range(0, len(ambulance)):
    if(ambulance[n]["engaged"] == 1):
        print(ambulance[n])
        engaged_ambulance = ambulance[n]
        patient = ambulance[n]["user"]
        hospital_selected = ambulance[n]["hospital"]
        location = ambulance[n]["Location"]
        latitude = ambulance[n]["Location"]["Latitude"]
        longitude =  ambulance[n]["Location"]["Longitude"]

webbrowser.open('https://maps.google.com/?q=' + str(latitude) + str(longitude), new = 2)

