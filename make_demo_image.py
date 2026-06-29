from pathlib import Path
import base64


Path("images").mkdir(exist_ok=True)

# Small valid 1x1 PNG image.
png_data = Path("images/TIU1.png").read_bytes()
png_data += b"\nCYBER: This is harmless demo hidden data for the StegoGuard lab.\n"

Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")
