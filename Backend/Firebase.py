from firebase import firebase
from math import radians, sin, cos, acos

usr_loc = {}
amb_loc = {}
hos_loc = {}

print('_____________________reading____________________')

firebase = firebase.FirebaseApplication('https://emergencyhospital-c9f88.firebaseio.com/')
result = firebase.get('/Management', None)
for key in result:
    if key == 'Emergency':
        usr_loc = result[key]
    elif key == 'Ambulance':
        amb_loc = result[key]
    elif key == 'Hospitals':
        hos_loc = result[key]

print(usr_loc)
print(amb_loc)
print(hos_loc)

print('_________________end_of_reading_________________')

while 1:
    for user in usr_loc:
        if (usr_loc[user]['request'] != 0):
            minA = 0
            minH = 0
            amb_info = {}
            usr_info = {}
            hos_info = {}

            flag = 0
            slat = radians(usr_loc[user]['Location']['Latitude'])
            slon = radians(usr_loc[user]['Location']['Longitude'])
            # print (slat)
            # print (slon)
            for ambu in amb_loc:
                # print (ambu)
                if (amb_loc[ambu]['engaged'] != 1):
                    elat = radians(amb_loc[ambu]['Location']['Latitude'])
                    elon = radians(amb_loc[ambu]['Location']['Longitude'])
                    if flag == 0:
                        minA = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
                        flag = 1
                        amb_info = ambu
                        usr_info = user
                    elif minA > 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon)):
                        minA = dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
                        amb_info = ambu
                        usr_info = user
            flag = 0
            for hos in hos_loc:
                if (hos_loc[hos]['availableBeds'] > 0):
                    elat = radians(hos_loc[hos]['Location']['Latitude'])
                    elon = radians(hos_loc[hos]['Location']['Longitude'])
                    if flag == 0:
                        minH = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
                        flag = 1
                        hos_info = hos
                        usr_info = user
                    elif minH > 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon)):
                        minH = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
                        hos_info = hos
                        usr_info = user
            print(amb_info)
            print(usr_info)
            print(hos_info)

            firebase.patch('/Management/Ambulance/' + str(amb_info), {'engaged': 1, 'user': usr_info, 'hospital': hos_info})
            firebase.patch('/Management/Emergency/' + str(usr_info), {'request': 0})

        print('____________________updating____________________')
        result = firebase.get('/Management', None)
        for key in result:
            if key == 'Emergency':
                usr_loc = result[key]
            elif key == 'Ambulance':
                amb_loc = result[key]
            elif key == 'Hospitals':
                hos_loc = result[key]
