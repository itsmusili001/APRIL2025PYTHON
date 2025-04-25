#converting sentences to coded sentences
codes={"a":"c","b":"d","c":"e","d":"f","e":"g","f":"h","g":"i","h":"j","i":"k","j":"l","k":"m","l":"n","m":"o",
       "n":"p","o":"q","p":"r","q":"s","r":"t","s":"u","t":"v","u":"w","v":"x","w":"y","x":"z","y":"a","z":"b"}
plainSentence=input("enter a sentence:")
codedSentence=""
for word in plainSentence:
    if word in codes:
        codedword = codes[word]
        codedSentence += codedword 
    else:
        codedSentence += word
        
print("Coded sentence:", codedSentence)