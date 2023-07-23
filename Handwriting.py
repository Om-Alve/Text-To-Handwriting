
from PIL import Image, ImageDraw, ImageFont
import textwrap

def calculate_text_size(text, font_size):
    char_width, char_height = font_size * 0.8, font_size 
    text_width, text_height = char_width * len(text), char_height

    return text_width, text_height

def convert_text_to_handwritten(text, font_path, output_path, image_size=(600,800), font_size=36, margin=10, text_color=(0, 0, 0)):
    image = Image.new("RGB", image_size, color="white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = calculate_text_size(text, font_size)
        x = (image_size[0] - text_width) / 2
        y = (image_size[1] - text_height) / 2

        draw.multiline_text((20,20), text, font=font, fill=text_color)

        image.save(output_path)
        image.show()
    except OSError:
        print(f"Error: Font file '{font_path}' not found.")
        return

if __name__ == "__main__":
    input_text = """
Hey this is me Om. 
This text will be converted to handwritten text.
Hello world
""" 
    
    width = int((600*.95)/(36*0.6))
    input_text = textwrap.fill(text = input_text,width=width)
    font_path = "blzee.ttf" 
    output_image_path = "output_image.png"

    convert_text_to_handwritten(input_text, font_path, output_image_path)
