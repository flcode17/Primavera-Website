from PIL import Image
import os

def resize_images_by_percentage(input_folder, output_folder, scale_percentage):
    """
    Resize all images in the input_folder by a scale percentage and save them to the output_folder.

    Args:
        input_folder (str): Path to the folder containing images to resize.
        output_folder (str): Path to the folder to save resized images.
        scale_percentage (float): Percentage to scale the images (e.g., 50 for 50%).
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

                # Calculate the new dimensions based on scale percentage
                new_width = int(original_width * (scale_percentage / 100))
                new_height = int(original_height * (scale_percentage / 100))

                # Resize the image using LANCZOS resampling
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)

                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

                print(f"Resized {filename} to {new_width}x{new_height} and saved to {output_path}")

# Example usage
input_folder = "/Volumes/Macintosh HD/Andrew/Work/PycharmProjects/Python/Primavera Website/Events/003_Afterburn/Input_Photos"  # Replace with your input folder path
output_folder = "/Volumes/Macintosh HD/Andrew/Work/PycharmProjects/Python/Primavera Website/Events/ResizedPhotos"  # Replace with your output folder path
scale_percentage = 50  # Replace with your desired scale percentage (e.g., 50 for 50%)

resize_images_by_percentage(input_folder, output_folder, scale_percentage)
