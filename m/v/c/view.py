# view.py
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import colorchooser



class CodeGeneratorView(ctk.CTk):
    def __init__(self):
        super().__init__()
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
        

        # Type de code
        self.code_type = ctk.StringVar(value="QR Code")
        self.radio_qr = ctk.CTkRadioButton(self, text="QR Code", variable=self.code_type, value="QR Code")
        self.radio_bar = ctk.CTkRadioButton(self, text="Code-barres", variable=self.code_type, value="Code-barres")
        self.radio_qr.pack(pady=5)
        self.radio_bar.pack(pady=5)

        # Sélecteurs de couleur
        self.color_frame = ctk.CTkFrame(self)
        self.color_frame.pack(pady=10)

        ctk.CTkLabel(self.color_frame, text="Couleur avant-plan :").grid(row=0, column=0, padx=10)
        self.color_btn_fill = ctk.CTkButton(self.color_frame, text="Choisir", command=self.choose_fill_color)
        self.color_btn_fill.grid(row=0, column=1, pady=5)
        

        ctk.CTkLabel(self.color_frame, text="Couleur arrière-plan :").grid(row=1, column=0, padx=10)
        self.color_btn_back = ctk.CTkButton(self.color_frame, text="Choisir", command=self.choose_back_color)
        self.color_btn_back.grid(row=1, column=1)
        

        # Bouton de génération
        self.generate_button = ctk.CTkButton(self, text="Générer le code", width=200)
        self.generate_button.pack(pady=15)

        # Zone d’affichage
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(pady=20)

        # Bouton de sauvegarde
        self.save_button = ctk.CTkButton(self, text="Enregistrer l'image", width=200)
        self.save_button.pack(pady=10)

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
