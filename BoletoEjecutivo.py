from Boletos import BoletoAvion
class BoletoEjecutivo(BoletoAvion):
    def __init__(self, nombre_cliente, direccion_cliente,telefono_cliente,
                 valor_boleto, impuesto_salida,hora_salida,
                 hora_llegada,ciudad_salida, ciudad_destino): 
        super().__init__(nombre_cliente,direccion_cliente,telefono_cliente,valor_boleto,
                         impuesto_salida,hora_salida, hora_llegada, ciudad_salida, ciudad_destino)
        self.alimentos_extras =[]

    def agregar_aliemento(self,aliemento):
        self.alimentos_extras.append(aliemento)
    def calcular_total_aliementos(self):
        return sum(alimento.precio for alimento in self.alimentos_extras)
    def calcular_precio_pagar(self):
        return(
            self.valor_boleto + self.impuesto_salida + self.calcular_total_aliementos()
        )
