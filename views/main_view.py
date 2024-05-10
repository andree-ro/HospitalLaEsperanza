from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import sql_structures
import pandas as pd
from reportlab.lib.pagesizes import legal, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os
from encrypt import *


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('views/CentroMedicoTejutla.ui', self)

        self.frame_modulos.hide()

        # Botones y funciones
        self.btn_inicio_sesion.clicked.connect(self.inicio_sesion)
        self.btn_modulo_farmacia.clicked.connect(self.show_page_farmacia)
        self.btn_modulo_doctor.clicked.connect(self.show_page_doctor)
        self.btn_modulo_paciente.clicked.connect(self.show_page_paciente)
        self.btn_modulo_receta.clicked.connect(self.show_page_receta)
        self.btn_agregar_farmacia.clicked.connect(self.show_page_agregar_i)
        self.btn_actualizar_farmacia.clicked.connect(self.show_page_actualizar_i)
        self.btn_agregar_paciente.clicked.connect(self.show_page_agregar_pac)
        self.btn_actualizar_paciente.clicked.connect(self.show_page_actualizar_pac)
        self.btn_agregarDoctor.clicked.connect(self.show_page_agregar_doc)
        self.btn_actualizarDoc.clicked.connect(self.show_page_actualizar_doc)
        self.btn_modulo_venta.clicked.connect(self.show_page_venta)

        # botones doctor
        self.agregarDoc_btn.clicked.connect(self.registrar_doctor)
        self.actualizarDoc_btn.clicked.connect(self.actualizar_doctor)
        self.tabla_doctores.cellClicked.connect(self.click_tabla_doctor)
        self.btn_eliminar_doctor.clicked.connect(self.eliminar_doctor)
        self.cargar_tabla_doc_btn.clicked.connect(self.carga_tabla_doctor)

        # botones inventario farmacias
        self.agMedicamento_btn.clicked.connect(self.registrar_medicamento)
        self.actualizarMedicamento_btn.clicked.connect(self.actualizar_medicamento)
        self.cargarInventarioMed_btn.clicked.connect(self.carga_tabla_medicamento)
        self.btn_eliminarMedicamento.clicked.connect(self.eliminar_medicamento)
        self.tablaFarmacia.cellClicked.connect(self.click_tabla_medicamento)

        # botones pacientes
        self.agPaciente_btn.clicked.connect(self.registrar_pacientes)
        self.actualizarPaciente_btn.clicked.connect(self.actualizar_pacientes)
        self.cargarInventarioPac_btn.clicked.connect(self.carga_tabla_pacientes)
        self.btn_eliminarPaciente.clicked.connect(self.eliminar_pacientes)
        self.tablaPaciente.cellClicked.connect(self.click_tabla_pacientes)

        # botones venta
        self.btn_realizado_cotizacion.clicked.connect(self.registrar_cotizacion)
        self.btn_realizado_facturacion.clicked.connect(self.registrar_factura)

    # Funcionalidad de botones

    def inicio_sesion(self):
        self.frame_modulos.show()

    def show_page_farmacia(self):
        self.stackedWidget.setCurrentWidget(self.page_farmacia)

    def show_page_venta (self):
        self.stackedWidget.setCurrentWidget(self.page_ventas)

    def show_page_paciente(self):
        self.stackedWidget.setCurrentWidget(self.page_paciente)

    def show_page_doctor(self):
        self.stackedWidget.setCurrentWidget(self.page_doctor)

    def show_page_receta(self):
        self.stackedWidget.setCurrentWidget(self.page_receta)

    def show_page_agregar_i(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def show_page_actualizar_i(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_inventario)

    def show_page_agregar_doc(self):
        self.stackedWidget.setCurrentWidget(self.page_agregar_doctor)

    def show_page_actualizar_doc(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_doctor)

    def show_page_agregar_pac(self):
        self.stackedWidget.setCurrentWidget(self.page_agregar_paciente)

    def show_page_actualizar_pac(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_paciente)

    # Doctor
    def registrar_doctor(self):
        try:
            doctor = sql_structures.Doctor(self.nombreDoc_le.text(),
                                           self.especialidadDoc_le.text(),
                                           self.costCita_ln.text())
            doctor.management('ag_doctor')
            self.nombreDoc_le.clear()
            self.especialidadDoc_le.clear()
            self.costCita_ln.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def actualizar_doctor(self):
        try:
            doctor = sql_structures.Doctor('',
                                           '',
                                           '',
                                           self.datoCambiarDoc_box.currentText(),
                                           self.nuevoValorDoc_le.text(),
                                           self.idActualizarDoc_le.text())
            doctor.management('up_doctor')
            self.idActualizarDoc_le.clear()
            self.nuevoValorDoc_le.clear()
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al actualizar!')

    def eliminar_doctor(self):
        try:
            doctor = sql_structures.Doctor('',
                                           '',
                                           '',
                                           '',
                                           '',
                                           self.id_c)
            doctor.management('del_doctor')
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')
        self.carga_tabla_doctor()

    def click_tabla_doctor(self, row, column):
        manager = sql_structures.Manager()
        item = self.tabla_doctores.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'nombre', 'especialidad', 'cobroCita']
        header_item = self.tabla_doctores.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'ID':
            self.id_c = manager.get('doctor', columns_ingreso, value, 'id')
        elif column_name == 'Nombre':
            self.id_c = manager.get('doctor', columns_ingreso, value, 'nombre')
        elif column_name == 'Especialidad':
            self.id_c = manager.get('doctor', columns_ingreso, value, 'especialidad')
        elif column_name == 'Cita':
            self.id_c = manager.get('doctor', columns_ingreso, value, 'cobroCita')

    def carga_tabla_doctor(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('doctor')
            self.tabla_doctores.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tabla_doctores.setItem(i, 0, QTableWidgetItem(str(dato[i][0])))
                self.tabla_doctores.setItem(i, 1, QTableWidgetItem(str(dato[i][1])))
                self.tabla_doctores.setItem(i, 2, QTableWidgetItem(str(dato[i][2])))
                self.tabla_doctores.setItem(i, 3, QTableWidgetItem(str(dato[i][3])))
        except Exception as e:
            print(e)

    # Inventario Medicamentos
    def registrar_medicamento(self):
        try:
            medicina = sql_structures.InventarioFarmacia(self.nombreMedicamento_le.text(),
                                                         self.cantMedicamento_ln.text(),
                                                         self.descMedicamento_le.text(),
                                                         self.precioMedicamento_le.text(),
                                                         self.fechaMedicamento_le.text())
            medicina.management('ag_inventarioFarmacia')
            self.nombreMedicamento_le.clear()
            self.cantMedicamento_ln.clear()
            self.descMedicamento_le.clear()
            self.precioMedicamento_le.clear()
            self.fechaMedicamento_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def actualizar_medicamento(self):
        try:
            medicamento = sql_structures.InventarioFarmacia('',
                                                            '',
                                                            '',
                                                            '',
                                                            '',
                                                            self.datoCambiarMed_box.currentText(),
                                                            self.nuevoValorMed_le.text(),
                                                            self.idActualizarMed_le.text())
            medicamento.management('up_inventarioFarmacia')
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al actualizar!')

    def eliminar_medicamento(self):
        try:
            medicina = sql_structures.InventarioFarmacia('',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         self.id_c)
            medicina.management('del_inventarioFarmacia')
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')
        self.carga_tabla_medicamento()

    def click_tabla_medicamento(self, row, column):
        manager = sql_structures.Manager()
        item = self.tablaFarmacia.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'nombre', 'cantidad', 'descripcion', 'precio', 'fecha_de_vencimiento']
        header_item = self.tablaFarmacia.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'Nombre':
            self.id_c = manager.get('inventariofarmacia', columns_ingreso, value, 'nombre')
        elif column_name == 'Cantidad':
            self.id_c = manager.get('inventariofarmacia', columns_ingreso, value, 'cantidad')
        elif column_name == 'Descripcion':
            self.id_c = manager.get('inventariofarmacia', columns_ingreso, value, 'descripcion')
        elif column_name == 'Precio':
            self.id_c = manager.get('inventariofarmacia', columns_ingreso, value, 'precio')
        elif column_name == 'Fecha_Ven':
            self.id_c = manager.get('inventariofarmacia', columns_ingreso, value, 'fecha_ven')

    def carga_tabla_medicamento(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('inventariofarmacia')
            self.tablaFarmacia.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tablaFarmacia.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablaFarmacia.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablaFarmacia.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tablaFarmacia.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tablaFarmacia.setItem(i, 4, QTableWidgetItem(str(dato[i][5])))
        except Exception as e:
            print(e)

# Inventario Medicamentos
    def registrar_pacientes(self):
        try:
            paciente = sql_structures.Paciente(self.nombrePaciente_le.text(),
                                               self.telefonoPaciente_le.text(),
                                               self.dpiPaciente_le.text(),
                                               self.direccionPaciente_le.text(),
                                               self.telefono2Paciente_le.text())
            paciente.management('ag_paciente')
            self.nombrePaciente_le.clear()
            self.telefonoPaciente_le.clear()
            self.dpiPaciente_le.clear()
            self.direccionPaciente_le.clear()
            self.telefono2Paciente_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def actualizar_pacientes(self):
        try:
            paciente = sql_structures.Paciente('',
                                               '',
                                               '',
                                               '',
                                               '',
                                               self.datoCambiarPac_box.currentText(),
                                               self.nuevoValorPac_le.text(),
                                               self.idActualizarPac_le.text())
            paciente.management('up_paciente')
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al actualizar!')

    def eliminar_pacientes(self):
        try:
            paciente = sql_structures.Paciente('',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         self.id_c)
            paciente.management('del_paciente')
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')
        self.carga_tabla_pacientes()

    def click_tabla_pacientes(self, row, column):
        manager = sql_structures.Manager()
        item = self.tablaPaciente.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']
        header_item = self.tablaPaciente.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'Nombre':
            self.id_c = manager.get('paciente', columns_ingreso, value, 'nombre')
        elif column_name == 'Teléfono':
            self.id_c = manager.get('paciente', columns_ingreso, value, 'telefono')
        elif column_name == 'DPI':
            self.id_c = manager.get('paciente', columns_ingreso, value, 'dpi')
        elif column_name == 'Dirección':
            self.id_c = manager.get('paciente', columns_ingreso, value, 'direccion')
        elif column_name == 'Teléfono 2':
            self.id_c = manager.get('paciente', columns_ingreso, value, 'telefono2')

    def carga_tabla_pacientes(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('paciente')
            self.tablaPaciente.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tablaPaciente.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablaPaciente.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablaPaciente.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tablaPaciente.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tablaPaciente.setItem(i, 4, QTableWidgetItem(str(dato[i][5])))
        except Exception as e:
            print(e)

    # Ventas factura
    def registrar_factura(self):
        try:
            columns_ingreso = ['id', 'nombre', 'cantidad', 'descripcion', 'precio', 'fecha_de_vencimiento']
            cantidad = self.cantidadFactura_le.text()
            precio = self.precioFactura_le.text()
            total = int(cantidad) * int(precio)
            pro = self.productofactura_le.text()
            mana = sql_structures.Manager()
            id_far = mana.get("inventariofarmacia", columns_ingreso, pro, "nombre")
            factura = sql_structures.Factura(self.nombreVenta_le.text(),
                                               self.nitVenta_le.text(),
                                               self.direccionVenta_le.text(),
                                               self.productofactura_le.text(),
                                               total,
                                               id_far,
                                               self.usuarioVenta_le.text())
            factura.management('ag_factura ')
            self.nombreVenta_le.clear()
            self.nitVenta_le.clear()
            self.direccionVenta_le.clear()
            self.productofactura_le.clear()
            self.precioFactura_le.clear()
            self.cantidadFactura_le.clear()
            self.usuarioVenta_le.clear()
            vie_Can = mana.gett("inventariofarmacia", "cantidad", "id", id_far)
            nue_Can = int(vie_Can) - int(cantidad)
            medicamento = sql_structures.InventarioFarmacia('',
                                                            '',
                                                            '',
                                                            '',
                                                            '',
                                                            "cantidad",
                                                            nue_Can,
                                                            id_far)
            medicamento.management('up_inventarioFarmacia')
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente el inventario!')
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    # Ventas cotizacion
    def registrar_cotizacion(self):
        try:
            columns_ingreso = ['id', 'nombre', 'cantidad', 'descripcion', 'precio', 'fecha_de_vencimiento']
            cantidad = self.cantidadCotizacion_le.text()
            precio = self.precioCotizacion_le.text()
            total = int(cantidad) * int(precio)
            pro = self.productoCotizacion_le.text()
            mana = sql_structures.Manager()
            id_far = mana.gett("inventariofarmacia", columns_ingreso, "nombre", pro)
            cotizacion = sql_structures.Cotizacion(self.nombreVenta_le.text(),
                                               self.nitVenta_le.text(),
                                               self.direccionVenta_le.text(),
                                               self.productoCotizacion_le.text(),
                                                   total,
                                                   id_far)
            cotizacion.management('ag_cotizacion')
            self.nombreVenta_le.clear()
            self.nitVenta_le.clear()
            self.direccionVenta_le.clear()
            self.productoCotizacion_le.clear()
            self.cantidadCotizacion_le.clear()
            self.precioCotizacion_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

# receta
    def registrar_receta(self):
        try:
            columns_ingreso = ['id', 'nombre', 'especialidad', 'cobroCita']
            doc = self.docReceta_le.text()
            mana = sql_structures.Manager()
            id_doc = mana.gett("doctor", columns_ingreso, "nombre", doc)
            #####
            columns_ingreso_pac = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']
            pac = self.pacReceta_le.text()
            mana = sql_structures.Manager()
            id_pac = mana.gett("paciente", columns_ingreso_pac, "nombre", pac)
            receta = sql_structures.Receta(self.medicamentoReceta_le.text(),
                                               self.dosisReceta_le.text(),
                                               self.horarioReceta_le.text(),
                                               self.descripcionReceta_le.text(),
                                                   id_doc,
                                                   id_pac)
            receta.management('ag_receta')
            self.medicamentoReceta_le.clear()
            self.dosisReceta_le.clear()
            self.horarioReceta_le.clear()
            self.descripcionReceta_le.clear()
            self.docReceta_le.clear()
            self.pacReceta_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def actualizar_pacientes(self):
        try:
            paciente = sql_structures.Paciente('',
                                               '',
                                               '',
                                               '',
                                               '',
                                               self.datoCambiarReceta_box.currentText(),
                                               self.nuevoValorReceta_le.text(),
                                               self.idActualizarReceta_le.text())
            paciente.management('up_receta')
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al actualizar!')

    def eliminar_pacientes(self):
        try:
            paciente = sql_structures.Paciente('',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         self.id_c)
            paciente.management('del_paciente')
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')
        self.carga_tabla_receta()

    def click_tabla_receta(self, row, column):
        manager = sql_structures.Manager()
        item = self.tablaReceta.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'medicamento', 'dosis', 'horarios', 'descripcion', 'doctor_id', 'paciente_id']
        header_item = self.tablaReceta.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'Medicamento':
            self.id_c = manager.get('recetase', columns_ingreso, value, 'medicamento')
        elif column_name == 'Dosis':
            self.id_c = manager.get('recetas', columns_ingreso, value, 'dosis')
        elif column_name == 'Horarios':
            self.id_c = manager.get('recetas', columns_ingreso, value, 'horarios')
        elif column_name == 'Descripción':
            self.id_c = manager.get('recetas', columns_ingreso, value, 'descripcion')
        elif column_name == 'Doctor':
            self.id_c = manager.get('recetas', columns_ingreso, value, 'doctor_id')
        elif column_name == 'Paciente':
            self.id_c = manager.get('recetas', columns_ingreso, value, 'paciente_id')

    def carga_tabla_receta(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('recetas')
            self.tablaReceta.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tablaReceta.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablaReceta.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablaReceta.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tablaReceta.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tablaReceta.setItem(i, 4, QTableWidgetItem(str(dato[i][5])))
        except Exception as e:
            print(e)