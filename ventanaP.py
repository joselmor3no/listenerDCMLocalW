import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class InterfazEnvioArchivos:
    def __init__(self, root,origen,destino):
        self.root = root
        self.root.title("Envío de Archivos")

        # Cargar una imagen PNG
        image = Image.open("connections.png")
        image = image.resize((300, 300))
        self.empresa_imagen = ImageTk.PhotoImage(image)

        # Mostrar la imagen en un Label
        imagen_label = tk.Label(root, image=self.empresa_imagen)
        imagen_label.grid(row=0, column=0, columnspan=2)

        # Etiqueta y Cuadro de texto 1
        label_texto1 = tk.Label(root, text="Ruta de origen:")
        label_texto1.grid(row=1, column=0, sticky="w")  # Alinear a la izquierda
        cuadro_texto1 = tk.Entry(root,width=40)
        cuadro_texto1.grid(row=1, column=1, padx=10, pady=15)
        cuadro_texto1.insert(0, origen)

        # Etiqueta y Cuadro de texto 2
        label_texto2 = tk.Label(root, text="Ruta de destino:")
        label_texto2.grid(row=2, column=0, sticky="w")  # Alinear a la izquierda
        cuadro_texto2 = tk.Entry(root,width=40)
        cuadro_texto2.grid(row=2, column=1, padx=10, pady=5)
        cuadro_texto2.insert(0, destino)

        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(root, length=300, mode="indeterminate")
        self.barra_progreso.grid(row=3, column=0, columnspan=2)

        # Etiqueta para mostrar el estado de envío
        self.estado_label = tk.Label(root, text="Leyendo y Enviando archivos...")
        self.estado_label.grid(row=4, column=0, columnspan=2)
        self.iniciar_envio()




    def iniciar_envio(self):
        self.estado_label.config(text="Leyendo y Enviando archivos...")
        self.barra_progreso.start(20)

def main():
    root = tk.Tk()
    app = InterfazEnvioArchivos(root,"p1","p2")
    root.mainloop()

if __name__ == "__main__":
    main()
