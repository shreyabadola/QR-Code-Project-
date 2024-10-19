import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    border=2,
                    box_size=10)
qr.add_data("https://www.linkedin.com/in/shreya-badola-552851291")
qr.make(fit=True)
img = qr.make_image(fill_color="dodgerblue", back_color="white")
img.save("Linkedin_Account.png")
