# -*- coding: cp1252 -*-
# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# <Jinwoo Yu>
# <Kort beskrivning av vad programmet gör>
# En klass som beskriver ett simulerat nöjesfält
# Attribut:
#       namn = Karusellens/attraktionens namn
#       minLangd = minimilängden
#       magpirrfaktor = magpirrfaktor

from random import*
import os                       # importerat för att kunna stänga programmet.
                                # Jag lyckades aldrig få sys.exit() att fungera trots att jag importerat sys. Hoppas det är okej.

class Karusell:

    # Konstruktorn
    def __init__(self, karusellNamn, minLangd, magpirrfaktor, ljud):
        self.namn = karusellNamn
        self.minLangd = int(minLangd)
        self.magpirrfaktor = magpirrfaktor
        self.ljud = ljud

    #Startar karusellen.
    def starta(self) :
        print(self.ljud)

    # Haverera som slumpas fram. Kollar om två slumpade värden från 0-10 blir lika, då havererar attraktionen.
    # Värdet 1 returneras om attraktionen havererat. Mer om det senare i vilkenAttraktion-funktionen.
    def haverera(self):
    
        haveriChans = randrange(0, 11)
        haveri = randrange(0, 11)
        somBool = 0
        
        if haveriChans == haveri :
            print(self.namn + " har havererat. ")
            somBool = 1
            return somBool
        else :
            return somBool

    # Stoppa attraktionen
    def stoppa(self) :
        print(self.namn, " har stoppats.")

    # Göra reklam för sig
    def reklam(self) :
        print(self.namn +  " ar super kul och far dig att skrika " + self.ljud + "! Magpirrfaktorn ar " + str(self.magpirrfaktor) + ".")


# -------- Funktioner till koden i Main --------

# Frågar om användaren vill se reklam om någon av attraktionerna.
def seReklam():
    print("Valkommen! \n")
    svar1 = input("Vill du se reklam om vara attraktioner? Skriv ja/nej? eller " + "q" + " for att avsluta programmet: \n")
    if svar1 == "q":
        os._exit(1)
    elif svar1 == "ja" :
        print("""Skriv namnet pa attraktionen som du vill se reklam om.\n
Bergochdalbana
Balder
Lusthuset \n""")
        svar2 = input("Skriv nej for att skippa reklam, q = avsluta: \n")

        if svar2 == "q":
            os._exit(1)
        else:    
            while svar2 != "nej" :    
                if svar2 == berg.namn :
                    berg.reklam()
                elif svar2 == balder.namn :
                    balder.reklam()
                elif svar2 == lusthuset.namn :
                    lusthuset.reklam()

                print()
                svar2 = input("""Vilken attraktion vill du se reklam om? \n
    Bergochdalbana
    Balder
    Lusthuset?\n
    Skriv nej for skippa reklam, q = avsluta: \n""")
                if svar2 == "q":
                    os._exit(1)

        print()


# Ber användaren om vilken attraktion den vill besöka/åka.
# Den valda attraktionen startas och klassmetoden haverera körs.
# Metoden haverera returnerar siffran 1 om attraktionen havererat, annars returneras 0.
# Det behövs till senare i koden när programmet kollar om attraktionen
# redan havererat eller ifall man kan stoppa attraktionen.
def vilkenAttraktion(attraktion):
    if langd < 140 :
        print("Du ar for kort for att aka " + berg.namn + " eller " +  balder.namn + ".")
        os._exit(1)
    elif attraktion == berg.namn and langd >= 140 :
        berg.starta()
        omHaveri = berg.haverera()
        return omHaveri
    elif attraktion == balder.namn and langd >= 140 :
        balder.starta()
        omHaveri = balder.haverera()
        return omHaveri
    elif attraktion == lusthuset.namn :
        lusthuset.starta()
        omHaveri = lusthuset.haverera()
        return omHaveri

# Kollar om haveri skett. Kollar först om längden är över 140 för om inte det stämmer,
# så betyder det att varken Bergochdalbanan eller Balder har körts.
def kollaHaveri(omHaveri, attraktion):
    if attraktion == lusthuset.namn and omHaveri == 1 :
            print("Vi beklagar for haveriet. Valkommen tillbaka nasta ar!")
            os._exit(1)
    elif langd > 140 :
        if attraktion == berg.namn and omHaveri == 1 :
            print("Vi beklagar for haveriet. Valkommen tillbaka nasta ar!")
            os._exit(1)
        elif attraktion == balder.namn and omHaveri == 1 :
            print("Vi beklagar for haveriet. Valkommen tillbaka nasta ar!")
            os._exit(1)
        else :
            omStoppa(attraktion)
    else :
        omStoppa(attraktion)

# Frågar användaren ifall attraktionen ska stoppas, förutsatt att den inte har havererat.
# Frågan repeteras till användaren stoppar attraktionen genom att svara "ja".
def omStoppa(attraktion):
    svar3 = ""    
    while svar3 != "ja" :
        svar3 = input("Vill du stoppa attraktionen? ja/nej? ")
        if svar3 == "ja" and attraktion == berg.namn :
            berg.stoppa()
        elif svar3 == "ja" and attraktion == balder.namn :
            balder.stoppa()
        elif svar3 == "ja" and attraktion == lusthuset.namn :
            lusthuset.stoppa()
        else :
            print("Okej, fortsatt njut av akturen!")
            
    os._exit(1)
            

#-------------- Main ----------------

# Attraktioner
berg = Karusell("Bergochdalbana", 140, 7, "Iiiih!")
balder = Karusell("Balder", 140, 10, "Aaaah!")
lusthuset = Karusell("Lusthuset", 0, 0, "Hahah!")

# Visa reklam
seReklam()

# Val av attraktion
attraktion = input("""Skriv namnet pa attraktionen du vill aka. \n
Bergochdalbana
Balder
Lusthuset?\n
q = avsluta: \n""")

if attraktion == "q" :
    os._exit(1)
langd = int(input("Hur lang ar du? "))

# Startar vald attraktion.
omHavererat = vilkenAttraktion(attraktion)    # Variabeln "omHavererat" är av värdet 1 eller 0 beroende på om haveri skett. Mer om det står vid vilkenAttraktion-funktionen. 

# Kollar först om attraktionen har havererat, om den har det så får användaren ett välkommen åter-hälsning.
# Om attraktionen inte havererat så frågar programmet om användaren vill stoppa attraktionen.
kollaHaveri(omHavererat, attraktion)
        
    
