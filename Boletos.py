class BoletoAvion:
    def __init__(self,nombre_cliente, direccion_cliente, telefono_cliente,
                 valor_boleto,impuesto_salida,hora_salida,hora_llegada,ciudad_salida,ciudad_destino,):

        self.nombre_cliente = nombre_cliente
        self.direccion_cliente = direccion_cliente
        self.telefono_cliente = telefono_cliente
        self.valor_boleto = valor_boleto
        self.impuesto_salida = impuesto_salida
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.ciudad_salida = ciudad_salida
        self.ciudad_destino = ciudad_destino

    def calcular_precio_pagar(self):
            return self.valor_boleto + self.impuesto_salida

    def __str__(self):
            return(
                f"Cliente: {self.nombre_cliente}\n"
                f"Origen: {self.ciudad_salida}\n" 
                f"Destino: {self.ciudad_destino}"
                f"Precio a pagar: {self.calcular_precio_pagar():.2f}"
            )
