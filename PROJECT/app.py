from flask import Flask ,render_template ,request
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/upload')
def upoad_file():
    return render_template("upload.html")

@app.route('/uploader' , methods =['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


@app.route('/analiz',methods=['GET','POST'])
def analize():

    print("A")



if __name__ == '__main__':
    app.run()
