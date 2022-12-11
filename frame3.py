
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
from sqlite3 import Error
import tkinter as tk
import tkinter.messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_usuario(conn, usuario):

    sql = ''' INSERT INTO usuario(dni,apellidos,nombres,fecha_nac,tipo_usuario,email,contrasenia)
              VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    return cur.lastrowid

window = Tk()

window.geometry("360x730")
window.configure(bg = "#FFFFFF")
dni=tk.IntVar()
apellidos = tk.StringVar()
nombres = tk.StringVar()
fecha_nac = tk.StringVar()
tipo_usuario = tk.StringVar()
email = tk.StringVar()
contrasenia = tk.StringVar()

def crear_usuario():
    database = "Cinemark.db"
    conn = create_connection(database)
    usuario = [dni.get(), apellidos.get(), nombres.get(),fecha_nac.get(),tipo_usuario.get(), email.get(),contrasenia.get()]
    
    create_usuario(conn, usuario)
    tkinter.messagebox.showinfo("Info", "Usuario Creado Correctamente")
    limpiar_datos()
    
def limpiar_datos():
    entry_dni.delete(0,"end")
    entry_apellidos.delete(0,"end")
    entry_nombres.delete(0,"end")
    entry_fecha_nac.delete(0,"end")
    entry_tipo_usuario.delete(0,"end")    
    entry_email.delete(0,"end")
    entry_contrasenia.delete(0,"end")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 730,
    width = 360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    64.0,
    100.375,
    anchor="nw",
    text="Para poder registrarte \ncompleta tus datos:",
    fill="#147984",
    font=("RobotoRoman SemiBold", 24 * -1)
)

canvas.create_text(
    30.0,
    170.3333282470703,
    anchor="nw",
    text="Dni:",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    180.0,
    214.4375,
    image=entry_image_1
)
entry_dni = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_dni.place(
    x=20.0,
    y=200.75,
    width=320.0,
    height=25.375
)

canvas.create_text(
    30.0,
    236.52000427246094,
    anchor="nw",
    text="Apelido/s:",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    180.0,
    275.57501125335693,
    image=entry_image_2
)
entry_apellidos = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_apellidos.place(
    x=20.0,
    y=261.88751220703125,
    width=320.0,
    height=25.374998092651367
)

canvas.create_text(
    30.0,
    300.760009765625,
    anchor="nw",
    text="Nombre/s:",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    180.0,
    341.2749938964844,
    image=entry_image_3
)
entry_nombres = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_nombres.place(
    x=20.0,
    y=327.5874938964844,
    width=320.0,
    height=25.375
)

canvas.create_text(
    22.0,
    362.0799865722656,
    anchor="nw",
    text="Fecha de nacimiento (dd-mm-aaa):",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    180.0,
    402.41253662109375,
    image=entry_image_4
)
entry_fecha_nac = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_fecha_nac.place(
    x=20.0,
    y=388.72503662109375,
    width=320.0,
    height=25.375
)

canvas.create_text(
    22.0,
    423.0,
    anchor="nw",
    text="¿Sos Cliente o Administrador?:",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    180.0,
    466.2875061035156,
    image=entry_image_5
)
entry_tipo_usuario = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_tipo_usuario.place(
    x=20.0,
    y=452.6000061035156,
    width=320.0,
    height=25.375
)

canvas.create_text(
    30.0,
    493.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    182.0,
    532.6875,
    image=entry_image_6
)
entry_email = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_email.place(
    x=22.0,
    y=519.0,
    width=320.0,
    height=25.375
)

canvas.create_text(
    13.0,
    555.0,
    anchor="nw",
    text="Contraseña (8 caracteres entre num.\ny letras, al menos 1 mayúscula):",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    180.0,
    613.6875,
    image=entry_image_7
)
entry_contrasenia = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_contrasenia.place(
    x=20.0,
    y=600.0,
    width=320.0,
    height=25.375
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: crear_usuario(),
    relief="flat"
)
button_1.place(
    x=55.0,
    y=650.0,
    width=250.0,
    height=40.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    180.0,
    66.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
