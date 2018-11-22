from flask import Flask,render_template,request,redirect,url_for
import os
from owernership_share_generator import *
from master_share_generator import *
import subprocess
STATIC_FOLDER = os.getcwd()+'/static/'

app = Flask(__name__)

app.config['STATIC_FOLDER'] = STATIC_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ownership',methods=['GET','POST'])
def ownership():
    if request.method == 'POST':
	originalImg = None
	try:
	    if request.files['originalImg']:
		originalImg = request.files['originalImg']
		filepath = app.config['STATIC_FOLDER']+"original_image.jpg"
		originalImg.save(filepath)
	except Exception as e:
	    print (e)
	watermarkImg = None
        try:
            if request.files['watermarkImg']:
                watermarkImg = request.files['watermarkImg']
                filepath = app.config['STATIC_FOLDER']+"watermark.jpg"
                watermarkImg.save(filepath)
        except Exception as e:
            print (e)
	owernership()
	return render_template('owernershipResult.html')
    else:
	return render_template('ownership.html')

@app.route('/master',methods=['GET', 'POST'])
def master():
    if request.method == 'POST':
	img1 = None
	img2 = None
	img3 = None
	img4 = None
	img5 = None
	img6 = None
	img7 = None
	try:
	    if request.files['img1']:
		img1 = request.files['img1']
		filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_0.jpg"
		img1.save(filepath)
	    if request.files['img2']:
                img2 = request.files['img2']
                filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_1.jpg"
                img2.save(filepath)
	    if request.files['img3']:
                img3 = request.files['img3']
                filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_2.jpg"
                img3.save(filepath)
	    if request.files['img4']:
                img4 = request.files['img4']
                filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_3.jpg"
                img4.save(filepath)
	    if request.files['img5']:
                img5 = request.files['img5']
                filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_4.jpg"
                img5.save(filepath)
	    if request.files['img6']:
                img6 = request.files['img6']
                filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_5.jpg"
                img6.save(filepath)
	    if request.files['img7']:
                img7 = request.files['img7']
                filepath = app.config['STATIC_FOLDER']+"stolen_images/stolen_image_6.jpg"
                img7.save(filepath)

	except Exception as e:
            print (e)
	return redirect(url_for('masterGenerate'))
    else:
        return render_template('master.html')
@app.route('/masterGenerate', methods=['GET','POST'])
def masterGenerate():
    if request.method == 'POST':
	master()
	return render_template('masterResult.html')
    else:
	return render_template('masterGenerate.html')

@app.route('/watermark', methods=['GET','POST'])
def watermark():
    if request.method == 'POST':
	subprocess.call("python runWater.py", shell=True)	
	return render_template('watermarkResult.html')
    else:
	return render_template('watermark.html')

@app.route('/template', methods=['GET','POST'])
def template():
    if request.method == 'POST':
	subprocess.call("python template_match_res.py", shell=True)
	return redirect(url_for('templateResult'))
    else:
	return render_template('template.html')

@app.route('/templateResult', methods=['GET'])
def templateResult():
    with open("result.txt") as f:
	res = []
	for line in f:
	    res.append(line)
    return render_template('templateResult.html', res=res)

if __name__ == "__main__":
    app.secret_key = os.urandom(24).encode('hex')
    app.run(debug=True,host='0.0.0.0',port=5080,ssl_context='adhoc')
