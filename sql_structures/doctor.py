from .manager import Manager

columns_ingreso = ['id', 'nombre', 'especialidad', 'cobroCita']


class Doctor:
    def __init__(self, nombre, especialidad, cobroCita, columna=None, valor=None, noDoctor=None):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cobroCita = cobroCita
        self.columna = columna
        self.valor = valor
        self.noDoctor = noDoctor

    def management(self, action):
        if action == 'ag_doctor':
            self.doctor_ag()
        elif action == 'up_doctor':
            self.doctor_update()
        elif action == 'del_doctor':
            self.doctor_delete()

    def doctor_update(self):
        management = Manager()
        management.update_table_with_id('doctor', columns_ingreso, self.columna, self.valor, self.noDoctor)

    def doctor_ag(self):
        management = Manager()
        data_list = [self.nombre, self.especialidad, self.cobroCita]
        management.insert_into_table('doctor', columns_ingreso, data_list)
        # management.print_table('cliente')

    def doctor_delete(self):
        management = Manager()
        management.delete_id_row('doctor', columns_ingreso, self.noDoctor)

    def __str__(self):
        return f"{self.nombre}, {self.especialidad}, {self.cobroCita}"