from flask import Flask, render_template


app = Flask(__name__, template_folder=r"c:\Users\User\OneDrive\Desktop\plantilla1\template")


@app.route('/')
def home():
    return render_template('plantilla.html', creador="Jared Fernando Olmeda Castillo")


@app.route('/plantilla')
def plantilla():
    return render_template('plantilla.html')


if __name__ == '__main__':
    app.run(debug=True)
