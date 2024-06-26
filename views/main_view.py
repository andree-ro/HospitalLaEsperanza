from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import sql_structures
from datetime import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import webbrowser
from encrypt import *


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('views/CentroMedicoTejutla.ui', self)
        # Patrón Adapter
        # Decorator

        self.frame_modulos.hide()

        self.productos = []
        self.recetas = []
        self.aux: int = 0
        self.idFactura = 0
        self.today = date.today()
        self.acumulador = 1
        self.total = 0
        # Botones y funciones
        #        self.btn_inicio_sesion.clicked.connect(self.inicio_sesion)
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
        self.btn_actualizarDoc.clicked.connect(self.show_page_actualizar_doc)
        self.btn_modulo_venta.clicked.connect(self.show_page_venta)
        self.btn_agregar_receta.clicked.connect(self.show_page_agregar_rece)
        self.btn_actualizar_Receta.clicked.connect(self.show_page_actualizar_rece)
        self.btn_Citas.clicked.connect(self.show_page_cita)
        self.btn_agregar_Cita.clicked.connect(self.show_page_agregar_cit)
        self.btn_actualizar_cita.clicked.connect(self.show_page_actualizar_cit)
        self.btn_modulo_usuario.clicked.connect(self.show_page_usuario)

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
        self.btn_historial.clicked.connect(self.show_page_historial)
        self.btn_agregar_historial.clicked.connect(self.show_page_agregar_historial)
        self.btn_factura_cita.clicked.connect(self.show_page_factura)

        # botones venta
        # self.btn_realizado_cotizacion.clicked.connect(self.registrar_cotizacion)
        # self.btn_realizado_facturacion.clicked.connect(self.registrar_factura)

        # Factura Cotizacion
        self.agregarFactura.clicked.connect(self.agregar_a_Factura)
        self.realizado_facturacion.clicked.connect(self.generarFactura)
        self.agregarCotizacion.clicked.connect(self.agregar_a_cotizacion)
        self.realizado_cotizacion.clicked.connect(self.generarCotizacion)
        #       self.generarFacCitas.clicked.connect(self.generarFacturaCita)

        # Receta
        self.agregarReceta_btn.clicked.connect(self.registrar_receta)
        self.actualizarReceta_btn.clicked.connect(self.actualizar_receta)
        self.cargarReceta_btn.clicked.connect(self.carga_tabla_receta)
        self.btn_eliminar_Receta.clicked.connect(self.eliminar_receta)
        self.tablaReceta.cellClicked.connect(self.click_tabla_receta)

        # Receta
        self.agCita_btn.clicked.connect(self.registrar_cita)
        self.actualizarCita_btn.clicked.connect(self.actualizar_cita)
        self.cargar_Cita.clicked.connect(self.carga_tabla_cita)
        self.btn_eliminar_Cita.clicked.connect(self.eliminar_cita)
        self.tablaCita.cellClicked.connect(self.click_tabla_cita)

        self.aghisto_btn.clicked.connect(self.registrar_historia)
        #self.actualizarCita_btn.clicked.connect(self.actualizar_cita)
        self.cargar_histo.clicked.connect(self.carga_tabla_historial)
        self.btn_eliminar_histo.clicked.connect(self.eliminar_historia)
        self.tablahistorial.cellClicked.connect(self.click_tabla_historia)

        self.realizado_faccita.clicked.connect(self.registrar_factura_ci)

        self.generarReceta_btn.clicked.connect(self.generarReceta)

        self.btn_agregar_usuario.clicked.connect(self.show_page_agregarusuario)
        self.btn_actualizar_usuario.clicked.connect(self.show_page_actualizarusuario)
        self.actualizarUsuario_btn.clicked.connect(self.new_user)
        self.actualizarUsuari_btn.clicked.connect(self.update_user)
        self.btn_eliminarUsuario.clicked.connect(self.delete_user)
        self.tablaUsuario.cellClicked.connect(self.click_tabla_usuario)
        self.cargarUsu_btn.clicked.connect(self.carga_tabla_Usuario)

        self.btn_inicio_sesion.clicked.connect(self.iniciar_sesion)
        self.Manualbtn.clicked.connect(self.abrir_manual)

    # Funcionalidad de botones

    # def inicio_sesion(self):
    #     self.frame_modulos.show()

    # Patrón strategy

    def show_page_farmacia(self):
        self.stackedWidget.setCurrentWidget(self.page_farmacia)
        self.carga_tabla_medicamento()

    def show_page_venta(self):
        self.stackedWidget.setCurrentWidget(self.page_ventas)

    def show_page_paciente(self):
        self.stackedWidget.setCurrentWidget(self.page_paciente)
        self.carga_tabla_pacientes()

    def show_page_usuario(self):
        self.stackedWidget.setCurrentWidget(self.page_usuarios)
        self.carga_tabla_Usuario()

    def show_page_agregarusuario(self):
        self.stackedWidget.setCurrentWidget(self.page_agregar_usuario)

    def show_page_actualizarusuario(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_usuario)

    def show_page_doctor(self):
        self.stackedWidget.setCurrentWidget(self.page_doctor)
        self.carga_tabla_doctor()

    def show_page_receta(self):
        self.stackedWidget.setCurrentWidget(self.page_receta)
        self.carga_tabla_receta()

    def show_page_cita(self):
        self.stackedWidget.setCurrentWidget(self.page_cita)
        self.carga_tabla_cita()

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

    def show_page_agregar_rece(self):
        self.stackedWidget.setCurrentWidget(self.page_agregar_receta)

    def show_page_actualizar_rece(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_Receta)

    def show_page_agregar_cit(self):
        self.stackedWidget.setCurrentWidget(self.page_agregar_cita)

    def show_page_actualizar_cit(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_Cita)

    def show_page_historial(self):
        self.stackedWidget.setCurrentWidget(self.page_historial_clinico)
        self.carga_tabla_historial()

    def show_page_agregar_historial(self):
        self.stackedWidget.setCurrentWidget(self.page_agrega_historial)

    def show_page_factura(self):
        self.stackedWidget.setCurrentWidget(self.page_Factura_Citas)

    # def show_page_factura_cita(self):
    #     self.stackedWidget.setCurrentWidget(self.page_Factura_Citas)

    # Patrón Factory Method
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
        self.show_page_doctor()

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
        self.show_page_doctor()

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
        self.show_page_farmacia()

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
        self.show_page_farmacia()

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
        self.show_page_paciente()

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
        self.show_page_paciente()

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

    # FACTURAS
    def agregar_a_Factura(self):
        print('1')
        producto = self.productofactura_le.text()
        print('1')
        cantidad = int(self.cantidadFactura_le.text())
        print('1')
        precioUnidad = float(self.precioFactura_le.text())
        print('2')
        if self.aux == 0:
            print('3')
            self.productos.append({
                "cantidad": cantidad,
                "producto": producto,
                "precioUnidad": precioUnidad,
                "subtotal": (cantidad * precioUnidad)
            })
            self.aux = 1
        else:
            print('4')
            encontrado = False
            for p in self.productos:

                if p["producto"] == producto:
                    encontrado = True
                    cantidadNueva = int(p['cantidad']) + int(cantidad)
                    self.productos[self.productos.index(p)] = {
                        "cantidad": cantidadNueva,
                        "producto": producto,
                        "precioUnidad": precioUnidad,
                        "subtotal": (cantidadNueva * precioUnidad)
                    }
                    break
            if not encontrado:
                self.productos.append({
                    "cantidad": cantidad,
                    "producto": producto,
                    "precioUnidad": precioUnidad,
                    "subtotal": (cantidad * precioUnidad)
                })
        self.productofactura_le.clear()
        self.cantidadFactura_le.clear()
        self.precioFactura_le.clear()

    def generarFactura(self):
        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')
        # crear pdf
        pdf = canvas.Canvas(f"factura{self.idFactura}.pdf")
        pdf.setFont("Helvetica", 12)
        usuario = str(self.usuarioVenta_le.text())
        nombre = str(self.nombreVenta_le.text())
        nit = str(self.nitVenta_le.text())
        direccion = str(self.direccionVenta_le.text())
        idFactura = f"{self.today.day}{self.today.month}{self.acumulador}"

        pdf.drawString(100, 720, "Usuario" + str(usuario))
        pdf.drawString(100, 700, "Nombre: " + str(nombre))
        pdf.drawString(100, 680, "NIT: " + str(nit))
        pdf.drawString(100, 660, "Dirección: " + str(direccion))
        pdf.drawString(400, 700, "Factura:" + str(idFactura))
        pdf.drawString(400, 680, "Fecha:" + str(formato))
        pdf.drawString(50, 620, "CANTIDAD")
        pdf.drawString(150, 620, "PRODUCTO")
        pdf.drawString(225, 620, "PRECIO UNIDAD")
        pdf.drawString(375, 620, "SUBTOTAL")
        y = 600  # Posición vertical inicial
        for producto in self.productos:
            if y < 50:  # Ejemplo de margen inferior
                break  # Salir del bucle si la posición y es demasiado baja
            pdf.drawString(50, y, str(producto["cantidad"]))
            pdf.drawString(150, y, str(producto["producto"]))
            pdf.drawString(225, y, str(producto["precioUnidad"]))
            pdf.drawString(375, y, str(producto["subtotal"]))
            y -= 20
        for producto in self.productos:
            total = float(producto["precioUnidad"]) * int(producto["cantidad"])
            self.total = total + self.total
        pdf.drawString(400, y - 20, "Total: " + str(self.total))
        pdf.save()
        factura = f"factura{self.idFactura}.pdf"
        webbrowser.open_new(factura)
        self.productos.clear()
        self.total = 0
        self.acumulador += 1
        self.registrar_factura()

    def agregar_a_cotizacion(self):
        print('1')
        producto = str(self.productoCotizacion_le.text())
        print('1')
        cantidad = int(self.cantidadCotizacion_le.text())
        print('1')
        precioUnidad = float(self.precioCotizacion_le.text())
        print('1')
        if self.aux == 0:
            self.productos.append({
                "cantidad": cantidad,
                "producto": producto,
                "precioUnidad": precioUnidad,
                "subtotal": (cantidad * precioUnidad)
            })
            self.aux = 1
            print('1')
        else:
            print('1')
            encontrado = False
            for p in self.productos:
                print('1')
                if p["producto"] == producto:
                    encontrado = True
                    cantidadNueva = int(p['cantidad']) + int(cantidad)
                    self.productos[self.productos.index(p)] = {
                        "cantidad": cantidadNueva,
                        "producto": producto,
                        "precioUnidad": precioUnidad,
                        "subtotal": (cantidadNueva * precioUnidad)
                    }
                    print('1')
                    break
            print('1')
            if not encontrado:
                print('1')
                self.productos.append({
                    "cantidad": cantidad,
                    "producto": producto,
                    "precioUnidad": precioUnidad,
                    "subtotal": (cantidad * precioUnidad)
                })
                print('1')
        self.productoCotizacion_le.clear()
        self.cantidadCotizacion_le.clear()
        self.precioCotizacion_le.clear()

    def generarCotizacion(self):
        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')
        # crear pdf
        pdf = canvas.Canvas(f"cotizacion.pdf")
        pdf.setFont("Helvetica", 12)
        usuario = str(self.usuarioVenta_le.text())
        nombre = str(self.nombreVenta_le.text())
        nit = str(self.nitVenta_le.text())
        direccion = str(self.direccionVenta_le.text())

        pdf.drawString(100, 720, "Usuario" + str(usuario))
        pdf.drawString(100, 700, "Nombre: " + str(nombre))
        pdf.drawString(100, 680, "NIT: " + str(nit))
        pdf.drawString(100, 660, "Dirección: " + str(direccion))
        pdf.drawString(400, 700, "Factura:" + str('----'))
        pdf.drawString(400, 680, "Fecha:" + str(formato))
        pdf.drawString(50, 620, "CANTIDAD")
        pdf.drawString(150, 620, "PRODUCTO")
        pdf.drawString(225, 620, "PRECIO UNIDAD")
        pdf.drawString(375, 620, "SUBTOTAL")
        y = 600  # Posición vertical inicial
        for producto in self.productos:
            if y < 50:  # Ejemplo de margen inferior
                break  # Salir del bucle si la posición y es demasiado baja
            pdf.drawString(50, y, str(producto["cantidad"]))
            pdf.drawString(150, y, str(producto["producto"]))
            pdf.drawString(225, y, str(producto["precioUnidad"]))
            pdf.drawString(375, y, str(producto["subtotal"]))
            y -= 20
        for producto in self.productos:
            total = float(producto["precioUnidad"]) * int(producto["cantidad"])
            self.total = total + self.total
        pdf.drawString(400, y - 20, "Total: " + str(self.total))
        pdf.save()
        cotizacion = f"cotizacion.pdf"
        webbrowser.open_new(cotizacion)
        self.productos.clear()
        self.total = 0
        self.acumulador += 1
        self.registrar_cotizacion()

    def generarFacturaCita(self):
        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')

        # Crear pdf
        pdf = canvas.Canvas(f"facturaCita{self.idFactura}.pdf", pagesize=letter)
        pdf.setFont("Helvetica", 12)

        nombre = str(self.nombreFaccita_le.text())
        nit = str(self.nitFaccita_le.text())
        direccion = str(self.direccionFaccita_le.text())
        motivo = str(self.Motivofaccita_le.text())
        total = str(self.totalfaccita_le.text())
        idFactura = f"{self.today.day}{self.today.month}{self.acumulador}"

        pdf.drawString(100, 700, "Nombre: " + nombre)
        pdf.drawString(100, 680, "NIT: " + nit)
        pdf.drawString(100, 660, "Dirección: " + direccion)
        pdf.drawString(400, 700, "Factura: " + idFactura)
        pdf.drawString(400, 680, "Fecha: " + formato)
        pdf.drawString(50, 620, "MOTIVO DE LA CITA")

        # Implementar salto de línea para el motivo
        maximo_caracteres = 80
        yPosicion = 600
        linea = [motivo[i:i + maximo_caracteres] for i in range(0, len(motivo), maximo_caracteres)]
        for i in linea:
            pdf.drawString(50, yPosicion, i)
            yPosicion -= 20  # Ajustar el espacio entre líneas

        # Posición vertical inicial para productos
        y = yPosicion - 20
        for producto in self.productos:
            if y < 50:  # Ejemplo de margen inferior
                break  # Salir del bucle si la posición y es demasiado baja
            y -= 20
            pdf.drawString(50, y, str(producto))  # Asumiendo que `producto` es una cadena

        pdf.drawString(400, y - 20, "Total: Q" + total)
        pdf.save()

        factura = f"facturaCita{self.idFactura}.pdf"
        webbrowser.open_new(factura)
        self.productos.clear()
        self.total = 0
        self.acumulador += 1

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
        self.show_page_farmacia()

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
        self.show_page_farmacia()

    # receta
    def registrar_receta(self):
        try:
            columns_ingreso = ['id', 'nombre', 'especialidad', 'cobroCita']
            doc = self.docReceta_le.text()
            mana = sql_structures.Manager()
            id_doc = mana.get("doctor", columns_ingreso, doc, "nombre")
            #####
            columns_ingreso_pac = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']
            pac = self.pacReceta_le.text()
            mana = sql_structures.Manager()
            id_pac = mana.get("paciente", columns_ingreso_pac, pac, "nombre")
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
        self.show_page_receta()

    def actualizar_receta(self):
        try:
            receta = sql_structures.Receta('',
                                           '',
                                           '',
                                           '',
                                           '', '',
                                           self.datoCambiarReceta_box.currentText(),
                                           self.nuevoValorReceta_le.text(),
                                           self.idActualizarReceta_le.text())
            receta.management('up_receta')
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al actualizar!')
        self.show_page_receta()

    def eliminar_receta(self):
        try:
            receta = sql_structures.Receta('',
                                           '',
                                           '',
                                           '',
                                           '',
                                           '',
                                           '', '',
                                           self.id_c)
            receta.management('del_receta')
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
            self.id_c = manager.get('recetas', columns_ingreso, value, 'medicamento')
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
                vie_Can = mana.gett("doctor", "nombre", "id", dato[i][5])
                vie_Ca = mana.gett("paciente", "nombre", "id", dato[i][6])
                self.tablaReceta.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablaReceta.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablaReceta.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tablaReceta.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tablaReceta.setItem(i, 4, QTableWidgetItem(str(vie_Can)))
                self.tablaReceta.setItem(i, 5, QTableWidgetItem(str(vie_Ca)))
        except Exception as e:
            print(e)

    # receta
    def registrar_cita(self):
        try:
            columns_ingreso = ['id', 'nombre', 'especialidad', 'cobroCita']
            doc = self.doctorCita_le.text()
            mana = sql_structures.Manager()
            id_doc = mana.get("doctor", columns_ingreso, doc, "nombre")
            #####
            columns_ingreso_pac = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']
            pac = self.pacienteCita_le.text()
            mana = sql_structures.Manager()
            id_pac = mana.get("paciente", columns_ingreso_pac, pac, "nombre")
            cita = sql_structures.Cita(self.horarioCita_le.text(),
                                       self.descripcionCita_ln.text(),
                                       id_doc,
                                       id_pac)
            cita.management('ag_cita')
            self.horarioCita_le.clear()
            self.descripcionCita_ln.clear()
            self.pacienteCita_le.clear()
            self.doctorCita_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')
        self.show_page_cita()

    def actualizar_cita(self):
        try:
            cita = sql_structures.Cita('',
                                       '',
                                       '', '',
                                       self.datoCambiarCita_box.currentText(),
                                       self.nuevoValorCita_le.text(),
                                       self.idActualizarCita_le.text())
            cita.management('up_cita')
            QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al actualizar!')
        self.show_page_cita()

    def eliminar_cita(self):
        try:
            cita = sql_structures.Cita('',
                                       '',
                                       '',
                                       '',
                                       '',
                                       '',
                                       self.id_c)
            cita.management('del_cita')
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')
        self.carga_tabla_cita()

    def click_tabla_cita(self, row, column):
        manager = sql_structures.Manager()
        item = self.tablaCita.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'horario', 'descripcion', 'paciente_id', 'doctor_id']
        header_item = self.tablaCita.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'Horarios':
            self.id_c = manager.get('citas', columns_ingreso, value, 'horarios')
        elif column_name == 'Descripción':
            self.id_c = manager.get('citas', columns_ingreso, value, 'descripcion')
        elif column_name == 'Doctor':
            self.id_c = manager.get('citas', columns_ingreso, value, 'doctor_id')
        elif column_name == 'Paciente':
            self.id_c = manager.get('citas', columns_ingreso, value, 'paciente_id')

    def carga_tabla_cita(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('citas')
            self.tablaCita.setRowCount(len(dato))
            for i in range(len(dato)):
                vie_Can = mana.gett("doctor", "nombre", "id", dato[i][4])
                vie_Ca = mana.gett("paciente", "nombre", "id", dato[i][3])
                self.tablaCita.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablaCita.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablaCita.setItem(i, 2, QTableWidgetItem(str(vie_Ca)))
                self.tablaCita.setItem(i, 3, QTableWidgetItem(str(vie_Can)))
        except Exception as e:
            print(e)

    def registrar_historia(self):
        try:
            historial = sql_structures.Historial_clinico(self.nombreHistorial_le.text(),
                                                         self.edadHistorial_le.text(),
                                                         self.sexoHistorial_le.text(),
                                                         self.tipoHistorial_le.text(),
                                                         self.enfHistorial_le.text(),
                                                         self.padHistorial_le.text(),
                                                         self.alergiaHistorial_le.text(),
                                                         self.id_paHistorial_le.text(),
                                                         self.obseHistorial_le.text())
            historial.management('ag_historial')
            self.nombreHistorial_le.clear()
            self.edadHistorial_le.clear()
            self.sexoHistorial_le.clear()
            self.tipoHistorial_le.clear()
            self.enfHistorial_le.clear()
            self.padHistorial_le.clear()
            self.alergiaHistorial_le.clear()
            self.id_paHistorial_le.clear()
            self.obseHistorial_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')
        self.show_page_historial()

    # def actualizar_pacientes(self):
    #     try:
    #         paciente = sql_structures.Paciente('',
    #                                            '',
    #                                            '',
    #                                            '',
    #                                            '',
    #                                            self.datoCambiarPac_box.currentText(),
    #                                            self.nuevoValorPac_le.text(),
    #                                            self.idActualizarPac_le.text())
    #         paciente.management('up_paciente')
    #         QMessageBox.about(self, 'Aviso', 'Actualizado correctamente!')
    #     except Exception as e:
    #         print(e)
    #         QMessageBox.about(self, 'Aviso', 'Error al actualizar!')

    def eliminar_historia(self):
        try:
            historial = sql_structures.Historial_clinico('',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '',
                                                         '', '',
                                                         '', '',
                                                         '',
                                                         self.id_c)
            historial.management('del_historial')
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')
        self.carga_tabla_historial()

    def click_tabla_historia(self, row, column):
        manager = sql_structures.Manager()
        item = self.tablahistorial.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'nombre', 'edad', 'sexo', 'tipoSangre', 'enfHereditarias', 'padPrevios', 'alergias',
                           'paciente_id', 'observaciones']
        header_item = self.tablahistorial.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'Nombre':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'nombre')
        elif column_name == 'Edad':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'edad')
        elif column_name == 'Sexo':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'sexo')
        elif column_name == 'Tipo de Sangre':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'tipoSangre')
        elif column_name == 'Enfermedades Hereditarias':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'enfHereditarias')
        elif column_name == 'Padecimientos previos':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'padPrevios')
        elif column_name == 'Alergias':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'alergias')
        elif column_name == 'paciente_id':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'paciente_id')
        elif column_name == 'observaciones':
            self.id_c = manager.get('historialClinico', columns_ingreso, value, 'observaciones')

    def carga_tabla_historial(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('historialClinico')
            self.tablahistorial.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tablahistorial.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablahistorial.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablahistorial.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tablahistorial.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tablahistorial.setItem(i, 4, QTableWidgetItem(str(dato[i][5])))
                self.tablahistorial.setItem(i, 5, QTableWidgetItem(str(dato[i][6])))
                self.tablahistorial.setItem(i, 6, QTableWidgetItem(str(dato[i][7])))
                self.tablahistorial.setItem(i, 7, QTableWidgetItem(str(dato[i][8])))
                self.tablahistorial.setItem(i, 8, QTableWidgetItem(str(dato[i][9])))
        except Exception as e:
            print(e)

    def registrar_factura_ci(self):
        try:
            columns_ingreso = ['id', 'horario', 'descripcion', 'paciente_id', 'doctor_id']
            columna = ['id', 'nombre', 'telefono', 'dpi', 'direccion', 'telefono2']
            pro = self.nombreFaccita_le.text()
            mana = sql_structures.Manager()
            id_pa = mana.get("Paciente", columna, pro, "nombre")
            id_far = mana.get("citas", columns_ingreso, id_pa, "id")
            print(id_far)
            factu = sql_structures.Factura_ci(self.nombreFaccita_le.text(),
                                              self.nitFaccita_le.text(),
                                              self.direccionFaccita_le.text(),
                                              self.Motivofaccita_le.text(),
                                              self.totalfaccita_le.text(),
                                              id_far)
            factu.management('ag_factura_ci')
            self.nombreFaccita_le.clear()
            self.nitFaccita_le.clear()
            self.direccionFaccita_le.clear()
            self.Motivofaccita_le.clear()
            self.totalfaccita_le.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')
        self.show_page_cita()

    # Receta

    def generarReceta(self):
        now = datetime.now()
        formato = now.strftime('%d-%m-%Y')
        medicamento = str(self.medicamentoReceta_le.text())
        dosis = str(self.dosisReceta_le.text())
        horario = str(self.horarioReceta_le.text())
        descripcion = str(self.descripcionReceta_le.text())
        doctor = str(self.docReceta_le.text())
        paciente = str(self.pacReceta_le.text())

        # Crear pdf
        pdf = canvas.Canvas(f"{paciente}{formato}.pdf", pagesize=letter)
        pdf.setFont("Helvetica", 12)

        pdf.drawString(100, 700, "Nombre: " + paciente)
        pdf.drawString(100, 660, "Doctor: " + doctor)
        pdf.drawString(400, 680, "Fecha: " + formato)
        pdf.drawString(50, 620, "DOSIS")
        pdf.drawString(200, 620, "MEDICAMENTO")
        pdf.drawString(350, 620, "HORARIO")
        pdf.drawString(500, 620, "DESCRIPCION")

        # Implementar salto de línea para el motivo
        yPosicion = 600

        # Dividir los textos por comas
        dosis_list = dosis.split(",")
        medicamento_list = medicamento.split(",")
        horario_list = horario.split(",")
        descripcion_list = descripcion.split(",")

        max_lineas = max(len(dosis_list), len(medicamento_list), len(horario_list), len(descripcion_list))

        for i in range(max_lineas):
            dosis_line = dosis_list[i] if i < len(dosis_list) else ""
            medicamento_line = medicamento_list[i] if i < len(medicamento_list) else ""
            horario_line = horario_list[i] if i < len(horario_list) else ""
            descripcion_line = descripcion_list[i] if i < len(descripcion_list) else ""

            pdf.drawString(50, yPosicion, dosis_line)
            pdf.drawString(200, yPosicion, medicamento_line)
            pdf.drawString(350, yPosicion, horario_line)
            pdf.drawString(500, yPosicion, descripcion_line)
            yPosicion -= 20  # Ajustar el espacio entre líneas

        # Posición vertical inicial para productos
        y = yPosicion - 20
        for producto in self.productos:
            if y < 50:  # Ejemplo de margen inferior
                break  # Salir del bucle si la posición y es demasiado baja
            y -= 20
            pdf.drawString(50, y, str(producto))  # Asumiendo que `producto` es una cadena

        pdf.save()

        factura = f"{paciente}{formato}.pdf"
        webbrowser.open_new(factura)
        self.productos.clear()
        self.total = 0
        self.acumulador += 1

    def new_user(self):
        try:
            usuarios = sql_structures.SqlDataBase_usuarios(self.info_usuario.text(),
                                                           self.info_contrasena.text(),
                                                           self.info_rol.currentText())
            usuarios.new_user()
            self.info_usuario.clear()
            self.info_contrasena.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')
        self.show_page_usuario()

    def update_user(self):
        try:
            usuarios = sql_structures.SqlDataBase_usuarios("", "", "",
                                                           self.datoCambiarUsu_box.currentText(),
                                                           self.nuevoValorMed_le.text(),
                                                           self.idActualizarUsu_le.text())
            usuarios.update_user()
            self.nuevoValorMed_le.clear()
            self.idActualizarUsu_le.clear()
            QMessageBox.about(self, 'Aviso', 'Modificado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al modificar!')
        self.show_page_usuario()

    def delete_user(self):
        try:
            usuarios = sql_structures.SqlDataBase_usuarios('', '', '',
                                                           '', '', self.id_c)
            usuarios.delete_user()
            QMessageBox.about(self, 'Aviso', 'Eliminado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al eliminar!')
        self.carga_tabla_Usuario()

    def click_tabla_usuario(self, row, column):
        manager = sql_structures.Manager()
        item = self.tablaUsuario.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'Usuario', 'Contraseña', 'Rol', 'permisos_id']
        header_item = self.tablaUsuario.horizontalHeaderItem(column)
        column_name = header_item.text()

        if column_name == 'Usuario':
            self.id_c = manager.get('usuario', columns_ingreso, value, 'Usuario')
        elif column_name == 'Contraseña':
            self.id_c = manager.get('usuario', columns_ingreso, value, 'Contraseña')
        elif column_name == 'Rol':
            self.id_c = manager.get('usuario', columns_ingreso, value, 'Rol')

    def carga_tabla_Usuario(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('usuario')
            self.tablaUsuario.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tablaUsuario.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tablaUsuario.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tablaUsuario.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
        except Exception as e:
            print(e)

    def iniciar_sesion(self):
        encrip = Metodo()
        refue = Metodos_refuerzo()
        key = "abcdefghijkl12345678!@#$"
        # key = 'protodrjympg15599357!@#$'
        key1 = "~Marp~__842631597"
        a = ""
        offset = 8
        encrypted = ""
        try:
            self.usuario_comprobacion = self.info_usua.text()
            usuario = sql_structures.Manager()
            rol = usuario.iniciar_ses(self.usuario_comprobacion)
            contrasena_comprobacion = self.info_contra.text()
            contrasena = usuario.iniciar_contra(self.usuario_comprobacion)
            c = encrip.decrypt(offset, contrasena, key)
            print(self.usuario_comprobacion)
            print(contrasena)
            print(c)
            print(rol)
            if contrasena_comprobacion == c:
                t = True
                if rol == 0:
                    self.frame_modulos.show()
                elif rol == 1:
                    self.frame_modulos.show()
                    self.btn_modulo_farmacia.hide()
                    self.btn_modulo_usuario.hide()
                elif rol == 2:
                    self.frame_modulos.show()
                    self.btn_modulo_doctor.hide()
                    self.btn_modulo_paciente.hide()
                    self.btn_modulo_receta.hide()
                    self.btn_modulo_usuario.hide()
                elif rol == 3:
                    self.frame_modulos.show()
                    self.btn_modulo_doctor.hide()
                    self.btn_modulo_farmacia.hide()
                    self.btn_modulo_receta.hide()
                    self.btn_modulo_usuario.hide()
                else:
                    QMessageBox.about(self, 'Aviso', 'Usuario incorrecto!')
            else:
                QMessageBox.about(self, 'Aviso', 'Contraseña incorrecta!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Contraseña incorrecta!')

    def abrir_manual(self):
        path = 'C:/Users/andre/Documents/analisis y diseño/proyecto/manual de usuario.pdf'
        webbrowser.open_new(path)
