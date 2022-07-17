import tkinter as tk 
from tkinter import ttk

class Aplicacion1: #ventana principal del inicio del juego 
    def __init__(self):  #constructor 
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="", labelanchor="n", relief="ridge")   #labelanchor es para la ubicación de la letra  
        self.labelframe1.grid(column=2, row=0, padx=100, pady=13)        
        self.explicacion() #se llama la función del texto de la explicación del juego 
        self.labelframe2=ttk.LabelFrame(self.ventana1, text="", labelanchor="n")        
        self.labelframe2.grid(column=2, row=1, padx=5, pady=10)        
        self.botones() #se llama la función de los botones 
        self.ventana1.resizable(0,0) #impedir que cambien el tamaño de la ventana 
        self.ventana1.geometry("1500x1000") 
        self.ventana1.mainloop()

    #labels que explican el juego y sus diferentes modalidades

    def explicacion(self):
        self.label0=ttk.Label(self.labelframe1, text="¡BIENVENIDOS!\n Las reglas del juego son:", font=("Fixedsys", 15))
        self.label0.grid(column=0, row=0, padx=4, pady=4)

        self.label1=ttk.Label(self.labelframe1, text="1.Empieza el jugador que saque mayor número de dados", font=("Fixedsys", 10))
        self.label1.grid(column=0, row=1, padx=4, pady=4)
       
        self.label2=ttk.Label(self.labelframe1, text="2.Se dan 3 oportunidades para sacar las fichas de la cárcel y se debe sacar pares", font=("Fixedsys", 5))        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
       
        self.label3=ttk.Label(self.labelframe1, text="3.Solo se puede avanzar con casillas especiales '5, 7, 10 o 12'", font=("Fixedsys", 5))        
        self.label3.grid(column=0, row=3, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="4.La casilla SEGURA te hace vulnerable ya que el oponente puede enviarte a la cárcel.", font=("Fixedsys", 5))        
        self.label4.grid(column=0, row=4, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe1, text="5.La casilla de salida de todos los jugadores es segura a menos que un jugador esté en la cárcel,\n al salir puede enviar a la cárcel esas fichas.", font=("Fixedsys", 5))        
        self.label5.grid(column=0, row=5, padx=4, pady=4)

        self.label6=ttk.Label(self.labelframe1, text="6.Si se encuentra en la casilla segura de su color puede ganar si saca únicamente 8 en los dados", font=("Fixedsys", 5))        
        self.label6.grid(column=0, row=6, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe1, text="7.Si un jugador no envía a la cárcel a su oponente pudiendo hacerlo, otro jugador puede soplar la jugada y enviarlo a la cárcel", font=("Fixedsys", 5))        
        self.label7.grid(column=0, row=7, padx=4, pady=4)
        
    # botones que redirigen a la interfaz de cada modo de juego
    def botones(self):
        self.label5=ttk.Label(self.labelframe2, text="¡A JUGAR!", font=("Fixedsys", 15))        
        self.label5.grid(column=1, row=1, padx=4, pady=4)

        '''self.boton2=ttk.Button(self.labelframe2, text="Forma 1", command=self.prueba)
        self.boton2.grid(column=0, row=2, padx=4, pady=4)
        self.boton3=ttk.Button(self.labelframe2, text="Forma 2", command = self.prueba2)
        self.boton3.grid(column=1, row=2, padx=4, pady=4)
        self.boton4=ttk.Button(self.labelframe2, text="Forma 3", command = self.prueba3)
        self.boton4.grid(column=2, row=2, padx=4, pady=4)'''

    #se llama a cada ventana(cada modo de juego)
    '''def prueba(self):
        forma1 = forma1Ventana()

    def prueba2(self):
        forma2 = forma2Ventana()
    
    def prueba3(self):
        forma3 = forma3Ventana()'''

aplicacion1=Aplicacion1()