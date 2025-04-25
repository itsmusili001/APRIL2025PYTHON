#converting a word to a coded word
codes={"a":"c","b":"d","c":"e","d":"f","e":"g","f":"h","g":"i","h":"j","i":"k","j":"l","k":"m","l":"n","m":"o",
       "n":"p","o":"q","p":"r","q":"s","r":"t","s":"u","t":"v","u":"w","v":"x","w":"y","x":"z","y":"a","z":"b"}
plainName=input("enter a name :")
codedName=""
for x in plainName:
    if x in codes:
        codedName+=codes[x]
   
    else:
        print("do not use numbers, special characters or capital letters ")
print(f"coded name:  {codedName}")