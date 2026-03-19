listas_nomes = ["yasmin" , "chocolate" , "matheus"]
vogais  = "aeiouAEIOU"
for nome in lista_nomes:
  print(nome)
  for i in nome:
    if i in vogais:
      count += 1
print(f"Nessa lista tem {count} vogais")
