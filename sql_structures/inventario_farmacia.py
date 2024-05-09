from .manager import Manager

columns_ingreso = ['id', 'nombre', 'cantidad', 'descripcion', 'precio', 'fecha_de_vencimiento']


class InventarioFarmacia:
    def __init__(self, nombre, cantidad, descripcion, precio, fecha_de_vencimiento, columna=None, valor=None, noInventario=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.precio = precio
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.columna = columna
        self.valor = valor
        self.noInventario = noInventario

    def management(self, action):
        if action == 'ag_inventarioFarmacia':
            self.inventarioFarmacia_ag()
        elif action == 'up_inventarioFarmacia':
            self.inventarioFarmacia_update()
        elif action == 'del_inventarioFarmacia':
            self.inventarioFarmacia_delete()

    def inventarioFarmacia_update(self):
        management = Manager()
        management.update_table_with_id('inventarioFarmacia', columns_ingreso, self.columna, self.valor, self.noInventario)

    def inventarioFarmacia_ag(self):
        management = Manager()
        data_list = [self.nombre, self.cantidad, self.descripcion, self.precio, self.fecha_de_vencimiento]
        management.insert_into_table('inventarioFarmacia', columns_ingreso, data_list)
        # management.print_table('cliente')

    def inventarioFarmacia_delete(self):
        management = Manager()
        management.delete_id_row('inventarioFarmacia', columns_ingreso, self.noInventario)

    def __str__(self):
        return f"{self.nombre}, {self.cantidad}, {self.descripcion}, {self.precio}, {self.fecha_de_vencimiento}"