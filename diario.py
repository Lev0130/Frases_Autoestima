#Objetivo, completar frases y guardar en un archivo txt con la fecha. Poder despues ver las respuestas pasadas.
#visualizar e interactuar con agparse
#crear un loggin
import argparse
from datetime import date

respuestas_para_guardar = []

frases_guardadas= list()

frases = [
    "Vivir de manera consciente significa para mí, ",
    "Si aporto un 5% más de consciencia a mis actividades de hoy, ",
    "Si presto más atención hoy a mi manera de relacionarme con las personas, "
    ]

parser = argparse.ArgumentParser(description="Rellenar frases Autoestima")


parser.add_argument("-f1", "--frase_1", type=str, required=False)
parser.add_argument("-f2", "--frase_2", type=str, required=False)
parser.add_argument("-f3", "--frase_3", type=str, required=False)
parser.add_argument("--start", action="store_true", required=False)
parser.add_argument("--read", action="store_true", required=False)

args = parser.parse_args()

if args.start:
    print(
    "\n"
    "Estas son las frases que tienes que rellenar:\n\n"
    "-f1 Vivir de manera consciente significa para mí,\n"
    "-f2 Si aporto un 5% más de consciencia a mis actividades de hoy,\n"
    "-f3 Si presto más atención hoy a mi manera de relacionarme con las personas,\n"
)

respuestas = [args.frase_1, args.frase_2, args.frase_3]

if all(respuestas): 

    respuestas_para_guardar = list(zip(frases,respuestas))

    print(respuestas_para_guardar)

    with open("autoestima.txt", "a", encoding="utf-8") as file:
        file.write(f"{date.today()}\n")
        for frase, respuesta in respuestas_para_guardar:
            file.write(f"{frase}{respuesta}.\n\n")
        file.write("\n\n")

if args.read:
    with open("autoestima.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
            print(line)