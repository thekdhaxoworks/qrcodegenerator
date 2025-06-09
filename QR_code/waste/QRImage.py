import qrcode
from PIL import Image
import base64
from io import BytesIO

# Step 1: Load the image and convert it to base64 string
def image_to_base64(image_path):
    with open(image_path, "tkr.jpeg") as img_file:
        # Encode the image as base64
        return base64.b64encode(img_file.read()).decode('utf-8')

# Step 2: Convert base64 string into QR code
def generate_qr_with_image_data(image_path):
    # Convert image to base64 string
    image_base64 = image_to_base64(image_path)
    
    # Generate QR code with the base64 image string
    qr = qrcode.QRCode(
        version=1,  # QR code size (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size
    )

    qr.add_data(image_base64)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill="black", back_color="white")

    # Show the QR code
    qr_img.show()

    # Optionally save the QR code image
    qr_img.save("qr_with_image_data.png")

# Example usage
generate_qr_with_image_data("your_image.png")