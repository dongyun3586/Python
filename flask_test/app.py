from flask import Flask
from flask import request
from flask import render_template, redirect, url_for, request
from flask import send_from_directory
from werkzeug.utils import secure_filename
import datetime

app=Flask(__name__)

@app.route('/api', methods = ['GET', 'POST'])
def upload_file():
    parameter_dict = request.args.to_dict()
    if 'type' in parameter_dict:
        if request.method == 'POST':
            if parameter_dict['type'] == 'uploads' and 'now' in parameter_dict:
                if request.files['image']:
                    try:
                        f = request.files['image']
                        f.save('upload_image/'+parameter_dict['now'])
                        return {'type': 'success', 'message': 'uploads directory > file upload success!'}
                    except Exception as e:
                        return {'type': 'error', 'message': e}
                else:
                    return {'type': 'error', 'message': 'cannot received file!'}
            else:
                return {'type': 'error', 'message': 'wrong parameter'}
        elif request.method == 'GET':
            if parameter_dict['type'] == 'deeplearning' and 'filename' in parameter_dict:
                if 'filename' in parameter_dict:
                    filename = parameter_dict['filename']
                    # 'upload_image/' + filename 현재 파일 경로
                    # 딥러닝 모델 구동
                    return {'type': 'success', 'message': 'success deeplearning'}
                else:
                    return {'type': 'error', 'message': 'wrong parameter value'}
            else:
                return {'type': 'error', 'message': 'wrong parameter'}
    else:
        return {'type': 'error', 'message': 'no have essential parameter'}

@app.route('/uploads')
def uploads():
    return render_template('uploads.html')

@app.route('/')
def main():
    return redirect(url_for('uploads'))

if __name__ == "__main__": # terminal에서 python 인터프리터로 .py 파일을 실행하면 무조건 이 부분을 찾아 실행합니다.
                           # C의 main
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    app.run(host="0.0.0.0")