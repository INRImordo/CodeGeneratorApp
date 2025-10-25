# model.py
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import io

class CodeGeneratorModel:
    def generate_qr(self, data, fill_color="black", back_color="white"):
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        return img

    def generate_barcode(self, data):
        ean = Code128(data, writer=ImageWriter())
        fp = io.BytesIO()
        ean.write(fp)
        fp.seek(0)
        img = Image.open(fp)
        return img
