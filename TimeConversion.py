''''### PROVA 1

import datetime

orario='18:24:57.441270'
ore, minuti, secondi = orario.split(":")
ore = int(ore)
minuti = int(minuti)
secondi, millesimi = secondi.split(".")
secondi = int(secondi)
millesimi = int(millesimi)

orario_umano = datetime.datetime(2023, 5, 17, ore, minuti, secondi, millesimi)  # 26 maggio 2023, ore 10:30:00
tempo_macchina = orario_umano.timestamp()

print(tempo_macchina)
'''

from datetime import datetime, timedelta
from dateutil import parser

# Stringa di tempo con secondi decimali
tempo_stringa = "18:24:57.441270"

# Utilizzare dateutil.parser per convertire la stringa di tempo in un oggetto datetime
tempo_datetime = parser.parse(tempo_stringa)
print(tempo_datetime)

# Ottenere i millesimi di secondo come parte frazionaria dei secondi
millesimi_secondo = tempo_datetime.microsecond / 1000.0

# Aggiungere i millesimi di secondo come parte frazionaria dei secondi dell'oggetto datetime
tempo_datetime2 = tempo_datetime.replace(microsecond=0) + timedelta(milliseconds=millesimi_secondo)
print(tempo_datetime2)

# Convertire datetime in tempo macchina
tempo_macchina = tempo_datetime.timestamp()

print(tempo_macchina)