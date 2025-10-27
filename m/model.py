import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import io

class CodeGeneratorModel:
    def generate_qr(self, data, fill_color="black", back_color="white", logo_path=None):
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

        # 🔹 Si un logo est fourni, on l'ajoute au centre
        if logo_path:
            try:
                logo = Image.open(logo_path)
                logo_size = int(img.size[0] * 0.2)
                logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

                pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
                img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)
            except Exception as e:
                print(f"Erreur lors de l’ajout du logo : {e}")

        return img

    def generate_barcode(self, data):
        ean = Code128(data, writer=ImageWriter())
        fp = io.BytesIO()
        ean.write(fp)
        fp.seek(0)
        img = Image.open(fp)
        return img
