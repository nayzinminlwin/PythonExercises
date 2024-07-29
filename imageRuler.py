from PIL import Image

# Load the image and check its size in pixels
filePath = input("Filepath : ")
img = Image.open(filePath)
width_px, height_px = img.size

# Convert pixels to centimeters
width_cm = width_px / 37.7953
height_cm = height_px / 37.7953

print(f"Width: {width_cm} cm, Height: {height_cm} cm")
input("Press Enter to exit!")