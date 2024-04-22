import os
import shutil

from copy_files import copy_files
from generate_page import generate_pages

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"


def main():
    if os.path.exists(static_path):
        if os.path.exists(public_path):
            shutil.rmtree(public_path)

        copy_files(static_path, public_path)

        generate_pages(content_path, template_path, public_path)


main()
