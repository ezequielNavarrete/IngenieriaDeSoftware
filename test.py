
import os

def copy_file(src_file, dest_dir):
    try:
        if not os.path.isfile(src_file):
            print(f"{src_file} does not exist.")
            return
        os.makedirs(dest_dir, exist_ok=True)

        dest_file = os.path.join(dest_dir, os.path.basename(src_file))

       
        with open(src_file, 'rb') as f_src:
            content = f_src.read()
        
        with open(dest_file, 'wb') as f_dest:
            f_dest.write(content)

        print(f"Copied {src_file} to {dest_file}")

    except Exception as e:
        print(f"Error copying file: {e}")

src_file = 'path/to/source/file.txt'
dest_dir = 'path/to/destination/folder'

copy_file(src_file, dest_dir)
