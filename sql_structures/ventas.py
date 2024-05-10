from .manager import Manager

columns_ingreso_f = ['id', 'nombre', 'nit', 'direccion', 'producto', 'total', 'inventarioFarmacia_id', 'usuarioFactura']
columns_ingreso_c = ['id', 'nombre', 'nit', 'direccion', 'producto', 'total', 'inventarioFarmacia_id']

class Factura:
    def __init__(self, nombre, nit, direccion, producto, total, inventarioFarmacia_id, usuarioFactura, columna=None, valor=None, noFactura=None):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.producto = producto
        self.total = total
        self.inventarioFarmacia_id = inventarioFarmacia_id
        self.usuarioFactura = usuarioFactura
        self.columna = columna
        self.valor = valor
        self.noFactura = noFactura

    def management(self, action):
        if action == 'ag_factura':
            self.factura_ag()
        # elif action == 'up_factura':
        #     self.factura_update()
        # elif action == 'del_factura':
        #     self.factura_delete()

    # def factura_update(self):
    #     management = Manager()
    #     management.update_table_with_id('factura', columns_ingreso_f, self.columna, self.valor, self.noFactura)

    def factura_ag(self):
        management = Manager()
        data_list = [self.nombre, self.nit, self.direccion, self.producto, self.total, self.inventarioFarmacia_id, self.usuarioFactura]
        management.insert_into_table('factura', columns_ingreso_f, data_list)
        # management.print_table('cliente')

    # def factura_delete(self):
    #     management = Manager()
    #     management.delete_id_row('factura', columns_ingreso_f, self.noFactura)

    def __str__(self):
        return (f"{self.nombre}, {self.nit}, {self.direccion}, {self.producto}, {self.total}, "
                f"{self.inventarioFarmacia_id}, {self.usuarioFactura}")


class Cotizacion:
    def __init__(self, nombre, nit, direccion, producto, total, inventarioFarmacia_id, columna=None, valor=None, noCotizacion=None):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.producto = producto
        self.total = total
        self.inventarioFarmacia_id = inventarioFarmacia_id
        self.columna = columna
        self.valor = valor
        self.noCotizacion = noCotizacion

    def management(self, action):
        if action == 'ag_cotizacion':
            self.cotizacion_ag()
        # elif action == 'up_cotizacion':
        #     self.cotizacion_update()
        # elif action == 'del_cotizacion':
        #     self.cotizacion_delete()

    # def cotizacion_update(self):
    #     management = Manager()
    #     management.update_table_with_id('cotizacion', columns_ingreso_c, self.columna, self.valor, self.noCotizacion)

    def cotizacion_ag(self):
        management = Manager()
        data_list = [self.nombre, self.nit, self.direccion, self.producto, self.total, self.inventarioFarmacia_id]
        management.insert_into_table('cotizacion', columns_ingreso_c, data_list)
        # management.print_table('cliente')

    # def cotizacion_delete(self):
    #     management = Manager()
    #     management.delete_id_row('cotizacion', columns_ingreso_c, self.noCotizacion)

    def __str__(self):
        return (f"{self.nombre}, {self.nit}, {self.direccion}, {self.producto}, {self.total}, {self.inventarioFarmacia_id},")