import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_base = script_dir 

copy_map = {
    "~/.config/i3/config": "i3",
    "~/.config/fish/config.fish": "fish",
    "~/.config/rofi/ayaka.rasi": "rofi",
    "~/anime.txt": "ascii", 
    "~/Documents/usefull/hints.txt": "hints",
    "~/Documents/usefull/nnn.txt": "hints"
}

def copy_item(src: str, relative_dest: str):
    # from home dir
    src = os.path.expanduser(src)
    dest = os.path.join(repo_base, relative_dest)

    try:
        if not os.path.exists(src):
            print(f"> failed to copy {src}: source not found")
            return

        os.makedirs(os.path.dirname(dest), exist_ok=True)

        if os.path.isdir(src):
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print(f"> successfully copied directory {src} to {relative_dest}")
        else:
            shutil.copy2(src, dest)
            print(f"> successfully copied file {src} to {relative_dest}")
    except Exception as e:
        print(f"> failed to copy {src} to {relative_dest}: {e}")

if __name__ == "__main__":
    for src_path, relative_dest in copy_map.items():
        copy_item(src_path, relative_dest)
