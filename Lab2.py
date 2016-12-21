# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# <Jinwoo Yu>
# <Användaren får skriva in fyra meningar sedan skapar programmet en rondelet av de.>
import string
                         
#Skriver ut välkomstmeddelandet.
def intro():
    print("""                   DIKTAUTOMATEN

    Skriv in fyra meningar och få ut rondelet!\n""")

#Ber användaren att skriva in fyra meningar.
def inputs():
    sentence = 4*[None]                             #None betyder att alla platserna ska vara lediga
    for i in range(0, 4):
        print("Skriv mening nr ", i+1, ": ")
        sentence[i] = input()

    return sentence

#Delar upp den första meningen
def sentenceOne(sentences):
    firstSentence = sentences[0].split()            #Delar orden från sentences[0] och lägger i listan firstSentence
    return firstSentence

#Tar de första fyra orden från de första meningen
def firstFour(firstSentence, size):
                                                    #Kollar ifall första meningen består av färre än fyra ord.
    if size < 4 :
        fourWords = size*[None]
        for i in range(size) :
            fourWords[i] = firstSentence[i]   
    else :
        fourWords = 4*[None]
        for i in range(0, 4):                       #Tar de första fyra orden.
            fourWords[i] = firstSentence[i]
            
    return fourWords

#Skriver ut rondelet.
def rondelet(fourWords, restOfSentence, theSentences):
    print(fourWords.upper())                        #Skriver ut de första fyra orden i versaler.
    print("\n")                                     #Radbyte
    print(fourWords)                                #Skriver ut de fyra orden från den första meningen.
    print(restOfSentence)
    print(fourWords)
    for i in range(1, 4):
        print(theSentences[i])
    print(fourWords)

#Sätter ihop listor av ord till en sträng
def join(sentence):
    joined = " ".join(sentence)
    return joined



#Main program
intro()                                             #Skriver ut introt
sentences = inputs()                                #sentences är en lista med de fyra meingarna som användaren skrivit in
firstSentence = sentenceOne(sentences)              #firstSentence är första meningen

sizeOf = len(firstSentence)
fourWords = firstFour(firstSentence, sizeOf)        #Första fyra orden från första meningen

                                                    #Ifall första meningen består av färre än 4 ord.
if sizeOf < 4 :
    restOfSentence = firstSentence[sizeOf:]         #Andra delen av den första meningen.
else :
    restOfSentence = firstSentence[4:]
    
theRestOfSentence = join(restOfSentence)            #Bildar en sträng av resten av orden från första meningen.
theFourWords = join(fourWords)                      #Sätter ihop de fyra första orden till en sträng.

rondelet(theFourWords, theRestOfSentence, sentences)#Skriver ut rondelet.








    
