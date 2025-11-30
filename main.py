import argparse
import os
# print(argparse.__file__)

#              function DigitalHealthIdPage

parser = argparse.ArgumentParser()

parser.add_argument("-p", "-path", required=True,
                    help="Full path of the directory/file")

parser.add_argument("-k","-keyword", required=True,
                    help="The keyword to search for in directory/file")

parser.add_argument("-ext", "-extension", 
                    nargs='+',  # Allows multiple inputs
                    help="The file extensions to be included in the search (space-separated)\n[OPTIONAL]")      #multiple support

args = parser.parse_args()
# print(type(args.ext))
# print(args)

skip = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico", ".tiff", ".mp3", ".wav", ".mp4", ".avi", ".mov", ".mkv", ".zip", ".tar", ".gz", ".rar", ".7z", ".exe", ".dll", ".so", ".bin", ".class", ".o", ".ttf", ".otf", ".woff", ".woff2", ".pdf", ".docx", ".xlsx", ".pptx"]

path = args.p


def should_process(file, ext):
    if file.endswith(tuple(skip)):
        return False
    if ext:
        if file.endswith(tuple(ext)):
            return True
        else:
            return False
    return True



if os.path.exists(path):
    if os.path.isdir(path):  #has subfolders
        has_subfolders = any(os.path.isdir(os.path.join(path, d)) for d in os.listdir(path))
        if has_subfolders:
            for root, dirs, files in os.walk(path):

                for dir, file in zip(dirs, files):
                    if should_process(file, args.ext):
                        p = os.path.join(root, file)
                        try:
                            with open(p, "r", encoding="utf-8") as f:
                                lines = f.readlines()
                                for index, line in enumerate(lines, start=1):
                                    if args.k in line:
                                        print(f"Keyword found in file {dir} {file} \033[93m- line {index}: \033[32m{line.strip()}\033[0m")
                        except UnicodeDecodeError:
                            pass

        else:  #no subfolders
            for file in os.listdir(path):
                if should_process(file, args.ext):
                    p = os.path.join(path, file)
                    try:
                        with open(p, "r", encoding="utf-8") as f:
                            for index, line in enumerate(f, start=1):
                                if args.k in line:
                                    print(f"Keyword found in file \033[36m{file}\033[0m \033[93m- line {index}: \033[32m{line.strip()}\033[0m")
                    except UnicodeDecodeError:
                        pass

    elif os.path.isfile(path):  # file path directly given
        if should_process(ext=args.ext, file=os.path.basename(path)):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for index, line in enumerate(f, start=1):
                        if args.k in line:
                            print(f"Keyword found in file \033[36m{os.path.basename(path)} \033[93m- line {index}: \033[32m{line.strip()}\033[0m")
            except UnicodeDecodeError:
                pass

else:
    print("The provided path {path} does not exist on your system!")