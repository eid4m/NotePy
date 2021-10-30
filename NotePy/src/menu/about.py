# En este archivo se almacenan todas las funciones de la barra de menu 
# en la cascada "Sobre"
from tkinter import messagebox

def display_license():
    with open("LICENSE", "r") as file:
        m = file.read()
    messagebox.showinfo("Licencia", m)

def display_credits():
    LINK = "https://github.com/eid4m"
    m = f"""
Versión: 1.0.2

Esta aplicación ha sido desarrollada por Adam en su repositorio de GitHub:

{LINK}

Puedes leer la lista completa de contribuidores de esta aplicación en el archivo contributors.md
    """
    messagebox.showinfo("Acerca de NotePy", m)

def display_contact():
    m = """
Si desea hacer una consulta o sugerencia sobre este programa, puedes hacerlo en nuestro repositorio de GitHub.

Tambien puedes contactarme a este correo: adamnolasco21@gmail.com


"""
    messagebox.showinfo("Acerca de NotePy", m)
