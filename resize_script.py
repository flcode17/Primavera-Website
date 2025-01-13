from PIL import Image
import os

def resize_images_by_percentage(input_folder, output_folder, scale_percentage):

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        #Gets the path of the image
        file_path = os.path.join(input_folder, filename)

        # Only process image files
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Opens image
            with Image.open(file_path) as img:
                # Get the original dimensions
                original_width, original_height = img.size

                # Calculate the new dimensions based on scale percentage by turning into a decimal
                new_width = int(original_width * (scale_percentage / 100))
                new_height = int(original_height * (scale_percentage / 100))

                # Resize the image
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)

                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

                print(f"Resized {filename} to {new_width}x{new_height} and saved to {output_path}")


input_folder = "/Volumes/Macintosh HD/Andrew/Work/PycharmProjects/Python/Primavera Website/Events/BackToNormal/Photos"  # Replace with your input folder path
output_folder = "/Volumes/Macintosh HD/Andrew/Work/PycharmProjects/Python/Primavera Website/Events/BackToNormal/GalleryPhotos"  # Replace with your output folder path
scale_percentage = 30  #number, not percentage

resize_images_by_percentage(input_folder, output_folder, scale_percentage)
