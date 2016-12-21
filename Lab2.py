# Programmeringsteknik webbkurs KTH inl�mningsuppgift 2.
# <Jinwoo Yu>
# <Anv�ndaren f�r skriva in fyra meningar sedan skapar programmet en rondelet av de.>
import string
                         
#Skriver ut v�lkomstmeddelandet.
def intro():
    print("""                   DIKTAUTOMATEN

    Skriv in fyra meningar och f� ut rondelet!\n""")

#Ber anv�ndaren att skriva in fyra meningar.
def inputs():
    sentence = 4*[None]                             #None betyder att alla platserna ska vara lediga
    for i in range(0, 4):
        print("Skriv mening nr ", i+1, ": ")
        sentence[i] = input()

    return sentence

#Delar upp den f�rsta meningen
def sentenceOne(sentences):
    firstSentence = sentences[0].split()            #Delar orden fr�n sentences[0] och l�gger i listan firstSentence
    return firstSentence

#Tar de f�rsta fyra orden fr�n de f�rsta meningen
def firstFour(firstSentence, size):
                                                    #Kollar ifall f�rsta meningen best�r av f�rre �n fyra ord.
    if size < 4 :
        fourWords = size*[None]
        for i in range(size) :
            fourWords[i] = firstSentence[i]   
    else :
        fourWords = 4*[None]
        for i in range(0, 4):                       #Tar de f�rsta fyra orden.
            fourWords[i] = firstSentence[i]
            
    return fourWords

#Skriver ut rondelet.
def rondelet(fourWords, restOfSentence, theSentences):
    print(fourWords.upper())                        #Skriver ut de f�rsta fyra orden i versaler.
    print("\n")                                     #Radbyte
    print(fourWords)                                #Skriver ut de fyra orden fr�n den f�rsta meningen.
    print(restOfSentence)
    print(fourWords)
    for i in range(1, 4):
        print(theSentences[i])
    print(fourWords)

#S�tter ihop listor av ord till en str�ng
def join(sentence):
    joined = " ".join(sentence)
    return joined



#Main program
intro()                                             #Skriver ut introt
sentences = inputs()                                #sentences �r en lista med de fyra meingarna som anv�ndaren skrivit in
firstSentence = sentenceOne(sentences)              #firstSentence �r f�rsta meningen

sizeOf = len(firstSentence)
fourWords = firstFour(firstSentence, sizeOf)        #F�rsta fyra orden fr�n f�rsta meningen

                                                    #Ifall f�rsta meningen best�r av f�rre �n 4 ord.
if sizeOf < 4 :
    restOfSentence = firstSentence[sizeOf:]         #Andra delen av den f�rsta meningen.
else :
    restOfSentence = firstSentence[4:]
    
theRestOfSentence = join(restOfSentence)            #Bildar en str�ng av resten av orden fr�n f�rsta meningen.
theFourWords = join(fourWords)                      #S�tter ihop de fyra f�rsta orden till en str�ng.

rondelet(theFourWords, theRestOfSentence, sentences)#Skriver ut rondelet.








    
