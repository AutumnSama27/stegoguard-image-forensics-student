from pathlib import Path
import base64

Path("images").mkdir(exist_ok=True)

# Use exact TIU logo image.
png_data = Path("images/TIU1.png").read_bytes()

# Add harmless hidden demo data.
png_data += b"\nCYBER: This is harmless demo hidden data for the StegoGuard lab.\n"

Path("images/student_image.png").write_bytes(png_data)

print("Created images/student_image.png with hidden demo data")
