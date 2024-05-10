from .manager import Manager

columns_ingreso = ['id', 'medicamento', 'dosis', 'horarios', 'descripcion', 'doctor_id', 'paciente_id']


class Receta:
    def __init__(self, medicamento, dosis, horarios, descripcion, doctor_id, paciente_id, columna=None, valor=None, noReceta=None):
        self.medicamento = medicamento
        self.dosis = dosis
        self.horarios = horarios
        self.descripcion = descripcion
        self.doctor_id = doctor_id
        self.paciente_id = paciente_id
        self.columna = columna
        self.valor = valor
        self.noReceta = noReceta

    def management(self, action):
        if action == 'ag_receta':
            self.receta_ag()
        elif action == 'up_receta':
            self.receta_update()
        elif action == 'del_receta':
            self.receta_delete()

    def receta_update(self):
        management = Manager()
        management.update_table_with_id('receta', columns_ingreso, self.columna, self.valor, self.noReceta)

    def receta_ag(self):
        management = Manager()
        data_list = [self.medicamento, self.dosis, self.horarios, self.descripcion, self.doctor_id, self.paciente_id]
        management.insert_into_table('receta', columns_ingreso, data_list)
        # management.print_table('cliente')

    def receta_delete(self):
        management = Manager()
        management.delete_id_row('receta', columns_ingreso, self.noReceta)

    def __str__(self):
        return f"{self.medicamento}, {self.dosis}, {self.horarios}, {self.descripcion}, {self.doctor_id}, {self.paciente_id}"
