import os

name_dir = ["first", "second"]


def dirs_new(name):
    for a in name:
        try:
            os.mkdir(a)
            print(f"Папка {a} создана!")
        except:
            print(f"Папка {a} уже была создана!")


def new_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file_write:
        file_write.write("Это текстовый файл")


def rm_file(file, rnm_file):
    os.rename(file, rnm_file)


def cp_file(file, file_go):
    os.system(f"cp {file} {file_go}")


def zip_file(file):
    if os.path.isdir(file.split(".")[0]):
        return "Такой файл уже распокован"
    else:
        os.system(f"unzip {file}")


def dir_names(path):
    return [name for name in os.listdir(path=path) if os.path.isdir(os.path.join(path, name))]


def file_details(file_name):
    with open(file_name, "r", encoding="utf-8") as file_write:
        file_write.read()


if __name__ == "__main__":
    dirs_new(name_dir)
    new_file("first/text.txt")
    rm_file("first/text.txt", "second/text_second.txt")
    cp_file("second/text_second.txt", "first/text.txt")
    zip_file("task.zip")
    dir_name = dir_names("task")
    print(dir_name)
