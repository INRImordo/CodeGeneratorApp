# view.py
import sys
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import colorchooser
from PIL import Image, ImageTk
import os
import tkinter as tk
from customtkinter import CTkImage


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if getattr(sys, 'frozen', False):
    os.environ['TK_LIBRARY'] = os.path.join(sys._MEIPASS, 'tcl8.6')
    os.environ['TCL_LIBRARY'] = os.path.join(sys._MEIPASS, 'tcl8.6')


class CodeGeneratorView(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        
        
        # ---- Chemins des icônes ----
        if getattr(sys, 'frozen', False):
            BASE_DIR = sys._MEIPASS
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        
        self.ICON_ICO_PATH = resource_path("m/v/icons/im.ico")
        self.ICON_PNG_PATH = resource_path("m/v/icons/im.PNG")
        self.ICON_GEM = resource_path("m/v/icons/gem.ico")
        self.ICON_SAVE = resource_path("m/v/icons/cloud-arrow-down-fill.ico")

        # ---- Charger et redimensionner les icônes ----
        self.icon_gem = CTkImage(Image.open(self.ICON_GEM).resize((20, 20)))
        self.icon_save = CTkImage(Image.open(self.ICON_SAVE).resize((20, 20)))
                
        if os.name == "nt":
            self.iconbitmap(self.ICON_ICO_PATH)
        else:
            self.iconphoto(True, ImageTk.PhotoImage(file=self.ICON_PNG_PATH))



            
        self.title("Générateur QR Code & Code-barres")
        self.geometry("600x690")
        self.resizable(False, False)
        
                

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.generated_image = None
        self.fill_color = "black"
        self.back_color = "white"
        

        # ---- Widgets ----
        self.label_title = ctk.CTkLabel(self, text="Générateur de QR Code & Code-barres", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)

        self.entry_text = ctk.CTkEntry(
            self,
            placeholder_text="Entrez un texte ou un lien...",
            width=500,  
            height=40,
            font=("Arial", 18)
        )        
        self.entry_text.pack(pady=10)
        
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("light")
        

        # Type de code
        self.code_type = ctk.StringVar(value="QR Code")
        self.radio_qr = ctk.CTkRadioButton(self, text="QR Code", variable=self.code_type, value="QR Code")
        self.radio_bar = ctk.CTkRadioButton(self, text="Code-barres", variable=self.code_type, value="Code-barres")
        self.radio_qr.pack(pady=5)
        self.radio_bar.pack(pady=5)

        # Zone d’affichage
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(pady=20)

        
        
        # Frame pour contenir les boutons côte à côte
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=15)
        
        # Bouton  0 : Choisir Couleur
        self.color_btn_fill = ctk.CTkButton(self.buttons_frame, text="Choisir Couleur", width=200, command=self.choose_fill_color)
        self.color_btn_fill.grid(row=0, column=1, pady=10)

        # Bouton 1 : Générer
        self.generate_button = ctk.CTkButton(self.buttons_frame, image=self.icon_gem, compound="left", text="Générer le code", width=200, fg_color="#007BFF",hover_color="#0056b3", text_color="white",border_color="#003f7f", border_width=2 )
        self.generate_button.grid(row=0, column=0, padx=10)

        # Bouton 2 : Enregistrer
        self.save_button = ctk.CTkButton(self.buttons_frame, image=self.icon_save, compound="left", text="Enregistrer l'image", width=200, fg_color="#146409",hover_color="#1E8810", text_color="white",border_color="#317E27", border_width=2 )
        self.save_button.grid(row=1, column=1, padx=10)
        
        
 
        

    # ---- Méthodes utilitaires ----
    def get_input_text(self):
        return self.entry_text.get().strip()

    def get_code_type(self):
        return self.code_type.get()

    def choose_fill_color(self):
        color = colorchooser.askcolor(title="Choisir la couleur du code")[1]
        if color:
            self.fill_color = color

    def choose_back_color(self):
        color = colorchooser.askcolor(title="Choisir la couleur de fond")[1]
        if color:
            self.back_color = color

    def get_colors(self):
        return self.fill_color, self.back_color

    def display_image(self, img):
        self.generated_image = img
        img_tk = ImageTk.PhotoImage(img.resize((250, 250)))
        self.image_label.configure(image=img_tk, text="")
        self.image_label.image = img_tk
