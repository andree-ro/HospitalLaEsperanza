from .manager import Manager

columns_ingreso = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']
columns_ingreso_c = ['id', 'horario', 'descripcion', 'paciente_id', 'doctor_id']


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
            self.paciente_ag()
        elif action == 'up_paciente':
            self.paciente_update()
        elif action == 'del_paciente':
            self.paciente_delete()

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


class Cita:
    def __init__(self, horario, descripcion, paciente_id, doctor_id, columna=None, valor=None, noCita=None):
        self.horario = horario
        self.descripcion = descripcion
        self.paciente_id = paciente_id
        self.doctor_id = doctor_id
        self.columna = columna
        self.valor = valor
        self.noCita = noCita

    def management(self, action):
        if action == 'ag_cita':
            self.cita_ag()
        elif action == 'up_cita':
            self.cita_update()
        elif action == 'del_cita':
            self.cita_delete()

    def cita_update(self):
        management = Manager()
        management.update_table_with_id('citas', columns_ingreso, self.columna, self.valor, self.noCita)

    def cita_ag(self):
        management = Manager()
        data_list = [self.horario, self.descripcion, self.paciente_id, self.doctor_id]
        management.insert_into_table('citas', columns_ingreso, data_list)
        # management.print_table('cliente')

    def cita_delete(self):
        management = Manager()
        management.delete_id_row('citas', columns_ingreso, self.noCita)

    def __str__(self):
        return f"{self.horario}, {self.descripcion}, {self.paciente_id}, {self.doctor_id}"


columns_ingreso_h = ['id', 'nombre', 'edad', 'sexo', 'tipoSangre', 'enfHereditarias', 'padPrevios', 'alergias',
                     'paciente_id', 'observaciones']


class Historial_clinico:
    def __init__(self, nombre, edad, sexo, tipoSangre, enfHereditarias, padPrevios, alergias, paciente_id,
                 observaciones, columna=None, valor=None, noHistoria=None):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.tipoSangre = tipoSangre
        self.enfHereditarias = enfHereditarias
        self.padPrevios = padPrevios
        self.alergias = alergias
        self.paciente_id = paciente_id
        self.observaciones = observaciones
        self.columna = columna
        self.valor = valor
        self.noHistoria = noHistoria

    def management(self, action):
        if action == 'ag_historial':
            self.historia_ag()
        elif action == 'up_historial':
            self.historia_update()
        elif action == 'del_historial':
            self.historia_delete()

    def historia_update(self):
        management = Manager()
        management.update_table_with_id('historialClinico', columns_ingreso, self.columna, self.valor, self.noHistoria)

    def historia_ag(self):
        management = Manager()
        data_list = [self.nombre, self.edad, self.sexo, self.tipoSangre, self.enfHereditarias, self.padPrevios,
                     self.alergias,
                     self.paciente_id, self.observaciones]
        management.insert_into_table('historialClinico', columns_ingreso, data_list)
        # management.print_table('cliente')

    def historia_delete(self):
        management = Manager()
        management.delete_id_row('historialClinico', columns_ingreso, self.noHistoria)

    def __str__(self):
        return (f"{self.nombre}, {self.edad}, {self.sexo}, {self.tipoSangre}, {self.enfHereditarias}, "
                f"{self.padPrevios}, {self.alergias}, {self.paciente_id}, {self.observaciones}")

columns_ingreso_f = ['id', 'nombre', 'nit', 'direccion', 'cita', 'total', 'cita_id']

class Factura_ci:
    def __init__(self, nombre, nit, direccion, cita, total, cita_id, columna=None, valor=None, noFactura_ci=None):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.cita = cita
        self.total = total
        self.cita_id = cita_id
        self.columna = columna
        self.valor = valor
        self.noFactura_ci = noFactura_ci

    def management(self, action):
        if action == 'ag_factura_ci':
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
        data_list = [self.nombre, self.nit, self.direccion, self.cita, self.total, self.cita_id]
        management.insert_into_table('factura_cita', columns_ingreso_f, data_list)
        #management.print_table('factura_cita')

    # def factura_delete(self):
    #     management = Manager()
    #     management.delete_id_row('factura', columns_ingreso_f, self.noFactura)

    def __str__(self):
        return (f"{self.nombre}, {self.nit}, {self.direccion}, {self.cita}, {self.total}, "
                f"{self.cita_id}")
