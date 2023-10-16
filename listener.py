import os
import time
import pydicom
import re
import shutil
from datetime import datetime
class folderWatcher:

    def __init__(self, file_path,umbral,carpeta_destino):
        self.file_path = file_path
        self.umbral=umbral
        self.carpeta_destino = carpeta_destino
        self.is_running = True
    def listar_atributos_dicom(self,ruta_completa):
        try:
            # Leer el archivo DICOM
            dicom_file = pydicom.dcmread(ruta_completa)

            # Obtener una lista de atributos disponibles
            atributos_disponibles = dir(dicom_file)

            return atributos_disponibles

        except Exception as e:
            return str(e)
    def watch(self,tipoRuta):
        while self.is_running:
            tiempo_actual = time.time()
            tiempo_hace_24_horas = tiempo_actual - (24 * 60 * 60)  # 24 horas en segundos
            archivos = os.listdir(self.file_path)
            ncarpeta="1x";

            for archivo in archivos:

                ruta_completa = os.path.join(self.file_path, archivo)

                # Comprobar si es un archivo (no un directorio)
                if os.path.isfile(ruta_completa):
                    # Obtener la marca de tiempo de la última modificación del archivo
                    tiempo_modificacion = os.path.getctime(ruta_completa)
                    # Comprobar si el archivo ha sido modificado recientemente
                    if tiempo_modificacion > tiempo_hace_24_horas:
                        dicom_file = pydicom.dcmread(ruta_completa)
                        cadena=str(dicom_file.PatientName)
                        if "l_" in cadena:
                            continue
                        tiipo = dicom_file.get("Modality", "Atributo no encontrado")
                        idEstudio = dicom_file.get("StudyID", "Atributo no encontrado")
                        paciente = re.sub(r'[^a-zA-Z0-9]', '_', tiipo+'_'+cadena+''+idEstudio)
                        if not os.path.exists(self.carpeta_destino+tipoRuta+paciente):
                            os.makedirs(self.carpeta_destino+tipoRuta+paciente)

                        serie = dicom_file.get("SeriesDescription", "no_name")
                        serieLimpia = re.sub(r'[^a-zA-Z0-9]', '_', serie)
                        numeroSerie = dicom_file.get("SeriesNumber", "0")

                        carpeta=serieLimpia+str(numeroSerie)
                        if (ncarpeta != carpeta):
                            numeroDCm = 1;
                            ncarpeta = carpeta
                        else:
                            numeroDCm += 1;
                        if not os.path.exists(self.carpeta_destino+tipoRuta+paciente+tipoRuta+carpeta):
                            os.makedirs(self.carpeta_destino+tipoRuta+paciente+tipoRuta+carpeta)
                        nuevo_nombre = 'dcm'+str(numeroDCm)+'.dcm'
                        ruta_destino_con_nombre = os.path.join(self.carpeta_destino+tipoRuta+paciente+tipoRuta+carpeta, nuevo_nombre)
                        shutil.copy(ruta_completa, ruta_destino_con_nombre)
                        nuevo_nombre_paciente = "l_"+cadena;
                        dicom_file.PatientName = nuevo_nombre_paciente
                        print('1---'+cadena+'-'+nuevo_nombre)
                        dicom_file.save_as(ruta_completa)
                        print('2----'+cadena + '-' + nuevo_nombre)

            # Dormir durante un cierto período antes de volver a verificar
            time.sleep(20)

    def stop(self):
        self.is_running = False  # Método para detener el hilo


# Ejemplo de uso
if __name__ == "__main__":
    file_watcher = folderWatcher("C:\\Users\\moren\\OneDrive\\Documentos\\horos\\database\\0090873",9600,"C:\\wamp64\\www\\hospital\\imagenologia\\servidor_dcm\\estudios_na");
    #file_watcher.watch();