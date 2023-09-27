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
