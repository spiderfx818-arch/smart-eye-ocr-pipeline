import argparse
from pathlib import Path

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    # Resize for better OCR performance
    height, width = image.shape[:2]
    scale = 2
    image = cv2.resize(image, (width * scale, height * scale))

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce small noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Convert to a clean black/white image
    processed = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return processed


def extract_text(image_path: str) -> str:
    processed = preprocess_image(image_path)

    # psm 6 works well for a block of text
    text = pytesseract.image_to_string(processed, config="--psm 6")
    return text.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Simple Python OCR pipeline using OpenCV + Tesseract."
    )
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument(
        "--output",
        default="output/result.txt",
        help="Path for saving extracted text",
    )
    args = parser.parse_args()

    text = extract_text(args.image)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text + "\n", encoding="utf-8")

    print("\n===== OCR OUTPUT =====\n")
    print(text if text else "[No text detected]")
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()
