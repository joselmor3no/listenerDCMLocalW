# This is a sample Python script.
from new_folder import NewFolder
from listener import folderWatcher

from hilos import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ruta_origen = 'C:\\Users\\moren\\OneDrive\\Documentos\\horos\\database';
    ruta_destino = "C:\\wamp64\\www\\hospital\\imagenologia\\servidor_dcm\\estudios_na";
    ventana_t = VerVentana(ruta_origen, ruta_destino)
    ventana_t.start()
    tipoRuta="\\";
    leerDCM=LeerDCM(ruta_origen, ruta_destino,tipoRuta)
    dcm_t = leerDCM
    dcm_t.start()

    # Espera a que los hilos finalicen
    ventana_t.join()

