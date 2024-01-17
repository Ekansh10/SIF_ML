# from flask import Flask, render_template, request, redirect, url_for
# import os
# import conversion
# import shingles
# import minhash
# import pickle

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'tar.gz', 'rpm','pix','cfg','exe','min.js','log','xlsx','zip','sh','bk','sql', 'jpeg', 'png','jpg'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/')
# def index():
#     files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', files=files)


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return redirect(request.url)

#     files = request.files.getlist('file')

#     for file in files:
#         if file.filename == '':
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

#     return redirect(url_for('index'))


# @app.route('/delete/<filename>')
# def delete_file(filename):
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.exists(file_path):
#         os.remove(file_path)
#     return redirect(url_for('index'))


# @app.route('/delete_files', methods=['POST'])
# def delete_files():
#     selected_files = request.form.getlist('selected_files')
#     for filename in selected_files:
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         if os.path.exists(file_path):
#             os.remove(file_path)
#     return redirect(url_for('index'))

# app.py

# app.py

# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import os
import subprocess
import conversion
import shingles
import minhash
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_folder1 = request.form['folder1']
        input_folder2 = request.form['folder2']
        output_folder_txt = 'C:\\Users\\ekans\\OneDrive\\Documents\\SIF 2023\\flask\\flask\\txt_out'
        output_folder_jpg = 'C:\\Users\\ekans\\OneDrive\\Documents\\SIF 2023\\flask\\flask\\img_out'

        # Process folder1 and folder2
        mapping_folder1, file_counter1 = conversion.process_folder(input_folder1, output_folder_txt, output_folder_jpg, folder_number=1)
        mapping_folder2, file_counter2 = conversion.process_folder(input_folder2, output_folder_txt, output_folder_jpg, folder_number=2, file_counter_start=file_counter1)

        # Combine the mapping dictionaries
        filename_mapping = {**mapping_folder1, **mapping_folder2}

        json_file_path = "C:\\Users\\ekans\\OneDrive\\Documents\\SIF 2023\\mapping.json"
        with open(json_file_path, 'w') as json_file:
            json.dump(filename_mapping, json_file, indent=4)
        # print(file_counter1)
        # print(file_counter2)
        no_shingles = shingles.main()
        redundancy_set = minhash.run_minhash(no_shingles, "C:\\Users\\ekans\\OneDrive\\Documents\\SIF 2023\\docShingleDict.pkl")
        print(redundancy_set)
    return render_template('process.html')

# @app.route('/delete_redundant', methods = ['GET', 'POST'])
# def delete_redundant():
#     if request.method == 'POST':

#     return render_template('result.html')
if __name__ == '__main__':
    app.run(debug=True)
