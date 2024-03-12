def calcular_imc(peso,altura):
    return peso / (altura*altura)

def classificar_imc(imc):                    
  if imc < 18.5:
     return "Abaixo do peso"
  elif 18.5 <= imc <25:
     return "peso normal"
  elif 25 <= imc <30:
     return "sobrepeso"
  elif 30<= imc <35:
    return "obesidade grau 1"
  elif 35<= imc <40:
    return "obesidade grau 2 (severa)"
  else: 
     return "obesidade grau3 (mórbida)"
  
peso = float(input("digite seu peso em Kg:"))
altura = float( input("digite sua altura em metros"))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
 

print("seu imc:", imc)
print("classificacao:", classificacao)    
