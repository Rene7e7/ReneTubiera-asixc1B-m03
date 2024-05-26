import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Create a blank canvas
width, height = 800, 1200
background_color = (255, 255, 255)
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Draw the background - simple representation of Tibidabo mountain
# Sky
draw.rectangle([(0, 0), (width, height//2)], fill=(135, 206, 235))  # Light blue sky

# Mountain and city elements
draw.polygon([(0, height//2), (width, height//2), (width, height), (0, height)], fill=(34, 139, 34))  # Green mountain base
draw.rectangle([(200, 600), (220, 800)], fill=(192, 192, 192))  # Torre de Collserola
draw.rectangle([(250, 500), (350, 700)], fill=(255, 255, 255))  # Sagrat Cor

# Simple cityscape
for i in range(0, width, 50):
    draw.rectangle([(i, 800), (i+30, 1000)], fill=(169, 169, 169))  # Grey buildings

# Draw the anime boy
boy_color = (0, 0, 0)
draw.ellipse([(300, 300), (500, 500)], outline=boy_color, width=3)  # Head
draw.line([(400, 500), (400, 800)], fill=boy_color, width=8)  # Body
draw.line([(400, 600), (300, 700)], fill=boy_color, width=8)  # Left arm
draw.line([(400, 600), (500, 700)], fill=boy_color, width=8)  # Right arm
draw.line([(400, 800), (350, 1000)], fill=boy_color, width=8)  # Left leg
draw.line([(400, 800), (450, 1000)], fill=boy_color, width=8)  # Right leg

# Add headphones
draw.ellipse([(350, 350), (450, 450)], outline=boy_color, width=3)  # Headphones
draw.line([(350, 400), (300, 400)], fill=boy_color, width=3)  # Left headphone wire
draw.line([(450, 400), (500, 400)], fill=boy_color, width=3)  # Right headphone wire

# Add dragon design on arms
dragon_color = (255, 0, 0)
draw.arc([(280, 700), (320, 740)], start=0, end=360, fill=dragon_color, width=3)  # Left arm dragon
draw.arc([(480, 700), (520, 740)], start=0, end=360, fill=dragon_color, width=3)  # Right arm dragon

# Save the image
file_path = "/mnt/data/anime_boy_tibidabo.png"
image.save(file_path)

file_path
