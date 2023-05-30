import requests
import json
import re


data = requests.get('http://www.columbia.edu/~fdc/sample.html').text
print(data)

result = re.findall(r'>.+</h3>', data)
finish_result = list(map(lambda x: x[1:-5], result))
print(finish_result)