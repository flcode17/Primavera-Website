from PIL import Image
import os

def resize_images(input_folder, output_folder, max_width, max_height):
    """
    Resize all images in the input_folder and save them to the output_folder.

    Args:
        input_folder (str): Path to the folder containing images to resize.
        output_folder (str): Path to the folder to save resized images.
        max_width (int): Maximum width of the resized image.
        max_height (int): Maximum height of the resized image.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Only process image files
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with Image.open(file_path) as img:
                # Get the original dimensions
                original_width, original_height = img.size

                # Calculate the scaling factor to maintain aspect ratio
                scaling_factor = min(max_width / original_width, max_height / original_height)

                # Calculate the new dimensions
                new_width = int(original_width * scaling_factor)
                new_height = int(original_height * scaling_factor)

                # Resize the image
                resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

                print(f"Resized {filename} to {new_width}x{new_height} and saved to {output_path}")

# Example usage
input_folder = ""  # Replace with your input folder path
output_folder = "output_images"  # Replace with your output folder path
max_width = 145  # Replace with your desired max width
max_height = 145  # Replace with your desired max height

resize_images(input_folder, output_folder, max_width, max_height)
