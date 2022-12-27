# Creacion de una app de escritorio con python
# Creacion de la interfaz ancho y alto
# Agregar un logo
# Instrucciones de carga de un archivo
# Aplicacion de diseño
# Adecuar el espacio para visualizar el mejor el diseño
# Invocar una funcion
# Desarrollar el codigo para procesar un archivo PDF y extraer el texto
# Importare las librerias necesarias
import tkinter as tk, PyPDF2
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


root = tk.Tk()
#diseño
canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=3)
#imagen header
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.grid(column=1, row=0)
#texto intrucciones
instrucciones = tk.Label(root, text="Selecciona un PDF para extraer Texto")
instrucciones.grid(column=0, row=1, columnspan=3)

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, bg="#8B23F9", fg="white", height=2, width=15, command=lambda:open_file())
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

def open_file():
    #print("Buscando archivo")
    browse_text.set("Leyendo archivo...")
    file = askopenfile(parent=root, mode="rb", title="Elige un archivo", filetypes=[("PDF File", "*.pdf")])
    if file:
        print("El archivo fue correctamente cargado")
        # vamos a leer el archivo PDF para extraer el texto de la pagina 1
        leer_pdf = PyPDF2.PdfReader(file)
        page = leer_pdf.pages[0]
        page_content = page.extract_text()
        
        print(f"page_content = {page_content}")
    
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        browse_text.set("Browse")

root.mainloop()

