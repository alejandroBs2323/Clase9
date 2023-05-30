import sys
import math
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QWidget, QGridLayout, \
    QScrollArea, QButtonGroup, QPushButton
from PyQt5 import QtGui
from cliente import Cliente
from ventana3 import Ventana3
from ventana4 import Ventana4


class Ventana2(QMainWindow):

    # Hacer el método de construciión de la ventana:
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

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
        self.imagenFondo = QPixmap('imagenes/mancha-jpg')

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central:
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en Layout vertical:
        self.vertical = QVBoxLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont('Andale Mono', 20))

        # Le ponemos el color de texto:
        self.letrero1.setStyleSheet("color: #800080;")

        # Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)

        # Ponemos un espacio después:
        self.vertical.addStretch()

        # Creamos un scrol:
        self.scrollArea = QScrollArea()

        # Le ponemos transparente el fondo del scroll:
        self.scrollArea.setStyleSheet("background-color: transparent;")

        # Hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para cada celda:
        self.contenedora = QWidget()

        # Vamos a crear un layout de grid para poner una cuadrícula de elementos:
        self.cuadricula = QGridLayout(self.contenedora)

        # Metemos la ventana contenedora ene l scroll:
        self.scrollArea.setWidget(self.contenedora)

        # Metemos el layout vertical en el scroll:
        self.vertical.addWidget(self.scrollArea)

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
        # Consultamos el tamaño de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la lista usuarios:
        self.contador = 0

        # Definimos la cantidad de elementos a mostrar por fila con columna:
        self.elementosPorColumna = 3

        # Calculamos el número de filas
        # Redondeamos al entero superior + 1, dividimos por elementosPorColumna:
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # Controlamos todos los botone por una variable:
        self.botones = QButtonGroup()

        # Definimos que el controlador de los botones debe agrupar a todos los botones inetrnos:
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):

                # Validamos que se están ingresando la cantidad de usuarios correcta:
                if self.contador < self.numeroFilas:
                    # En cada celda de la cuadrícula va una ventana:
                    self.ventanaAuxiliar = QWidget()

                    # Se determina su ancho y su alto:
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # Creamos un layout vertical para cada elemento de la cuadrícula:
                    self.verticalCuadrícula = QVBoxLayout()

                    # Creamos un boton para cada usuario mostrando su cédula:
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    # Establecemos el ancho del boton:
                    self.botonAccion.setFixedWidth(150)

                    # Le ponemos los estilos:
                    self.botonAccion.setStyleSheet("background-color: #BF3EFF;"
                                                   "color: #FFFFFF;"
                                                   "padding: 10px;"
                                                   )
                    # Metemos el boton en el layout vertical para que se vea:
                    self.verticalCuadrícula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo con su cédula como id:
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    # Agregamos un espacio en blanco:
                    self.verticalCuadrícula.addStretch()

                    # A la ventana le asignamos el layout vertical:
                    self.ventanaAuxiliar.setLayout(self.verticalCuadrícula)

                    # A la cuadrícula le agregamos la ventana en la fila y columna actual:
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador:
                    self.contador += 1

        # Establecemos para que funcionen todos los botones:
        self.botones.idClicked.connect(self.metodo_accionBotones)

        # -------BOTN FORMA TABULAR--------------------

        # Hacemos el boton para navegar a la ventana de la tabla de usuarios:
        self.botonFormaTabular = QPushButton("Forma Tabular")

        # Establecemos el ancho del botón
        self.botonFormaTabular.setFixedWidth(100)

        # Establecemos los estilos:
        self.botonFormaTabular.setStyleSheet("background-color: #BF3EFF;"
                                             "color: #FFFFFF;"
                                             "padding: 10px;"
                                             "margin-top: 10px;")

        # Hacemos que el boton Forma Tabular tenga su método:
        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        # Metemos en el layout vertical el boton forma Tabular:
        self.vertical.addWidget(self.botonFormaTabular)

        # ---------  BOTON VOLVER -------------------------

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

    # Método para controlar las acciones de los botones:
    def metodo_accionBotones(self, cedulaUsuario):
        #print(cedulaUsuario)
        self.hide()
        self.ventana4 = Ventana4(self, cedulaUsuario)
        self.ventana4.show()

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())