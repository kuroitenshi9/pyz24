'''1. Utwórz dekorator `@uppercase_decorator`, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
    - Utwórz funkcję zwracającą tekst
    - Utwórz dekorator przyjmujący tę funkcję
    - Wywołaj funkcję, by sprawdzić, że decorator działa
2. Utwórz dekorator `@timepassed` mierzący czas działania dowolnej funkcji.'''

def upper_case_decorator(func):
    def upper_cased():
        z = func()
        print(z.upper())
    return upper_cased
    
@upper_case_decorator
def my_text(text='jakis tam tekst'):
    return text

my_text()