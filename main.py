# main.py
from m.model import CodeGeneratorModel
from m.v.view import CodeGeneratorView
from m.v.c.controller import CodeController
from PIL import ImageTk
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    model = CodeGeneratorModel()
    view = CodeGeneratorView()

    # ---- Charger l'icône après création de la fenêtre ----
    icon_path = resource_path("m/v/icons/im.png")
    icon_img = ImageTk.PhotoImage(file=icon_path)
    view.iconphoto(True, icon_img)

    controller = CodeController(model, view)
    view.mainloop()
