import fuzzywuzzy
from fuzzywuzzy import fuzz


aproximacion=fuzz.ratio('hola', 'hola')

print(aproximacion)