#%%
name = input("Entern name: ")
age = input(f"hello {name}, how old are you?")
print(age)

#%%
print('hello')
      
# typer av fel man kan få:
# syntax error - skrivit fel i koden, följer inte syntax
# runtime error - syntaxen är korrekt, men man får tex name error, value error, type error
# logiska fel: koden fungarar, får köra den, men den är felaktig
# ToDo: lär mig hur man jobbar med terminalen i vscode
# "try:" - försök göra detta...
# "except"
#%%
my_int = int(input("input integer: "))
print(f"my int = {my_int}")
#%%
try:
    my_int = int(input("input integer: "))
except ValueError:
    print("my_int is not an integer.")
else:
    print(f"my int = {my_int}")

# man kan skriva excep på olika sätt.
# except ValueError tex
# bara lägga koden som man tror kan gå fel, i try blocket
# det som ligger i except blocket körs om det som finns i try inte fungerar.
# det som ligger i else blocket körs om det som finns i try blocket fungerar.
# man kan ha flera except efter varandra.
# ToDo: leta upp en online python interpreter som visar hur koden fungerar.
# 
#%% ett annat sätt att göra det på:
while True:
    try:
        my_int = int(input("input integer: "))
        print(x)
    except ValueError:
        print("my_int is not an integer.")
    except NameError:
        print('x is not degfined.')
    except:
        print('some other kind of error')
    else:
        break

print(f"my int = {my_int}")
#%% funktion, kortaste varianten man kan skriva typ
def input:int(prompt = ""):
    while True:
        try:
            return = int(input("input integer: "))
        except ValueError:
            print("my_int is not an integer.")
#%%
import random
l1 = [1, 4, 4, 5, 7, 2, 8, 2]
l2 = [2, 3, 6, 1, 8, 2, 5, 1]
l3 = random.sample(range(0, 8), 8) 
print(f'{l1 =}')
print(f'{l2 =}')
print(f"{l3 = }")

l4 = zip(l1, l2, l3)

for item in l4:
    print(item)
#sorterar listan l1 baserat på random listan l3
sorted_l1 = [x[1] for x in sorted(zip(l3, l1))]
sorted_l2 = [x[1] for x in sorted(zip(l3, l2))]
print(f'{sorted_l1 = }')
print(f'{sorted_l2 = }')

#sorterar både lista l1 och l2, baserat på lista l3
# man kan använda enumerate och zip.
# https://www.geeksforgeeks.org/zip-in-python/

#sorted_l12 = [(x[1]),(x[2]) for x, y in sorted(zip(l3, l1, l2))]





l4 = []

# %%
