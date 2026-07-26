from Boletos import BoletoAvion
class BoletoClienteFrecuente(BoletoAvion):
    def __init__(self, nombre_cliente, direccion_cliente,telefono_cliente,
                 valor_boleto,impuesto_salida,hora_salida,hora_llegada,
                 ciudad_salida,ciudad_destino,porcentaje_descuento):
        super().__init__(nombre_cliente,direccion_cliente,telefono_cliente,valor_boleto,
                         impuesto_salida,hora_salida,hora_llegada,ciudad_salida,ciudad_destino)
        self.porcentaje_descuento = porcentaje_descuento

    def calcularpreciopagar(self):
            descuento = self.valor_boleto * self.porcentaje_descuento
            return self.valor_boleto + self.impuesto_salida - descuento
