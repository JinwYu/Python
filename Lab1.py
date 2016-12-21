# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# <2014-07-10>
# <Användaren skriver in ett fyrsiffrigt tal. Programmet beräknar
#  Kaprekar-talet och visar hur många iterationer det krävdes.  >

counter = 0                                     #En räknare som adderas varje gång differensen räknas.

n = int(input("Skriv in ett fyrsiffrigt tal: "))

while n != 6174 :

    if n < 1000 :                                                                  
        n = str(n)
        length = len(n)
        int(length)
        
        while length < 4 :                      #Kollar längden på strängen och adderar en nolla framför talet ifall det inte är fyrsiffrigt
            n = "0" + str(n)
            length = length + 1      

    n = str(n)                                  #Konverterar en int till en sträng.        
    large = "".join(sorted(n, reverse=True))    #Tilldelar talet med stora siffror först i variabeln large. 
    small = "".join(sorted(n))                  #Tilldelar sorterade talet i variabeln small.

    descending = int(large)                     #Gör om strängarna till ints och räknar ut differensen.
    ascending = int(small)
    n = descending - ascending
    
    counter += 1                                #Adderar räknaren med 1.

print("Det krävdes ", counter, " iterationer.") #Utskrift
