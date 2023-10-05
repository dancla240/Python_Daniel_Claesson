import L27_module

#eller
#from L27_module import square
# runtime error, syntax error (direkt fel), logical error
# testa corner cases, gränsfall => edge cases
# unit testing: testa varje funktion för sig att resultatet blir det man förväntar sig.

# assert, ett keyword (sv. hävda)

print('start')
try:
    assert 1 < 0 # hävdar att 1 är större ön 0. Om det inte stämmer får vi ett AssertionError
except AssertionError:
    print('1 is not less than zero')
print('end')
#print(L27_module.square(9))
