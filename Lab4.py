# -*- coding: cp1252 -*-
# Programmeringsteknik webbkurs KTH Slutinl�mning.
# <2014-08-17>
# <Programmet f�r en konversation med anv�ndaren och svarar med en mening d�r utvalda ord har bytts ut.>

# Importeras f�r att kunna st�nga programmet.
import os

# ------------------------------------------------
#                   KLASS
# ------------------------------------------------

# En klass som simulerar en konversation, kan b�de l�sa och skriva till fil.
# Attribut:
#           filename = filens namn
#           wordPair = en tom dictionary
#           oppositeWord = en tom dictionary
class Conversation:
    
    #Skapar en textfil.
    def __init__(self, filename):
        self.filename = filename
        self.wordPair = {}
        self.oppositeWord = {}

    # L�sa in orden fr�n textfilen och s�tta de i tv� dictionary.
    def readFile(self):
        
        # Felkontroll ifall filen finns.
        if os.path.isfile(self.filename):
            file = open (self.filename, 'r')
        else:
            print("Det finns ingen fil som heter " + self.filename + ". Programmet avslutas.")
            os._exit(0)
       
        for line in file:
            word1, word2 = line.rstrip('\n').split('/')

            # Tv� dictionarys.
            self.wordPair[word1] = word2
            self.oppositeWord[word2] = word1
  
        file.close()

    # Anv�ndarens svar g�rs till gemener och delas upp.
    # Indata:
    #       sentence = svaret som anv�ndaren matat in.
    # Utdata:
    #       splitSentence = anv�ndarens svar uppdelat och i gemener.
    def prepare(self, sentence):
        lowerCase = sentence.lower()
        splitSentence = lowerCase.split()
        return splitSentence

    # Bygger meningen som programmet ska svara med.
    # Indata:
    #       answerSplit = Anv�ndarens svar, uppdelat, gemener.
    #       name = Anv�ndarens namn.
    # Utdata:
    #       reply = Programmets svar i en str�ng.
    def buildSentence(self, answerSplit, name):
        sentence = ""
        for word in answerSplit:
            if word in self.wordPair:
                sentence += " " + self.wordPair[word]
                
            elif word in self.oppositeWord:
                sentence += " " + self.oppositeWord[word]
                
            else:
                sentence += " " + word

        # Programmets svar.
        reply = "Jasa, " + name + "," + sentence + " An sen?\n" 
        return reply


    # Skriva ut ordlistan i en txt-fil.
    def writeToFile(self):  
        file = open (self.filename, 'w')
        wordpair = "jag/du\n" + "dig/mig\n" + "dej/mej\n" + "vi/ni\n" + "min/din\n" + "mina/dina\n" + "mitt/ditt\n"
        file.write(wordpair)
        file.close()


# ------------------------------------------------
#                   FUNKTIONER
# ------------------------------------------------

# Be anv�ndaren om input.
# Utdata:
#       name = Anv�ndarens namn.
#       answer = Anv�ndarens svar.
def getInput():
    name = input("Hej, jag heter Snacke! Vad heter du?\n")
    if name == "":
        print("Varst vad pratglad du var.")
        os._exit(0)
    else:
        answer = input("Roligt att traffa dej, " + name + "! " + "Vad har du for problem?\n")
        if answer == "":
            print("Varst vad pratglad du var.")
            os._exit(0)

    return (name, answer)

# Input loopas tills anv�ndaren trycker p� enterknappen utan att ha skrivit n�got.
# Indata:
#       theName = Anv�ndarens namn.
#       theAnswer = Anv�ndarens svar.
def loopInput(theAnswer, theName):
    while True:
        # Byta ordparen och bygga meningen som programmet ska svara.
        reply = chat.buildSentence(theAnswer, theName)
        answer = input(reply)
        theAnswer = chat.prepare(answer)
        if answer == "":
            break
        
# ------------------------------------------------
#                   HUVUDPROGRAM
# ------------------------------------------------

# Textfilens namn.
filename = "ordpar.txt"

chat = Conversation(filename)

# Skriva ordparen till en fil.
chat.writeToFile()

# Be anv�ndaren om input.
name, answer = getInput()

# Delar str�ngen som anv�ndaren matat in, och g�r till gemener.
theAnswer = chat.prepare(answer)

# �ppnar textfilen och lagrar orden i tv� dictionary.
chat.readFile()

# Loopas till anv�ndaren trycker p� enterknappen utan att ha skrivit n�got.
loopInput(theAnswer, name)

print("Du skrev inget. Tack for konversationen!")
os._exit(0)
