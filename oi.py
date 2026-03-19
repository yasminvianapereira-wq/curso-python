lista = []
for i in range(1, 4):
  item = input("Digite o item {i+ 1}")
  lista.append(item)

print(f"sua lista ficou assim: {lista}")

remover = input ("digte um item pra remover.")
for i in lista:
    print(i)
for i in lista:
  if i == remover:
    lista.remoeve(remover)
  else:
    print("não exite esse{remover} na lista")
  print(f"lista: {lista}")
