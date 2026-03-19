lista_nomes = ["chocolate" , "yasmin"]
vogais = "aeiouAEIOU"
count = 0

for nome in lista_nomes:
  print(nome)
  for i in nome:
      if i in vogais:
        count += 1
