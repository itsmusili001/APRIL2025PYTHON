#converting a letter to a coded letter
codes={"a":"c","b":"d","c":"e","d":"f","e":"g","f":"h","g":"i","h":"j","i":"k","j":"l","k":"m","l":"n","m":"o",
       "n":"p","o":"q","p":"r","q":"s","r":"t","s":"u","t":"v","u":"w","v":"x","w":"y","x":"z","y":"a","z":"b"}

letter=input("enter a letter :")
while letter not in codes:
    print("do not use numbers, special characters or capital letters ")
    letter=input("enter a letter :")
print(f"the coded letter is:{codes[letter]}")
