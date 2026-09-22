# Smart Eye OCR Pipeline

A small Python-based OCR pipeline created for the Smart Eye AI/ML, Technology Research Internship technical challenge.

## What it does

The pipeline:

1. Takes an image as input.
2. Resizes the image.
3. Converts it to grayscale.
4. Applies Gaussian blur to reduce small noise.
5. Uses Otsu thresholding to create a cleaner black-and-white image.
6. Uses Tesseract OCR to extract text.
7. Prints the extracted text and saves it to `output/result.txt`.

## Tech used

- Python
- OpenCV
- Tesseract OCR
- pytesseract

## Project structure

```text
smart-eye-ocr-pipeline/
├── main.py
├── requirements.txt
├── README.md
├── sample_input/
└── output/
```

## Installation

### 1. Install Python packages

```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR

On Windows, install Tesseract OCR and make sure its executable is available to Python.

If it is installed in the default location but Python cannot find it, add this line in `main.py` before calling `image_to_string`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Run

```bash
python main.py sample_input/document.png
```

The extracted text will be printed in the terminal and saved to:

```text
output/result.txt
```

## Example

Input:

```text
Name: Sayan Debnath
Course: B.Tech
Department: Electrical & Computer Engineering
```

Expected OCR output will be similar to:

```text
Name: Sayan Debnath
Course: B.Tech
Department: Electrical & Computer Engineering
```

OCR accuracy can vary depending on image quality, font, lighting, blur, skew and background noise.

## Limitations

This is a simple baseline OCR pipeline. It may perform poorly on heavily blurred, rotated, low-light or complex-background images. A future version could add deskewing, adaptive thresholding, perspective correction, multiple preprocessing variants, confidence scoring and a stronger OCR engine such as PaddleOCR.
