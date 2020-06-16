#!/usr/bin/env python3

import os, getpass, glob
from PIL import Image

def creates_directory(directory):
    """creates a directory if it does not already exists"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def iterates(directory,pattern):
    """iteretes files over a given directory and returns a list of files with a given pattern"""
    for file in glob.glob(directory + "/" + pattern):
        file_list.append(os.path.basename(file))

def modifies_image_1(file_list):
    """given list of images as argument, it rotates an image 90 degress clockwise, resizes it to 128x128 and saves it as .jpeg format"""
    for im in file_list:
        temp_im = Image.open(path + "/" + im).convert("RGB")
        new_im = temp_im.rotate(270).resize((128,128)).save(dest_folder + im, "JPEG")

if __name__ == "__main__":
    file_list = []
    user = getpass.getuser()
    path = "/home/" + user + "/images"
    dest_folder = "/opt/icons/"
    image_pattern = "ic*"
    creates_directory(dest_folder)
    iterates(path,image_pattern)
    modifies_image_1(file_list)

