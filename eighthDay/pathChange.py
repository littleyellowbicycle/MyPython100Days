import os


def main():
    path = input("please input path")
    file_list = os.listdir(path)
    for f in file_list:
        file_name = os.path.splitext(f)[0]
        Olddir = os.path.join(path, f)
        newdir = os.path.join(path, file_name)
        print(newdir)
        os.rename(Olddir, newdir)
    pass


if __name__ == "__main__":
    main()
    pass