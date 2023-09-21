# Call stack: håller reda på anropen,
# "stack overflow error", call stacken överfull
# recursive: kan användas, men det finns risk för cirkulära anrop.
# recursive kan användas när man har en trädstruktur man vill undersöka.
# maze solver.
# i de flesta fall blir koden jobbigare med recursive.
# i felmeddelanden visas call stacken!

def main():
    print('start of main()')
    print('end of main()')..


def func_a():
    print('start of funca()')
    print('end of func_a()')

main()
