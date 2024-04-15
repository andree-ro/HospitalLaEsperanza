from .manager import Manager

columns_ingreso = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']


class Paciente:
    def __init__(self, nombre, telefono, dpi, direccion, telefono2, columna=None, valor=None, noPaciente=None):
        self.nombre = nombre
        self.telefono = telefono
        self.dpi = dpi
        self.direccion = direccion
        self.telefono2 = telefono2
        self.columna = columna
        self.valor = valor
        self.noPaciente = noPaciente

    def management(self, action):
        if action == 'ag_paciente':
            self.cliente_ag()
        elif action == 'up_paciente':
            self.cliente_update()
        elif action == 'del_paciente':
            self.cliente_delete()

    def paciente_update(self):
        management = Manager()
        management.update_table_with_id('paciente', columns_ingreso, self.columna, self.valor, self.noPaciente)

    def paciente_ag(self):
        management = Manager()
        data_list = [self.nombre, self.telefono, self.dpi, self.direccion, self.telefono2]
        management.insert_into_table('paciente', columns_ingreso, data_list)
        # management.print_table('cliente')

    def paciente_delete(self):
        management = Manager()
        management.delete_id_row('paciente', columns_ingreso, self.noPaciente)

    def __str__(self):
        return f"{self.nombre}, {self.telefono}, {self.dpi}, {self.direccion}, {self.telefono2}"