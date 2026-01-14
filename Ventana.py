import tkinter as tk
from datetime import date
from tkinter import messagebox

frases_guardadas= list()
frases = [
    "Vivir de manera consciente significa para mí, ",
    "Si aporto un 5% más de consciencia a mis actividades de hoy, ",
    "Si presto más atención hoy a mi manera de relacionarme con las personas, "
    ]

class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("800x500")
        
        self.title = tk.Label(self.root, text= "Autoestima", font=("Times New Roman", 26))
        self.title.pack(pady=20)
        
        self.button_new_frases = tk.Button(
            self.root, text="Completar", font=("Times New Roman", 16),
            justify="left", command=self.rellenar
        )
        self.button_new_frases.pack(padx=10, pady=20)
        
        self.button_old_frases = tk.Button(
            self.root, text="Registro", font=("Times New Roman", 16),
            command=self.ver_respuetas
        )
        self.button_old_frases.pack(padx=10, pady=20)

        
        self.root.mainloop()
        
    def rellenar(self):
        ventana_new = tk.Toplevel(self.root)
        ventana_new.title("Rellenar frases")
        entradas = []
        
        for frase in frases:
            tk.Label(ventana_new, text=frase, justify="left",
                     font=("Times New Roman",18), wraplength=700).pack(pady=(8,0))
            
            entry = tk.Entry(ventana_new, width=80)
            entry.pack(pady=(0,8))
            
            entradas.append((frase,entry))
#aquí entry no es un str, es un objeto de tkinter, si lo escribo sale= ".!toplevel.!entry"
            
        def guardar():
            respuestas_para_guardar = []
            for frase,entry in entradas:
                text = entry.get().strip()
                respuestas_para_guardar.append((frase, text))
                
            with open("autoestima.txt", "a", encoding="utf-8") as file:
                file.write(f"{date.today()}\n")
                for frase, respuesta in respuestas_para_guardar:
                    file.write(f"{frase}{respuesta}.\n\n")
                file.write("\n\n")
                
            tk.messagebox.showinfo("Guardado", "Tus respusetas se han guardado.")
            ventana_new.destroy()
            
        #porfín el botón para guardar que usa lo que acabamos de definir
        tk.Button(ventana_new, text="Guardar respuestas", command=guardar).pack(pady=10)
        #recuerda que no ponemos "command=guardar()" porque lo estaríaamos llamando automáticamente
        
        
            
    def ver_respuetas(self):
        ventana_new = tk.Toplevel(self.root)
        ventana_new.geometry("800x400")
        ventana_new.title("Respuestas anteriores")
        
        texto = tk.Text(ventana_new, wrap="word", width="700", height="300")
        texto.pack(padx=10, pady=10)
        
        try:
            with open("autoestima.txt", "r", encoding = "utf-8") as file:
                content= file.read()
                texto.insert("1.0", content)
        except FileNotFoundError:
            texto.insert("1.0", "Aún no hay respuestas guardadas.")
            

            
    
    
MyGUI()