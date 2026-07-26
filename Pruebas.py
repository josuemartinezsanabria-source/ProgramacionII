from Boletos import BoletoAvion
from Boletoclientefrecuente import BoletoClienteFrecuente
from AlimentoExtra import AlimentoExtra
from BoletoEjecutivo import BoletoEjecutivo

#Boleto Normal
boleto1 = BoletoAvion(
    "Juan Martinez",
    "Cartago",
    "1234-5678",
    300,
    50,
    "09:00",
    "21:00",
    "Alajuela",
    "MexicoDF"
)
print("Boleto Normal")
print(boleto1)
print()

#Cliente Frecuente
boleto2 = BoletoClienteFrecuente(
    "Maria Lopez",
    "Cartago",
    "1234-5678",
    300,
    50,
    "09:00",
    "21:00",
    "Alajuela",
    "Ciudad Panama",
    0.15 # 15%
)

print("Cliente Frecuente")
print("Precio a pagar:", boleto2.calcularpreciopagar())
print()

#Ejecutivo
boleto3 = BoletoEjecutivo(
    "Carlos Mora",
    "Heredia",
    "8888-2222",
    600,
    100,
    "14:00",
    "04:00" ,
    "Alajuela",
    "Madrid",
)

al1 = AlimentoExtra("A01","Sandwich",25)
al2 = AlimentoExtra("A02","Refresco",10)
al3 = AlimentoExtra("A03","Torta chilena",35)

boleto3.agregar_aliemento(al1)
boleto3.agregar_aliemento(al2)
boleto3.agregar_aliemento(al3)

print("Boleto Ejecutivo")
print("Total alimentos:", boleto3.calcular_total_aliementos())
print("Precio a pagar:",boleto3.calcular_precio_pagar())