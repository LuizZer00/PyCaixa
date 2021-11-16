import datetime
from time import gmtime, strftime

comprando = 0
prod = []
carrinho = []
totalProd = 0
total = 0

print(" -------------")
print("|Super Mercado|")
print(" -------------")
print("\n0-Encerrar Programa.\n1-Adicionar ao estoque.\n2-Pesquisar via código.\n3-Mostrar Produtos.\n4-Adicionar ao carrinho.\n5-Ver Produtos do carrinho.\n6-Nota Fiscal.")

while(1):   
 print("\n")
 try:
    op = int(input("Opção:"))
 except:
    print("Parâmetro Inválido!")
    continue

 if op == 0:
  print("Encerrando Programa.")
  exit(0)

  
 if op == 1:
  try:
      pro = input("\nProduto:")	
      pre = float(input("Preço:"))
      cod = int(input("Código:"))
      aux = pro,pre,cod
      prod.append(aux)
  except:
      print("Parâmetro Inválido!")
      continue

	
 if op == 2:
  codI = int(input("Código:"))
  for i in prod:
   if codI in i:
    print("\n-Produto:", i[0])
    print(" Preço:", i[1], "R$")
    print(" Código:", i[2])
     
 
 
 if op == 3:
  for i in prod:
    print("\n-Produto:", i[0])
    print(" Preço:", i[1], "R$")
    print(" Código:", i[2])
    print("\n")


 if op == 4:
    try:
      codI = int(input("Código:"))
    except:
       print("Parâmetro Inválido!")
       continue

    for i in prod:
        if codI in i:
            carrinho.append(i)
            totalProd += 1
            aux = i[1]
            total += aux
            comprando = 1

      
 if op == 5:
  for i in carrinho:
   print("\n-Produto:", i[0])
   print(" Preço:", i[1], "R$")
   print(" Código:", i[2])
   print("\n")


 if op == 6 and comprando == 1:
    print("\n -----------")
    print("|Nota Fiscal|")
    print(" -----------\n")
    print("Quantidade de produtos:",totalProd)
    print("Total:",total, "R$\n\n")
    print(str("Data: " + datetime.datetime.now().strftime('%Y-%m-%d')))
    print(str("Hora: " + datetime.datetime.now().strftime('%H:%M:%S')))
    break
 elif op == 6 and comprando == 0:
  print("Carrinho Vázio!")
  continue
    
       
 
     
       
