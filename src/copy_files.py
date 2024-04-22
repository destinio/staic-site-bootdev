import os
import shutil


def copy_files(src, des):
    if not os.path.exists(des):
        os.mkdir(des)

    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        des_path = os.path.join(des, file)

        print(f"copying {src_path} to {des_path}")

        if os.path.isfile(src_path):
            shutil.copy(src_path, des_path)

        else:
            copy_files(src_path, des_path)
