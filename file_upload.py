# 참고 링크 : https://flask.palletsprojects.com/en/0.12.x/patterns/fileuploads/
import os
import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


# 업로드 HTML 렌더링
@app.route('/upload')
def render_file():
    return render_template('upload.html')


# 파일 업로드 처리
@app.route('/file_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.' \
                   + file.filename.rsplit('.', 1)[1].lower()
        file.save(os.path.join(os.getcwd() + '\\uploads', filename))
    return 'uploads 디렉토리 -> 파일 업로드 성공!'


# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)
