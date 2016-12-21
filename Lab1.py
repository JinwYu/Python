# Programmeringsteknik webbkurs KTH inl�mningsuppgift 1.
# <2014-07-10>
# <Anv�ndaren skriver in ett fyrsiffrigt tal. Programmet ber�knar
#  Kaprekar-talet och visar hur m�nga iterationer det kr�vdes.  >

counter = 0                                     #En r�knare som adderas varje g�ng differensen r�knas.

n = int(input("Skriv in ett fyrsiffrigt tal: "))

while n != 6174 :

    if n < 1000 :                                                                  
        n = str(n)
        length = len(n)
        int(length)
        
        while length < 4 :                      #Kollar l�ngden p� str�ngen och adderar en nolla framf�r talet ifall det inte �r fyrsiffrigt
            n = "0" + str(n)
            length = length + 1      

    n = str(n)                                  #Konverterar en int till en str�ng.        
    large = "".join(sorted(n, reverse=True))    #Tilldelar talet med stora siffror f�rst i variabeln large. 
    small = "".join(sorted(n))                  #Tilldelar sorterade talet i variabeln small.

    descending = int(large)                     #G�r om str�ngarna till ints och r�knar ut differensen.
    ascending = int(small)
    n = descending - ascending
    
    counter += 1                                #Adderar r�knaren med 1.

print("Det kr�vdes ", counter, " iterationer.") #Utskrift
