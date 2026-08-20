def est_sur(niveaux):
    ecarts=[b-a for a, b in zip(niveaux, niveaux[1:])]
    tous_croissants= all(1<= e <= 3 for e in ecarts)
    tous_decroissants= all(-3 <= e <= -1 for e in ecarts)
    return tous_croissants or tous_decroissants

def est_sur_avec_dampener(niveaux):
    if est_sur(niveaux):
        return True
    for i in range(len(niveaux)):
        sans_i= niveaux[:i]+ niveaux[i+1:]
        if est_sur(sans_i):
            return True 
    return False
with open("input2.txt") as f :
    rapports=[[int(x) for x in ligne.split()] for ligne in f]

p1= sum(1 for rapport in rapports if est_sur(rapport))
p2= sum(1 for rapport in rapports if est_sur_avec_dampener(rapport))
print("p1", p1)
print("p2", p2)