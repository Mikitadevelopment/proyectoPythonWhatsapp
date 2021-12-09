from datetime import timedelta, datetime
import datetime
import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class contacto:

    def __init__(self, telefono, Nombre, email):
        self.telefono = telefono
        self.email = email
        self.nombre = Nombre

    def __str__(self):
        return f'{self.telefono};{self.nombre};{self.email}'

class GestionContactos:
    def __init__(self):
        self.nombre_archivo = 'grafica/contactos.txt'

        self.verificar_archivo()

    def verificar_archivo(self):
        if os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, 'wt', encoding='utf-8') as f:
                pass

    def agregar_contacto(self, contacto):
        try:
            with open(self.nombre_archivo, 'at', encoding='utf-8') as f:
                f.write(contacto)
                f.write('\n')

            return True
        except:
            return False

    def existe_contactos(self, telefono):
        for c in self.obtener_contactos:
            if c.telefono == telefono:
                return True

        return False

    def obtener_contactos(self):
        try:
            contactos = []
            with open(self.nombre_archivo, 'rt', encoding='utf-8') as f:
                for l in f.readlines():
                    partes = l.split(';')
                    contacto = contacto(*partes)
                    contactos.append(contacto)

            return contactos
        except:
            return None

    def buscar_contacto_por_telefono(self,telefono):
        for c in self.obtener_contactos():
            if c.telefono == telefono:
                return c

        return None

    def eliminar_contacto_por_telefono(self, telefono):
        contactos = self.obtener_contactos

        for c in contactos:
            if c.telefono == telefono:
                contactos.remove(c)
                reemplazar_archivo(contactos)
                return True

        return False

    def reemplazar_archivo(self, contactos):
        try:
            with open(self.nombre_archivo, 'wt', encoding='utf-8') as f:
                for c in contactos:
                    f.write(c)
                    f.write('\n')
            return True
        except:
            return False

    def modificar_contacto(self, telefono, contacto):
        contactos = self.obtener_contactos()

        indice = 0

        for c in contactos:
            if c.telefono == telefono:
                c.nombre = contacto.nombre
                c.email = contacto.email
                self.reemplazar_archivo(contactos)

                return True

        return False

class contactosApp:

    def __init__(self, master):
        self.master = master
        self.gestion_contactos = GestionContactos()

        patron = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.patron_telefono = re.compile(patron)

        self.inicializar_gui()

    def inicializar_gui(self):
        lbl_titulo = tk.Label(self.master, text='contactos App', font=('Helvetica', 16))
        lbl_titulo.place(x=10, y=10)

        self.lbx_contactos = tk.Listbox(self.master, width=30, height=20)
        self.lbx_contactos.place(x=10, y=40)
        self.lbx_contactos.bind('<<ListboxSelect>>', self.seleccionar_contacto)

        lbl_nombre = tk.Label(self.master, text='Nombre:', font=('Helvetica',13))
        lbl_nombre.place(x=230, y=40)
        self.txt_nombre = tk.Entry(self.master, width=48)
        self.txt_nombre.place(x=230, y=70)

        lbl_telefono = tk.Label(self.master, text='Telefono:', font=('Helvetica',13))
        lbl_telefono.place(x=230, y=90)
        self.txt_telefono = tk.Entry(self.master, width=48)
        self.txt_telefono.place(x=230, y=120)

        lbl_email = tk.Label(self.master, text='Email:', font=('Helvetica',13))
        lbl_email.place(x=230, y=140)
        self.txt_email = tk.Entry(self.master, width=48)
        self.txt_email.place(x=230, y=170)

        btn_nuevo = tk.Button(self.master, text='Nuevo', width=18)
        btn_nuevo.place(x=230, y=255)
        btn_nuevo['command'] = self.nuevo

        btn_guardar = tk.Button(self.master, text='Guardar', width=18)
        btn_guardar.place(x=385, y=255)
        btn_guardar['command'] = self.guardar

        btn_actualizar = tk.Button(self.master, text='Actualizar', width=18)
        btn_actualizar.place(x=230, y=287)
        btn_actualizar['command'] = self.actualizar

        btn_eliminar = tk.Button(self.master, text='Eliminar', width=18)
        btn_eliminar.place(x=385, y=287)
        btn_eliminar['command'] = self.eliminar

        self.lbl_foto = tk.Label(self.master)
        self.lbl_foto.place(x=550, y=70, width=200, height=200)

    def nuevo(self):
        self.txt_telefono.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)

    def guardar(self):
        telefono = self.txt_telefono.get().strip()
        nombre = self.txt_nombre.get().strip()
        email = self.txt_email.get().strip()

        if not self.patron_telefono.search(telefono):
            messagebox.showwarning('Mensaje', 'Debe escribir un telefono válido')
            return

        if len(nombre) == 0:
            messagebox.showwarning('Mensaje', 'El campo Nombre es obligatorio.')
            return

        if not self.patron_telefono.search(email):
            messagebox.showwarning('Mensaje', 'Debe escribir un Email válido')
            return

        if self.gestion_contactos.existe_contactos(telefono):
            messagebox.showwarning('Mensaje', 'Ya existe un contacto con el numero de telefono especificado')
            return

        contacto = contacto(telefono, nombre, email)
        messagebox.showinfo('Mensaje', 'El contacto se creó de forma correcta.')

        self.nuevo()

    def actualizar(self):
        pass

    def eliminar(self):
        pass

    def seleccionar_contacto(self, evento):
        pass

def main():
    app = tk.Tk()
    app.title('Contactos App')
    app.geometry('700x420')

    ventana = contactosApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
