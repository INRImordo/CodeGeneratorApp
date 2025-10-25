

# main.py
from m.model import CodeGeneratorModel
from m.v.c.view import CodeGeneratorView
from m.v.c.controller import CodeController

if __name__ == "__main__":
    model = CodeGeneratorModel()
    view = CodeGeneratorView()
    controller = CodeController(model, view)
    view.mainloop()
