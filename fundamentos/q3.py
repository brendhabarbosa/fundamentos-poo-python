list_names = ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana"]

cont = {}
for name in list_names:
    if name in cont:
        cont[name] += 1
    else:
        cont[name] = 1

print("Contagem de nomes:", cont)

names_duplicates = [names for names in cont if cont[names] > 1]

print("Nomes duplicados:", names_duplicates)