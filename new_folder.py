import os

class NewFolder:
    def __init__(self, directorio):
        self.directorio = directorio

    def obtener_carpeta_mas_reciente(self):
        carpetas = [nombre for nombre in os.listdir(self.directorio) if os.path.isdir(os.path.join(self.directorio, nombre))]
        info_carpetas = [(nombre, os.path.getctime(os.path.join(self.directorio, nombre))) for nombre in carpetas]
        info_carpetas.sort(key=lambda x: x[1], reverse=True)

        if info_carpetas:
            carpeta_mas_reciente = info_carpetas[0][0]
            return carpeta_mas_reciente
        else:
            return None

# Uso de la clase
if __name__ == "__main__":
    directorio = 'C:\\Users\\moren\\OneDrive\\Documentos\\horos\\database'  # Reemplaza con la ruta de tu directorio
    gestor_carpeta = NewFolder(directorio)
    carpeta_mas_reciente = gestor_carpeta.obtener_carpeta_mas_reciente()

    if carpeta_mas_reciente:
        print(f"La carpeta más reciente en '{directorio}' es '{carpeta_mas_reciente}'.")
    else:
        print(f"No se encontraron carpetas en '{directorio}'.")