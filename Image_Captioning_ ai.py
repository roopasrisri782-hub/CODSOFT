from PIL import Image

def analyze_image(image_path):
    try:
        image = Image.open(image_path)

        width, height = image.size
        mode = image.mode
        format_type = image.format

        print("\n----- IMAGE DETAILS -----")
        print("Width :", width)
        print("Height :", height)
        print("Color Mode :", mode)
        print("Image Format :", format_type)

        if width > height:
            caption = "This image appears to be a landscape oriented photograph."
        elif height > width:
            caption = "This image appears to be a portrait oriented photograph."
        else:
            caption = "This image appears to be a square photograph."

        print("\n----- GENERATED CAPTION -----")
        print(caption)

    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print("Error:", e)

print("===================================")
print("        IMAGE CAPTIONING AI        ")
print("===================================")

image_path = input("Enter Image Path: ")

analyze_image(image_path)

print("\nProgram Executed Successfully")
