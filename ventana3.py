import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication, QToolBar, QAction, QMessageBox
from PyQt5 import QtGui

from cliente import Cliente


class Ventana3(QMainWindow):

    # Hacer el método de construción de la ventana:
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        # Creamos un atributo que guarde la ventana anterior:
        self.ventanaAnterior = anterior

        # poner el título:
        self.setWindowTitle("Usuarios Registrados")

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

        # Definimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/isto12.jpg')

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central:
        self.setCentralWidget(self.fondo)

        # Abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacía para guardar los usuarios:
        self.usuarios = []

        # Recorremos el archivo, línea por línea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string 11 datos separados por ;
            lista = linea.split(";")
            # Se para sí ya no hay más registros en el archivo:
            if linea == '':
                break
            # Creamos un objeto tipo cliente llamado u:
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
            self.usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista usuario con todos los usuarios:

        # Obtenemos el número de usuarios registrados:
        # Consultamos el tamaño de la lista usuario:
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la lista usuarios:
        self.contador = 0

        # Establecemos la distribución de los elementos en distribución vertical:
        self.vertical = QVBoxLayout()

        # -----CONSTRUIR EL MENÚ TOOLBAR-----

        self.toolbar = QToolBar('manin toolbar')
        self.toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(self.toolbar)

        # -----DELETE------------
        self.delete = QAction(QIcon('imagenes/delete.png'), '&Delete', self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # -----ADD--------------
        self.add = QAction(QIcon('imagenes/add.png'), '&Add', self)
        self.add.triggered.connect(self.accion_add)
        self.toolbar.addAction(self.add)

        # --------INSERT-----------
        self.insert = QAction(QIcon('imagenes/insert.png'), '&Insert', self)
        self.insert.triggered.connect(self.accion_insert)
        self.toolbar.addAction(self.insert)

        # ----FIN MENÚ TOOLBAR-------------

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 11))

        # Le ponemos el color de texto y márgenes:
        self.letrero1.setStyleSheet("color: #BF3EFF;")

        # Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)

        # Le ponemos un espacio después:
        self.vertical.addStretch()

        # Creamos un scroll:
        self.scrollArea = QScrollArea()

        # Hacemos que el scroll se adapte a varios tamaños:
        self.scrollArea.setWidgetResizable(True)

        # Creamos uns tabla:
        self.tabla = QTableWidget()

        # Definimos el número de columnas que tendrá la tabla:
        self.tabla.setColumnCount(11)

        # Definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        # Definimos el letrero de la cabecera:
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta1',
                                              'Pregunta 2',
                                              'Respuesta2',
                                              'Pregunta 3',
                                              'Respuesta3'])

        # Establecemos el número de las filas:
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla:
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # Hacemos que el nombre no se pueda editar:
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # Hacemos que el documento no se pueda editar:
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metemos el layout vertical en el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Ponemos un espacio después:
        self.vertical.addStretch()

        # -------BOTON VOLVER---------------

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

        # Metemos en el layout vertical el boton Volver:
        self.vertical.addWidget(self.botonVolver)

        # ------------ OJO IMPORTANTE PONER AL FINAL ---------------

        # Indicamos que el Layout principal del fondo es vertical:
        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_delete(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self,
                                       'warning',
                                       'para borrar, DEBE seleccionar un registro')

        boton = QMessageBox.question(
            self,
            'confirmation',
            '¿Está segur@ de que quieres borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:
            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):

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

                # Recorremos la lista de usuarios
                for u in usuarios:
                    # Buscamos el usuario por el documento:
                    if (
                            u.documento == self.tabla.item(filaActual, 3).text()
                    ):
                        # Indicamos que encontramos el documento:
                        existeDocumeto = True

                        # Removemos el usuario de la lista de usuarios:
                        usuarios.remove(u)

                        # Pramos el for:
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

                # Hacemos que en la tabla no se vea el registro:
                self.tabla.removeRow(filaActual)

                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente',
                    QMessageBox.StandardButton.Yes
                )
            else:

                # Hacemos que en la tabla no se vea el registro en caso de tratarse de una fila vacía:
                self.tabla.removeRow(filaActual)

    def accion_add(self):
        # Obtenemos el número de filas que tiene la tabla:
        ultimaFila = self.tabla.rowCount()

        # Insertamos uan fila nueva después de la última fila:
        self.tabla.insertRow(ultimaFila)

        # Llenamos cada celda de la nueva fila con un string vacío'':
        self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 10, QTableWidgetItem(''))

    def accion_insert(self):
        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self,
                                       'warning'
                                       'Para ingresar deb seleccionar un registro')

        boton = QMessageBox.question(
            self,
            'confirmation'
            '¿Estás segur@ de que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # Variable para controlar que se hayan ingresado todos los datos:
        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:
            # Validamos que se han ingresado los datos correctos:
            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):
                # Actualizamos la Variable para controlar que se hayan ingresado todos los datos:
                datosVacios = False

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

                # Variable para controlar si ya existe el registro:
                existeRegistro = False

                # Variable para controlar si ya es un registro que ya existe y se va a editar:
                existeDocuemnto = Falsei


                    










if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana3 = Ventana3()

    ventana3.show()

    sys.exit(app.exec_())
