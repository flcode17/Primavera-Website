import os

def rename_photos(folder_path):
    try:
        # name of photos
        prefix = "G"
        counter = 1

        # List and filter photo files
        photo_files = []
        for f in os.listdir(folder_path):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                photo_files.append(f)

        # Sort files by name
        photo_files.sort()
        # Rename files
        for file_name in photo_files:
            # Extract file extension
            fname, extension = os.path.splitext(file_name)

            # Generate new name
            new_name = f"{prefix}{counter}{extension}"

            # Full paths
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)

            # Rename file
            os.rename(old_path, new_path)

            # Increment counter
            counter += 1

        print(f"Successfully renamed {counter - 1} photos.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
rename_photos(r"C:\Users\Andrew Sergeyev\PycharmProjects\Python\Primavera Website\Events\BackToNormal\Photos")
