#Objetivo, completar frases y guardar en un archivo txt con la fecha. Poder despues ver las respuestas pasadas.
#visualizar e interactuar con agparse
#crear un loggin
import argparse
import tkinter as tk
from datetime import date
from tkinter import messagebox
respuestas_para_guardar = dict()

frases_guardadas= list()

frases = [
    "Vivir de manera consciente significa para mí, ",
    "Si aporto un 5% más de consciencia a mis actividades de hoy, ",
    "Si presto más atención hoy a mi manera de relacionarme con las personas, "
    ]

parser = argparse.ArgumentParser(description="Rellenar frases Autoestima")

parser.add_argument("-1", "--frase_1", type=str, required=True)
parser.add_argument("-2", "--frase_2", type=str, required=True)
parser.add_argument("-3", "--frase_3", type=str, required=True)

args = parser.parse_args()
respuestas = [args.frase_1, args.frase_2, args.frase_3]

for frase in frases:
    x=0
    respuestas_para_guardar[frase] = respuestas[x]
    x= x+1

print(respuestas_para_guardar)

with open("autoestima.txt", "a", encoding="utf-8") as file:
                file.write(f"{date.today()}\n")
                for frase, respuesta in respuestas_para_guardar:
                    file.write(f"{frase}{respuesta}.\n\n")
                file.write("\n\n")