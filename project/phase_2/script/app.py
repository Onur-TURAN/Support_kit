from flask import Flask ,render_template ,request
from werkzeug.utils import secure_filename

import Docker_Logs
import database_con

app = Flask(__name__)


@app.route('/upload')
def upoad_file():
    return render_template("upload.html")

@app.route('/uploader' , methods =['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

        return {"data":{
            "filename":f.filename
        }}


@app.route('/analiz',methods=['GET','POST'])
def Database(file_name):
    #results=database_con.SQL_request(database_con.hashing('Level.exe')) // bu çalışacak fakat ilk başta veri tabanı kurulmalı
    results=database_con.hashing('filename')
    return results


@app.route('/docker',methods=['GET','POST'])
def docker():
    #direkt çalıştır.
    logs=Docker_Logs.docker()
    return logs


if __name__ == '__main__':
    app.run()
