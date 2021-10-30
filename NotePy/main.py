from tkinter import *
from tkinter import filedialog as f
import platform
import sys
import os
# package imports
import src.menu.about as about

TITLE = "NotePy"

# Configuracion de la raiz de nuestro editor
root = Tk()
root.title(TITLE)
if platform.system() == "Windows":
    root.iconbitmap("img/icon.ico")
else:
    root.iconphoto(True, PhotoImage(os.path.join(sys.path[0], "img/icon.xbm")))

url_file = ""

# caja de texto
text = Text(root, undo=True)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("Arial", 14), wrap=NONE)

#monitor Inferior
mensaje = StringVar()
mensaje.set(" Bienvenido a NotPy")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

# scrollbar para text
scroll = Scrollbar(root)
scroll.config(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)


# funciones

def new_file():
    global url_file
    # borra desde el primer caracter hasta el ultimo
    text.delete(1.0, "end")
    url_file = ""
    root.title(url_file + TITLE) 

def open_file():
    global url_file
    mensaje.set(" Abrir archivo")
    url_file = f.askopenfilename(initialdir='.', filetypes=[("Documento de texto", "*.txt"), ("Documento RTF", "*.rtf"), ("Archivo Python", "*.py"), ("Archivo HTML", "*.html"), ("Archivo CSS", "*.css"), ("Archivo Javascript", "*.js"), ("Todos los archivos", "*"),], title="Abrir archivo")
    if url_file != "":
        with open(url_file, 'r') as file:
            file = open(url_file, 'r')
            content = file.read()
            text.delete(1.0, "end")
            text.insert('insert', content)
            root.title(f"{url_file} {TITLE}")

def save_file():
    global url_file
    if url_file == "":
        save_file_as()
    else:
        content = text.get(1.0, "end-1c")
        with open(url_file, "w+") as file:
            file.write(content)
            root.title(f"Archivo guardado en {url_file} {TITLE}")
            mensaje.set(" Archivo guardado correctamente")

def save_file_as(event=None):
    global url_file
    url_file = f.asksaveasfile(initialdir='.', filetypes=[("Documento de texto", "*.txt"), ("Documento RTF", "*.py"), ("Archivo Python", "*.py"), ("Archivo HTML", "*.html"), ("Archivo CSS", "*.css"), ("Archivo Javascript", "*.js"), ("Escriba una extensión", "*"),], title="Guardar archivo como")
    content = text.get(1.0, "end-1c")
    if url_file not in [None, ""]:
        with open(url_file.name, "w+") as file:
            file.write(content)
            root.title(f"Archivo guardado en {url_file.name} {TITLE}")
            mensaje.set(" Archivo guardado correctamente")
    else:
        mensaje.set(" Guardado cancelado")
            
def copiar():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get())


def pegar():

    text.insert(INSERT, text.clipboard_get())


def cortar():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get())

    text.delete("sel.first", "sel.last")


def deshacer(event=None):

    text.edit_undo()


def rehacer(envent=None):

    text.edit_redo()

def fuente(a):
    text.config(font=a)

#eventos de teclado

root.bind('<Control-s>', save_file_as)
root.bind('<Control-z>', deshacer)
root.bind('<Control-y>', rehacer)

# Menú
bar = Menu(root)
file_menu = Menu(bar, tearoff=0)
file_menu.add_command(label="Nuevo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar como", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)
bar.add_cascade(menu=file_menu, label="Archivo")

#menu de edicion
editar = Menu(bar, tearoff=0)
editar.add_command(label="Deshacer ", command=deshacer)
editar.add_command(label="Rehacer ", command=rehacer)
editar.add_separator()
editar.add_command(label="Copiar", command=copiar)
editar.add_command(label="Cortar", command=cortar)
editar.add_command(label="Pegar", command=pegar)
bar.add_cascade(label="Edición", menu=editar)

 #fuente
file_menu = Menu(bar, tearoff=0)
file_menu.add_command(label="Arial", command=lambda:fuente("Arial"))
file_menu.add_command(label="Consolas", command=lambda:fuente("Consolas"))
file_menu.add_command(label="Georgia", command=lambda:fuente("Georgia"))
file_menu.add_command(label="Times", command=lambda:fuente("Times"))
file_menu.add_command(label="Franklin", command=lambda:fuente("Franklin"))
file_menu.add_command(label="Segoe", command=lambda:fuente("Segoe"))
file_menu.add_command(label="Lucida", command=lambda:fuente("Lucida"))
file_menu.add_command(label="Cambria", command=lambda:fuente("Cambria"))
file_menu.add_command(label="Impact", command=lambda:fuente("Impact"))
file_menu.add_command(label="Courier", command=lambda:fuente("Courier"))
file_menu.add_command(label="Verdana", command=lambda:fuente("Verdana"))
file_menu.add_command(label="Jerbreins mono", command=lambda:fuente("jerbreins"))
bar.add_cascade(menu=file_menu, label="Fuente")

# menu de ayuda
more_menu = Menu(bar, tearoff=0)
more_menu.add_command(label="Acerca de NotePy", command=about.display_credits)
more_menu.add_command(label="Licencia", command=about.display_license)
more_menu.add_command(label="Contacto", command=about.display_contact)
bar.add_cascade(menu=more_menu, label="Ayuda")


root.config(menu=bar)
root.mainloop()
