#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import uuid

from flask import Flask, jsonify, flash, request, redirect, url_for, make_response, render_template
from werkzeug.utils import secure_filename


from app.main.utils import allowed_file
from flask import current_app as app
from . import main
from app.main.animegan.AnimeGAN import AnimeGAN

@main.route('/')
def upload_form():
	return render_template('upload.html')

@main.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.content_type):

        filename = secure_filename(file.filename)
        # filename = str(uuid.uuid4()) + ".png"
        # filename = filename + 
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        flash('Image successfully uploaded and displayed below')

        """Deep learning model"""
        output_name = str(uuid.uuid4()) + ".png"

        aniGAN = AnimeGAN()
        aniGAN.runInference(save_path, os.path.join(app.config['UPLOAD_FOLDER'], output_name))


        return render_template('upload.html', filename=output_name)
    else:
        return "No image found", 400
    
@main.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    main.run()