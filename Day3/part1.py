import re 
with open("Day3/input3.txt") as f: 
    memoire=f.read()
paires = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memoire) # r est un raw string (chaîne brute) ça empêche python de mal interpreter \ --- (\d{1,3}) \d signifie un chiffre 0 à 9 et {1,3} signifie entre 1 et 3 
total = sum(int(x) * int(y) for x, y in paires)
print (total)