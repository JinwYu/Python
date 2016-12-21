# -*- coding: cp1252 -*-
# Programmeringsteknik webbkurs KTH inl�mningsuppgift 3.
# <Jinwoo Yu>
# <Kort beskrivning av vad programmet g�r>
# En klass som beskriver ett simulerat n�jesf�lt
# Attribut:
#       namn = Karusellens/attraktionens namn
#       minLangd = minimil�ngden
#       magpirrfaktor = magpirrfaktor

from random import*
import os                       # importerat f�r att kunna st�nga programmet.
                                # Jag lyckades aldrig f� sys.exit() att fungera trots att jag importerat sys. Hoppas det �r okej.

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

    # Haverera som slumpas fram. Kollar om tv� slumpade v�rden fr�n 0-10 blir lika, d� havererar attraktionen.
    # V�rdet 1 returneras om attraktionen havererat. Mer om det senare i vilkenAttraktion-funktionen.
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

    # G�ra reklam f�r sig
    def reklam(self) :
        print(self.namn +  " ar super kul och far dig att skrika " + self.ljud + "! Magpirrfaktorn ar " + str(self.magpirrfaktor) + ".")


# -------- Funktioner till koden i Main --------

# Fr�gar om anv�ndaren vill se reklam om n�gon av attraktionerna.
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


# Ber anv�ndaren om vilken attraktion den vill bes�ka/�ka.
# Den valda attraktionen startas och klassmetoden haverera k�rs.
# Metoden haverera returnerar siffran 1 om attraktionen havererat, annars returneras 0.
# Det beh�vs till senare i koden n�r programmet kollar om attraktionen
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

# Kollar om haveri skett. Kollar f�rst om l�ngden �r �ver 140 f�r om inte det st�mmer,
# s� betyder det att varken Bergochdalbanan eller Balder har k�rts.
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

# Fr�gar anv�ndaren ifall attraktionen ska stoppas, f�rutsatt att den inte har havererat.
# Fr�gan repeteras till anv�ndaren stoppar attraktionen genom att svara "ja".
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
omHavererat = vilkenAttraktion(attraktion)    # Variabeln "omHavererat" �r av v�rdet 1 eller 0 beroende p� om haveri skett. Mer om det st�r vid vilkenAttraktion-funktionen. 

# Kollar f�rst om attraktionen har havererat, om den har det s� f�r anv�ndaren ett v�lkommen �ter-h�lsning.
# Om attraktionen inte havererat s� fr�gar programmet om anv�ndaren vill stoppa attraktionen.
kollaHaveri(omHavererat, attraktion)
        
    
