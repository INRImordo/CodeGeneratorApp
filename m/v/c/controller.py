from tkinter import messagebox, filedialog

class CodeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Lier les actions
        self.view.generate_button.configure(command=self.generate_code)
        self.view.save_button.configure(command=self.save_code)

    def generate_code(self):
        data = self.view.get_input_text()
        if not data:
            messagebox.showerror("Erreur", "Veuillez entrer un texte ou lien.")
            return

        code_type = self.view.get_code_type()
        fill, back = self.view.get_colors()
        logo_path = self.view.get_logo_path()  # 🔹 récupération du logo

        try:
            if code_type == "QR Code":
                img = self.model.generate_qr(data, fill, back, logo_path)
            else:
                img = self.model.generate_barcode(data)
            self.view.display_image(img)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de générer le code : {e}")

    def save_code(self):
        if not self.view.generated_image:
            messagebox.showwarning("Avertissement", "Aucune image à enregistrer.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png"), ("Tous les fichiers", "*.*")]
        )
        if file_path:
            self.view.generated_image.save(file_path)
            messagebox.showinfo("Succès", "Image enregistrée avec succès !")
