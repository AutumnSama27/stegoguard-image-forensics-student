from pathlib import Path
import base64

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

# Small valid 1x1 PNG image.
png_data = Path("images/TIU1.png").read_bytes()


Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")
