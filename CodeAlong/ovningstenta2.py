# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:07:30 2023

@author: danie
"""

#%% Övningstenta uppgift 3 (fick rätt direkt på den)
import random

ds = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

for i in range(1_000_000):
    nbr = random.randint(1,6)
    ds[str(nbr)] += 1
    
print(ds)

#%% Övningstenta uppgift 4 ()
def pattern(n):
    for row in range(n):
        for col in range(n):
            if row%2 == 1 and col%2 == 1:
                print('o', end=' ') #end=' ' ger ett whitespace mellan varje
            else: print('x', end=' ')
        print() # ny rad
        
pattern(5)
#%% övningstenta uppgift 5
system = {1000 : ['Tusenlapp: ',0],
          500 : ['Femhundralapp: ', 0],
          200 : ['Tvåhundralapp ', 0],
          100 : ['Hundralapp ', 0],
          50 : ['Femtiolapp', 0],
          20 : ['Tjugolapp', 0],
          10 : ['Tiokrona', 0],
          5 : ['Femkrona', 0],
          2 : ['Tvåkrona', 0],
          1 : ['Enkrona', 0]}

belopp = 3214

for key in system:
    antal = belopp//key
    belopp = belopp - antal * key
    system[key][1] = antal
    
for key in system:
    if system[key][1] != 0:
        print(f'{system[key][0]} : {system[key][1]}')
        

#%% Hur man kommer åt andra indexet i value listan:
my_dict = {1000 : ['Tusenlapp: ',0],
          500 : ['Femhundralapp: ', 0],
          200 : ['Tvåhundralapp ', 0]}

print(my_dict[1000][1])

#%% Övningstenta, uppgift 3:

import math

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

try:
    r = float(input('Write cylinder radius: '))
    h = float(input('Write cylinder height: '))
    if r > 0 and h > 0:
        cyl_vol = cylinder_volume(r, h)
        print(cyl_vol)
except ValueError:
    print('Input must be floats or integers')


#%% Övning 6
class Animal:
    def __init__(self, name):
        self.name = name

def __str__(self):
    return f"Animal {self.name}"

class Dog(Animal):
    def __repr__(self):
        return f"Dog: {self.name}"

class Fish(Animal):
    def __repr__(self):
        return f"Fish: {self.name}"


class PetOwner:
    def __init__(self, name, dogs=[], fishes=[]):
        self.name = name
        self.dogs = [Dog(dog) for dog in dogs] #instanitiera en hund av klassen Dog för varje hund i listan
        self.fishes = [Fish(fish) for fish in fishes] # samma för fisk
        
    def __str__(self):
        text = self.name + (' owns:\n') + str([str(dog) for dog in self.dogs]) +"\n" + str([str(fish) for fish in self.fishes])
        return text

owner1 = PetOwner('Ada', ['Bruno','Charlie'],['Guppy','Buppy'])
owner2 = PetOwner('Beda', ['Kalle','Plutten'])
print(owner1)
print(owner2)
#%% Practice Exam uppgift 6:
class Litteratur:
    def __init__(self, titel):
        self.titel = titel
    def __str__(self):
        return f'Litteratur: "{self.titel}"'

class Bok(Litteratur):
    def __str__(self):
        return f'Bok: "{self.titel}"'

class Tidning(Litteratur):
    def __str__(self):
        return f'Tidning: "{self.titel}"'

class Tidskrift(Litteratur):
    def __str__(self):
        return f'Tidskrift: "{self.titel}"'


class Bibliotekarie:
    def __init__(self, namn, böcker=[], tidningar=[], tidskrifter=[]):
        self.namn = namn
        self.böcker = [Bok(namn) for namn in böcker]
        self.tidningar = [Tidning(namn) for namn in tidningar]
        self.tidskrifter = [Tidskrift(namn) for namn in tidskrifter]
        
    def __str__(self):
        text = self.namn + " ansvarar för:\n"
        if self.böcker:
            text += str([str(namn) for namn in self.böcker]) + "\n"
        if self.tidningar:
            text += str([str(namn) for namn in self.tidningar]) + "\n"
        if self.tidskrifter:
            text += str([str(namn) for namn in self.tidskrifter]) + "\n"
        
        return text
    
bib1 = Bibliotekarie("Erik", böcker=["Sagan om Ringen", "Hobbiten"],
tidningar=["Dagens Nyheter"], tidskrifter=["Nature"])

#sagan_om_ringen = Bok('sagan om ringen')
#print(sagan_om_ringen)
#print(str(sagan_om_ringen))

print(bib1)

#%%
# manuell test av Bibliotekarie
bib1 = Bibliotekarie("Erik", böcker=["Sagan om Ringen", "Hobbiten"],
tidningar=["Dagens Nyheter"], tidskrifter=["Nature"])
bib2 = Bibliotekarie("Anna", böcker=["Moby Dick"],
tidskrifter=["Science"])
print(bib1)
print(bib2)
#Implementera Bibliotekarie klassen så att du får liknande utskrift som nedan med det manuella
#testet:
Erik ansvarar för:
[Bok: "Sagan om Ringen", Bok: "Hobbiten"]
[Tidning: "Dagens Nyheter"]
[Tidskrift: "Nature"]
Anna ansvarar för:
[Bok: "Moby Dick"]
[Tidskrift: "Science"]