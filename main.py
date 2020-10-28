from flask import Flask , render_template, request , flash , redirect, url_for
from werkzeug.exceptions import BadRequestKeyError
import pathlib


from imageW import MakePhoto
import os


CountImages = 0



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.after_request
def add_header(r):

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/imageReady',methods=['POST','GET'])
def ImageRedactor():
    imgName = ''


    for file in os.listdir('static/images/'):
        imgName = file
        imgFile = 'static/images/' + file

    global CountImages
    CountImages += 1
    makPhot = MakePhoto(imgName)





    if request.method == "POST":
        if request.form.get('SubmitImgFil') == 'BtnFilter1':
            ReadyImg = makPhot.BlurImg()
            return render_template('index.html', imgFile=imgFile, ReadyImg=ReadyImg)
        elif request.form.get('SubmitImgFil') == 'BtnFilter2':
            ReadyImg = makPhot.WitoutColors()
            return render_template('index.html', imgFile=imgFile, ReadyImg=ReadyImg)
        elif request.form.get('SubmitImgFil') == 'BtnFilter3':
            ReadyImg = makPhot.FilterPhoto()
            return render_template('index.html', imgFile=imgFile, ReadyImg=ReadyImg)
        else:
            return render_template('index.html',NotFoundImage="Ошибка")

    else:
        return render_template('index.html', NotFoundImage="нечего не случилось")






    # if imgName != "":
    #     imgFile = PathToDir + imgName
    #     print(request.form)
    # #     makPhot = MakePhoto(imgFile,PathToDir)
    # if request.method == "POST":
    #     if request.form.get('SubmitImgFil') == 'BtnFilter1':
    #         ReadyImg = makPhot.BlurImg()
    #         return render_template('index.html',imgFile=imgFile,ReadyImg=ReadyImg)
    #     elif request.form.get('SubmitImgFil') == 'BtnFilter2':
    #         ReadyImg = makPhot.WitoutColors()
    #         return render_template('index.html', imgFile=imgFile, ReadyImg=ReadyImg)
    #     elif request.form.get('SubmitImgFil') == 'BtnFilter3':
    #         ReadyImg = makPhot.FilterPhoto()
    #         return render_template('index.html', imgFile=imgFile,  ReadyImg=ReadyImg)
    #     else:
    #        return  upload_fileTemplates
    #
    #
    # return render_template('index.html',imgFile=imgFile,imgName=imgName)




@app.route('/', methods=['POST',"GET"])
def upload_file():
    return render_template('index.html')


@app.route('/image', methods=['POST',"GET"])
def upload_fileTemplates():
    #  upload image
    for file in os.listdir('static/images/'):
        os.remove('static/images/' + file)

    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            imgFile = 'static/images/' + uploaded_file.filename
            uploaded_file.save(imgFile)
            return render_template('index.html',imgFile=imgFile)
        else:
            return render_template('index.html',NotFoundImage="нет картинки")
    except BadRequestKeyError as  e:
        return "нет картинки ошибка"


def GetFileName():
    try:
        uploaded_file = request.files['file']
    except BadRequestKeyError as e :
        uploaded_file = 'ошибка'
    return uploaded_file.filename








# @app.route('/<string:ImgName>', methods=['POST',"GET"])
# def upload_file_Plus(ImgName):
#     print("Вторая картинка")
#
#     for file in os.listdir('static/images/'):
#         os.remove('static/images/' + file)
#
#     uploaded_file = request.files['file']
#     if uploaded_file.filename != '':
#         imgFile = 'static/images/'+ uploaded_file.filename
#         uploaded_file.save(imgFile)
#         return render_template('index.html',imgFile=imgFile, imgName=uploaded_file.filename)
#     else:
#         return render_template('index.html', NotFoundImage="нет картинки")
#
#
#
#
#






if __name__ == "__main__":
    app.run(debug=True);