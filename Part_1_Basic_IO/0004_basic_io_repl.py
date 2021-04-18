# Wir führen das Konzept einer Variable ein, für die
# wir eine kleine Box im Speicher unseres Computers reservieren
# um den String aufzunehmen, den wir eingeben werden
# wenn wir aufgefordert werden, unser Lieblingsessen und
# Lieblingsgetränk einzugeben
favorite_food = input('Was ist dein Lieblingsessen? ')
favorite_drink = input('Was ist dein Lieblingsgetränk? ')

# Hier verwenden wir die in MicroPython eingebaute Formatierungsmethode 
# die Teil der Formatter Klasse des String Moduls ist. 
# Die folgende Code-Zeile liefert 
# eine Antwort zurück auf die Konsole, basierend auf
# unseren beiden Variablen, die wir oben eingegeben haben
print('Ich liebe {0} und {1} gleichermaßen!'.format(favorite_food, favorite_drink))
