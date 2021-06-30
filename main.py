minu = "abcdefghijklmnopqrstuywxz" 
maiu = "ABCDEFGHIJKLMNOPQRSTUYWXZ"
num = "0123456789"
qtminu = 0 #variavel para guardar a quantidade de letras minusculas
qtmaiu = 0 #variavel para guardar a quantidade de letras maiusculas
qtnum = 0 #variavel para guardar a quantidade de numeros
senhaC = '' 
e = 0
chavecriptografia = 12 #pode ser qualquer outro numero inteiro
print("Informe uma senha Forte \nDeve conter: \n No mínimo 8 caracteres \n Letras maiúsculas\n Letras minusculas\n E números. ")
senha = input("Informe uma senha:")
senha = senha.strip()
if len(senha) >= 8:
  lensenha = len(senha)
  while True:
    if e > lensenha - 1:
      break 
    elif senha[e] in minu:
      qtminu = qtminu + 1
    elif senha[e] in maiu:
      qtmaiu = qtmaiu + 1
    elif senha[e] in num:
      qtnum = qtnum + 1 
    e = e + 1
  if qtminu == 0:
    print("A sua senha precisa conter no mínimo uma letra minuscula.")
  elif qtmaiu == 0:
    print("A sua senha precisa conter no mínimo uma letra maiúscula.")  
  elif qtnum == 0:
    print("A sua senha precisa conter no mínimo um número.") 
  else:
    for l in senha:
      senhaC += chr(ord(l)+chavecriptografia)
else:
  print("Sua senha precisa ter no minimo 8 caracteres.")   
print(senhaC)   
