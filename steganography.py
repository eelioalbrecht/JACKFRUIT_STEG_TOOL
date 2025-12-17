import cv2
import numpy as np

# Delimiter
DELIMITER = "1111111111111110"

def text_to_binary(text):
    return ''.join([format(ord(i), "08b") for i in text])

def binary_to_text(binary_data):
    all_bytes = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
    decoded_text = "".join([chr(int(b, 2)) for b in all_bytes])
    return decoded_text

def encode_text_in_image(input_image_path, output_image_path, secret_text):
    image = cv2.imread(input_image_path)
    if image is None:
        raise ValueError("Image not found or invalid format. Use PNG/BMP.")
    binary_secret = text_to_binary(secret_text) + DELIMITER
    flat_image = image.flatten()
    if len(binary_secret) > len(flat_image):
        raise ValueError("Message too long to hide in this image!")
    for i in range(len(binary_secret)):
        val = int(flat_image[i])
        val = (val & 0b11111110) | int(binary_secret[i])
        flat_image[i] = np.uint8(val)
    stego_image = flat_image.reshape(image.shape)
    cv2.imwrite(output_image_path, stego_image)
    print(f"[INFO] Secret text hidden successfully in {output_image_path}")

def decode_text_from_image(stego_image_path):
    image = cv2.imread(stego_image_path)
    if image is None:
        raise ValueError("Stego image not found or invalid format. Use PNG/BMP.")
    flat_image = image.flatten()
    binary_data = ""
    for i in range(len(flat_image)):
        binary_data += str(flat_image[i] & 1)
        if binary_data[-16:] == DELIMITER:
            break
    if DELIMITER not in binary_data:
        raise ValueError("No hidden message found with this scheme!")
    binary_data = binary_data[:-16]
    decoded_text = binary_to_text(binary_data)
    return decoded_text

#-------------------------------------
if __name__ == "__main__":
    print("\n===== IMAGE STEGANOGRAPHY TOOL =====")
    print("1. Encode (Hide Text in Image)")
    print("2. Decode (Extract Text from Image)")
    choice = input("Enter choice (1/2): ").strip()
    if choice == "1":
        in_img = input("Enter input image filename (e.g., input.png): ").strip()
        out_img = input("Enter output stego image filename (e.g., stego.png): ").strip()
        secret = input("Enter secret message to hide: ").strip()
        encode_text_in_image(in_img, out_img, secret)
    elif choice == "2":
        stego_img = input("Enter stego image filename (e.g., stego.png): ").strip()
        message = decode_text_from_image(stego_img)
        print(f"[INFO] Recovered hidden message:\n{message}")
    else:
        print("Invalid choice. Run again and enter 1 or 2.")
