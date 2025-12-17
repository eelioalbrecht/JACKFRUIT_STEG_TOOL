# JACKFRUIT_STEG_TOOL
Python script demonstrating image steganography using the Least Significant Bit (LSB) technique for embedding and extracting hidden text.

## Overview

This repository contains a **single-file Python script** that implements **image steganography using the Least Significant Bit (LSB) technique**. The program allows users to hide a secret text message inside an image and later extract it, without visibly altering the image.

The project is intentionally kept simple and self-contained, focusing on core steganography concepts, binary manipulation, and image processing fundamentals.

---

## Key Characteristics

* Single Python script (no frontend/backend separation)
* Command-line interface (CLI)
* Uses LSB substitution for data hiding
* Minimal and educational implementation
* Suitable for undergraduate engineering coursework

---

## Technologies Used

* **Python 3**
* **OpenCV (cv2)** for image reading and writing
* **NumPy** for efficient array and pixel manipulation

---

## How the System Works

1. The secret text message is converted into an 8-bit binary representation.
2. A fixed 16-bit delimiter is appended to mark the end of the message.
3. The input image is read and flattened into a one-dimensional array.
4. Each bit of the secret message replaces the least significant bit of a pixel value.
5. The modified pixel data is reshaped and saved as a stego image.
6. During decoding, LSBs are extracted sequentially until the delimiter is detected.
7. The extracted binary data is converted back into readable text.

---

## File Structure

```
├── steganography.py   # Main script (encode + decode)
├── input.png         # Sample input image
├── stego.png         # Output image with hidden text
└── README.md
```

---

## Usage

Run the script from the terminal:

```bash
python steganography.py
```

### Encoding (Hiding Text)

* Choose option `1`
* Provide input image filename (PNG/BMP recommended)
* Provide output stego image filename
* Enter the secret message

### Decoding (Extracting Text)

* Choose option `2`
* Provide the stego image filename
* The hidden message will be displayed in the terminal

---

## Supported Image Formats

* Recommended: **PNG, BMP**
* Not recommended: JPEG (lossy compression may corrupt hidden data)

---

## Limitations

* Message size is limited by image resolution
* No encryption is applied to the hidden text
* Not resistant to image compression or steganalysis
* Uses a fixed delimiter-based termination scheme

---

## Applications

* Educational demonstration of steganography
* Introductory information security projects
* Understanding binary data embedding in images

---

## Future Improvements

* Encrypt the message before embedding
* Add key-based embedding
* Improve robustness against compression
* Extend to audio or video steganography

---

## Disclaimer

This project is intended strictly for **educational purposes**. Misuse of steganography techniques for unethical or illegal activities is discouraged.

---

## Author

Undergraduate project developed at **PES University** by **Pranav, Nikhil, Pradhyun**.
