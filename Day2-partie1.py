def solve():
    with open("input2.txt") as f:
        s = 0
        for ligne in f:
            niveaux = [int(x) for x in ligne.split()]

            croissant = True
            decroissant = True
            for i in range(len(niveaux) - 1):
                ecart = niveaux[i+1] - niveaux[i]
                if not (1 <= ecart <= 3):
                    croissant = False
                if not (-3 <= ecart <= -1):
                    decroissant = False

            if croissant or decroissant:
                s += 1
    return s

print(solve())

"""def est_sur(niveaux):
    ecarts = [b - a for a, b in zip(niveaux, niveaux[1:])]
    tous_croissants = all(1 <= e <= 3 for e in ecarts)
    tous_decroissants = all(-3 <= e <= -1 for e in ecarts)
    return tous_croissants or tous_decroissants

with open("input.txt") as f:
    rapports = [[int(x) for x in ligne.split()] for ligne in f]

nb_surs = sum(1 for rapport in rapports if est_sur(rapport))
print(nb_surs)"""
