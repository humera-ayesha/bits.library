import qrcode
from PIL import Image

# Step 1: Define the URL to your library website
url = "https://humera-ayesha.github.io/library-website/"  # Change to your live hosted URL later

# Step 2: Create QR code with high error correction
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Step 3: Load your logo
logo = Image.open("logo.png");  # Make sure 'logo.png' is in the same directory

# Resize logo
logo_size = 60
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Step 4: Paste logo at center of QR
qr_width, qr_height = qr_img.size
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Step 5: Save QR code image
qr_img.save("library_qrcode.png")

print("QR code with logo saved as 'library_qrcode.png'")
