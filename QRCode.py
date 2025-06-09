import qrcode
from PIL import Image
import tkinter

Data = input("Enter the data you want to enter 🥲 : ")

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (minimum is 4)
)

# Add Data to the QR Code
qr.add_data(Data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image file
#img.save("qrcode.png")

# If you want to display the image, you can use the following
img.show()