import os
from PIL import Image #Python Imaging Library
from flask import current_app

def add_profile_pic(pic_upload,username):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    store_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/profile_pics', store_filename)
    output_size = (200,200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return store_filename