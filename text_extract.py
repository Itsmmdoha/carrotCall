import pytesseract
import cv2

# Load screenshot
image_path = "text.png"
image = cv2.imread(image_path)

# Convert to grayscale (improves accuracy)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Run OCR
text = pytesseract.image_to_string(gray)

print("Extracted Text:")
print(text.strip())
