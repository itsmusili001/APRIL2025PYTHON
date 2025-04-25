#import random
from random import randint
countries= ["Algeria","Angola","Benin","Botswana","Burundi","Burkina Faso","Cameroon",
"Cape Verde","Central African Republic","Chad","Comoros","Cote d’Ivoire","DR Congo","Djibouti",
"Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon","Gambia","Ghana","Guinea",
"Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania",
"Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Réunion",
"Rwanda","São Tomé and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan",
"Sudan","Swaziland","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]


cities= ["Algiers","Luanda","Porto-Novo","Gaborone","Bujumbura","Ouagadougou","Yaoundé",
"Praia","Bangui","N’Djamena","Moroni","Yamoussoukro","Kinshasa","Djibouti City",
"Cairo","Malabo","Asmara", "Addis Ababa","Libreville","Banjul","Accra","Conakry",
"Bissau","Nairobi","Maseru","Monrovia","Tripoli","Antananarivo","Lilongwe","Bamako","Nouakchott", 
"Port Louis","Rabat","Maputo","Windhoek","Niamey", "Abuja","Brazzaville","Saint-Denis",
"Kigali","Sao Tome","Dakar","Victoria","Freetown","Mogadishu","Pretoria","Juba",
"Khartoum","Mbabane","Dodoma","Lome","Tunis","Kampala","Lusaka","Harare"]

# trying out the random module
#print(len(countries))
#rand=randint(0,len(countries)-1)
#print(rand)

question= ("what is the capital of")
correctPoints=0
incorrectPoints=0
for counter in range(5):
    rand=randint(0,len(countries)-1)
    print(question+" what is the capital of "+countries[rand]+"?")
    
    answer=input()
    if (answer.upper()==cities[rand].upper()):
        print("correct")
    else:
        print("incorrect, the capital of "+countries[rand]+" is "+cities[rand])
    if (answer.upper()==cities[rand].upper()):
        correctPoints+=1
    else:
        incorrectPoints+=1
print(f"correct points: {correctPoints}")
print(f"incorrect points: {incorrectPoints}")
    