import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QHBoxLayout, QDialog, QDialogButtonBox
from PyQt5 import QtGui, QtCore

from cliente import Cliente


class Ventana4(QMainWindow):
    # Hacer el método de construcción de la ventana:
    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior

        self.cedulaUsuario = cedula

        # poner el título:
        self.setWindowTitle("Editar Usuario")

        # Poner el ícono:
        self.setWindowIcon(QtGui.QIcon('imagenes/cflor13.png'))

        # Estableciendo las propiedades de ancho y alto:
        self.ancho = 900
        self.alto = 600

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal:
        self.fondo = QLabel(self)

        # Definimos el color de forno:
        self.fondo.setStyleSheet('background-color: #FFBBFF;')

        # Establecemos la ventana de fondo como la ventana central:
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en Layout vertical:
        self.horizontal = QHBoxLayout()

        # Le ponemos las márgenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------LAYOUT IZQUIERDO-------------------

        # Creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Editar cliente")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto y márgenes:
        self.letrero1.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #800080;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del Label:
        self.letrero2.setFixedWidth(310)

        # Le escribimos el texto:
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos el color de texto y márgenes:
        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Hacemos el campo para ingresar el usuario
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el password:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos el Correo en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # -----------BOTON EDITAR-------------

        # Hacemos el botón para registrar los datos:
        self.botonEdita = QPushButton("Editar")

        # Establecemos el ancho del botón:
        self.botonEdita.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonEdita.setStyleSheet("background-color: #BF3EFF;"
                                      "color: #FFFFFF;"
                                      "padding: 10px;"
                                      "margin-top: 40px;")

        self.botonEdita.clicked.connect(self.accion_botonEdita)

        # ------------BOTON LIMPIAR---------------

        # Hacemos el botón para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón:
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #BF3EFF;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonEdita, self.botonLimpiar)

        # -----------BOTON ELIMINAR -----------------

        # Hacemos el botón para eliminar los datos:
        self.botonEliminar = QPushButton("Eliminar")

        # Establecemos el ancho del botón:
        self.botonEliminar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonEliminar.setStyleSheet("background-color: #BF3EFF;"
                                         "color: #FFFFFF;"
                                         "padding: 10px;"
                                         "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonEliminar)

        # Agregamos los dos botones al layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonEliminar)

        # -----------------BOTON VOLVER-----------

        # Hacemos el botón para devolvernos a la ventana anterior:
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del botón
        self.botonVolver.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #BF3EFF;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;")

        # Hacemos que el botón Volver tenga su método:
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Metemos en el layout vertical el botón Volver:
        self.ladoIzquierdo.addRow(self.botonVolver)

        # Agregamos el Layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # ----------LAYOUT DERECHO---------

        # Creamos el layout del lado derecho:
        self.ladoDerecho = QFormLayout()

        # Se asigna la margen solo a la izquierda de 100px:
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrtero 3.
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("EditarRecuperar la contraseña")

        # Le asignamos el tipo de letra:
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Le ponemos el color de texto:
        self.letrero3.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #800080;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        # Le escribimos el texto:
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero4.setFont(QFont("Andale Mono", 11))

        # Le ponemos el color de texto y márgenes:
        self.letrero4.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # ------1

        # Hacemos el letrero de la pregunta1:
        self.labelPregunta1 = QLabel("Pregunta de verificación1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta1:
        self.labelRespuesta1 = QLabel("Respuesta de verificación1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta1:
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)

        # -----2

        # Hacemos el letrero de la pregunta2:
        self.labelPregunta2 = QLabel("Pregunta de verificación2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respuesta2:
        self.labelRespuesta2 = QLabel("Respuesta de verificación2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta2:
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta2)

        # _____3

        # Hacemos el letrero de la pregunta3:
        self.labelPregunta3 = QLabel("Pregunta de verificación3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta3:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta3:
        self.labelRespuesta3 = QLabel("Respuesta de verificación3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)

        # --------

        # Agregamos el layout ladoDerecho layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # ---------- OJO IMPORTANTE PONER AL FINAL ------------

        # Indicamos que el Layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

        # -------CONSTRUCCION DE LA VENTANA EMERGENTE -----------

        # Creamos la ventana de diálogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el botón para aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Configuramos la ventana para que sea Modal.
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilos al label mensaje:
        self.mensaje.setStyleSheet("background-color: #E066FF; color: #000000; padding: 10px;")

        # Agregamos el label de mensaje:
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones:
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana:
        self.ventanaDialogo.setLayout(self.vertical)

        # Llamamos el método para que se carguen los datos del usuario en el formulario:
        self.cargar_datos()

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText("")
        self.usuario.setText("")
        self.password.setText("")
        self.password2.setText("")
        self.documento.setText("")
        self.correo.setText("")
        self.pregunta1.setText("")
        self.respuesta1.setText("")
        self.pregunta2.setText("")
        self.respuesta2.setText("")
        self.pregunta3.setText("")
        self.respuesta3.setText("")

    def accion_botonEdita(self):

        # Variable para controlar que se han ingresado los datos correctos:
        self.datosCorrectos = True

        # Establecemos el título de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de edición")

        # Validamos que los passwords sean iguales:
        if (
                self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            # Escriimos el texto explicativo:
            self.mensaje.setText("Los passwords NO son iguales")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Validamos que se ingresen todos los campos:
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Debe seleccionar un usuario con documento válido!")

            # Hacemos que la ventana de diálogo se vea:
            self.ventanaDialogo.exec()

            self.metodo_botonVolver()

        # Si los datos están correctos:
        if self.datosCorrectos:
            # Abrimos el archivo en modo agregar escribiendo datos en binario:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacía para agregar todos los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por;
                lista = linea.split(";")

                # Se para si ya no hay más registros en el archivo
                if linea == '':
                    break

                # Creamos un objeto de tipo cliente llamado u:
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10]

                )

                # Metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista usuarios con todos los usuarios:

            # Variable para controlar si existe el documento.
            existeDocumento = False

            # Buscamos en la lista usuario por usuario si existe la cédula:
            # es la cédula seleccionada de la ventana anterior
            for u in usuarios:
                # Comparamos el documento ingresado:
                # Si corresponde con el documento, es el usuario correcto:
                if int(u.documento) == self.cedulaUsuario:
                    # Guardamos los datos del formulario en las propiedades del usuario:
                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()
                    # Indicamos que encontramos el documento:
                    existeDocumento = True
                    # Paramos el for:
                    break
            # Si no existe un usuario con este documento:
            if (
                    not existeDocumento
            ):
                # Escribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaUsuario))

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

            # Abrimos el archivo en modo lectura en modo de binario:
            self.file = open('datos/clientes.txt', 'wb')

            # Recorremos la lista de usuarios:
            # Para guardar usuario por usuario en el archivo:
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))

            self.file.close()

            # Si existe un usuario con este documento:
            # Y si se editó correctamente:
            if (
                    existeDocumento
            ):
                # Escribimos el texto explicativo:
                self.mensaje.setText(" usuario actualizado correctamente!")

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.metodo_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break

            self.file.close()

    def accion_botonEliminar(self):
        # Variable para controlar que se han ingresado los datos correctos:
        self.datosCorrectos = True

        # Controlamos si vamos a eliminar:
        self.eliminar = False

        # Validamos que se ingresen todos los campos:
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Debe seleccionar un usuario con documento valido!")

            # Hacemos que la ventana de diálogo se vea:
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Creamos la ventana de diálogo para confirmar si vamos a eliminar el registro:
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            # Definimos el tamaño de la ventana:
            self.ventanaDialogoEliminar.resize(300, 150)

            # Configuramos la ventana para que sea modal:
            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            # Creamos un layout vertical:
            self.verticalEliminar = QVBoxLayout()

            # Creamos un label para los mensajes:
            self.mensajeElimiar = QLabel("¿Estás seguro que desea eliminar este registro de usuario?")

            # Le ponemos estilos al label mensaje:
            self.mensajeElimiar.setStyleSheet("background-color: #E066FF; color: #000000; padding: 10px;")

            # Agregamos el label de mensaje:
            self.verticalEliminar.addWidget(self.mensajeElimiar)

            # Agregamos las opciones de aceptar y cancelar en la ventana de dialogo:
            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # Agregamos las opciones de los botones:
            self.verticalEliminar.addWidget(self.opcionesBox)

            # Establecemos el layout para la ventana:
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            # Hacemos que la ventana de Diálogo se vea:
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            # Abrimos el archivo en modo lectura:
            self.file = open('datos/clientes.txt', 'rb')
            # Lista vacía para agregar todos los usuarios:
            usuarios = []

            # Iteramos sobre el archivo línea por línea:
            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por;
                lista = linea.split(";")

                # Se para si ya no hay más registros en el archivo
                if linea == '':
                    break

                # Creamos un objeto de tipo cliente llamado u:
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10]

                )

                # Metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista usuario con todos los usuarios:

            # Variable para controlar si existe el documento.
            existeDocumento = False

            # Buscamos en la lista usuario por usuario si existe la cédula:
            for u in usuarios:
                # Comparamos el documento ingresado:
                # Si corresponde con el documento, es el usuario correcto:
                if int(u.documento) == self.cedulaUsuario:
                    # Eliminamos el usuario de la lista de usuarios:
                    usuarios.remove(u)
                    existeDocumento = True
                    # Paramos el for:
                    break

            # Abrimos el archivo en modo escritura escribiendo datos en binario
            self.file = open('datos/clientes.txt', 'wb')

            # Recorremos la lista de usuarios
            # Para guardar los usuarios restantes en el archivo:
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))

            self.file.close()


            # Si se encontró un usuario con este documento y se ha eliminado:
            if (
                existeDocumento
            ):
                # Escribimos el texto explicativo:
                self.mensaje.setText("Usuario eliminado exitosamente!")

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.metodo_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):

        # Abrimos el archivo en modo lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacía para agregar todos los usuarios:
        usuarios = []

        # Iteramos sobre el archivo línea por línea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")

            # Se para si ya no hay más registros en el archivo
            if linea == '':
                break

            # Creamos un objeto de tipo cliente llamado u:
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10]

            )

            # Metemos el objeto en la lista de usuarios:
            usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista usuario con todos los usuarios:

        # Variable para controlar si existe el documento.
        existeDocumento = False

        # Buscamos en la lista usuario por usuario si existe la cédula:
        # es la cédula seleccionada de la ventana anterior
        for u in usuarios:
            # Comparamos el documento ingresado:
            # Si corresponde con el documento, es el usuario correcto:
            if int(u.documento) == self.cedulaUsuario:
                # Mostramos los datos en el formulario:
                self.nombreCompleto.setText(u.nombreCompleto)
                # Hacemos que el nombre no se pueda editar:
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                # Hacemos que el documento no se pueda editar:
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)
                # Indicamos que encontramos el documento:
                existeDocumento = True
                # Paramos el for:
                break

        # Si no existe un usuario con este documento:
        if (
                not existeDocumento
        ):
            # Escribimos el texto explicativo:
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.cedulaUsuario))

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana4 = Ventana4()

    ventana4.show()

    sys.exit(app.exec_())