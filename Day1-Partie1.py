gauche, droite = [], []
with open("input.txt") as f:
    for ligne in f:
        g, d = ligne.split()
        gauche.append(int(g))
        droite.append(int(d))

distance = sum(abs(g - d) for g, d in zip(sorted(gauche), sorted(droite)))
print(distance)