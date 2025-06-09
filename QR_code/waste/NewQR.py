import qrcode

# Data to encode in the QR code
data = "https://example.com"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code, from 1 to 40
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction
    box_size=10,  # size of the box where the QR code will be displayed
    border=4,  # thickness of the border
)

qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code as an image
img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")