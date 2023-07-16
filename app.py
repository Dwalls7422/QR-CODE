from flask import Flask,render_template,request
import qrcode

app= Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')

@app.route('/generate_qr',methods=['POST'])

def generate_qr():
    data=request.form['qr_data']
    qr=  qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')

    img.save('static/qr_code.png')

    return render_template('qr_generated.html')

if __name__ =='__main__':
    app.run(debug=True)
