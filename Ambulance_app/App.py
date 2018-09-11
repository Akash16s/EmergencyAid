from firebase import firebase

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
print(engaged_ambulance)
print(patient)
print(hospital_selected)
print(location)
