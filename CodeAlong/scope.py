# Scope: In python we have two types of scope:
# Local scope: variabel skapad i en funktion, kan bara användas i den funktionen
# Global scope: available through execution of program. Global variabel kan användas i funktioner.
# Bra att skriva alla sina funktioner först, i början av koden.
# längre ner skriver man sin kod, man kan sedan start hela programmet med att anropa main()
# Python: variabler som skapas i tex en loop eller if-sats, blir globala. Så är det ofta inte i andra språk, dvs Python har inte "block scope".
# C++, C# och Java har block scope.
# CTRL + K + C
# CTRL + K + U
# CTRL + *
# man kan ha en lokal variabel med samma namn som en global variabeö
# man kan skriva 'global + variabelnamnet' i funktionen, om man vill tilldela en global variabel i funktionen
# man vill undvka att ha för många globala variabler.


def main():
    name = "Fredrik"
    print(name)

main()
