'''arquivo = open("texto.txt","r")
print(arquivo.read())'''
'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.seek(0))
print(arquivo.readlines())
#print(arquivo.seek(0))'''
'''print(arquivo.tell())
arquivo.close()
print(arquivo.closed)'''
'''print(arquivo.read())
print(arquivo.seek(0))
print(arquivo.read(8))'''
'''print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)'''

'''arquivo = open("novo.txt","w")
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("frutas.txt","w")
arquivo.write("banana")
arquivo.write("uva")
arquivo.write("mamao")
arquivo.close()'''

'''precos = [20,100,500,600]
with open("precos_roupas.txt","w") as arquivo:
 for preco in precos:
     arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

'''precos =  [8000]
with open("precos_roupas.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''
"""precos = [100000]
with open("precos_roupas", "w") as arquivo:
    for preco in precos:
        .write(str(preco) + '\n')"""

"""with open ("texto.txt", "r") as arquivo:
    print("Representação oroginal da linha")
    for linha in arquivo:
        linha_ = linha.strip()
        print(repr(linha_))"""

"""try: 
    with open("arquivo_teste","r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo inexistente")"""

'''import os 
try:
    os.remove("teste1.txt")
    print("Arquivo removido")
except FileNotFoundError as error:
    print("Descrição;", error)'''

try:
    f = open("novo2.txt","r")
    f.write("hello")
except IOError as erro:
    print ("O erro foi: ", erro)