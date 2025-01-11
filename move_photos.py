from PIL import Image

image = Image.open(".jpg")

new_image = image.resize((200, 200))

new_image.save("resized_image.jpg")