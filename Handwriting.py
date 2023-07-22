
from PIL import Image, ImageDraw, ImageFont

def calculate_text_size(text, font_size):
    char_width, char_height = font_size * 0.6, font_size 
    text_width, text_height = char_width * len(text), char_height

    return text_width, text_height

def convert_text_to_handwritten(text, font_path, output_path, image_size=(800, 400), font_size=36, margin=10, text_color=(0, 0, 0)):
    image = Image.new("RGB", image_size, color="white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = calculate_text_size(text, font_size)
        x = (image_size[0] - text_width) / 2
        y = (image_size[1] - text_height) / 2

        draw.text((x, y), text, font=font, fill=text_color)

        image.save(output_path)
    except OSError:
        print(f"Error: Font file '{font_path}' not found.")
        return

if __name__ == "__main__":
    input_text = input("Enter text: ") 
    font_path = "blzee.ttf" 
    output_image_path = "output_image.png"

    convert_text_to_handwritten(input_text, font_path, output_image_path)
