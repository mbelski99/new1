import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''
regexp1 = re.compile('Niebieski',re.IGNORECASE)
res1 = regexp1.search(bridge_of_death)
print(res1)
res1 = regexp1.findall(bridge_of_death)
print(res1)
res1= regexp1.finditer(bridge_of_death)
for i,s in enumerate(res1):
    print(i,s.start(),s.span()[-1],s.group())