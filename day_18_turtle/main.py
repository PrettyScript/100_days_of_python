import colorgram
colors = colorgram.extract('image.jpg', 10)
print(colors[0].rgb.r)
extracted_colors = colors

for color in extracted_colors:
    print(extracted_colors[color])

# hirst_colors = []
