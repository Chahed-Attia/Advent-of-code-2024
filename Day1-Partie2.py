from collections import Counter

gauche, droite = [], []
with open("input.txt") as f:
    for ligne in f:
        g, d = ligne.split()
        gauche.append(int(g))
        droite.append(int(d))

compte = Counter(droite)
score = sum(g * compte[g] for g in gauche)
print(score)