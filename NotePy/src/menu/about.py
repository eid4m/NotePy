from tkinter import messagebox

def display_license():
    with open("LICENSE", "r") as file:
        m = file.read()
    messagebox.showinfo("Licencia", m)

def display_credits():
    LINK = "https://github.com/eid4m/NotePy"
    m = f"""
Versión: 1.2.1 (Pre-release)

Esta aplicación es un editor de texto/código hecha en Python, desarrollado por Adam:

{LINK}

Puedes leer la lista de contribuidores de esta aplicación en el archivo colaborators.txt
    """
    messagebox.showinfo("Acerca de NotePy", m)

def display_contact():
    m = """
Si desea hacer una consulta o sugerencia sobre este programa, puedes hacerlo en nuestro repositorio de GitHub.

Tambien puedes contactarme a este correo: adamnolasco21@gmail.com


"""
    messagebox.showinfo("Acerca de NotePy", m)
