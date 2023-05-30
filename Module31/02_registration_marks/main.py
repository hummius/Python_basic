import re
from typing import List


text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

result_1: List[str] = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text)
result_2: List[str] = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3,6}', text)

print(f'Список номеров частных автомобилей: {result_1}')
print(f'Список номеров такси: {result_2}')
