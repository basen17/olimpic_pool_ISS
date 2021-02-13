from flask import Flask, render_template, url_for, request, jsonify, redirect
import datetime
from simple_pid import PID
from pool import *

#============================================
#=             Input values                 =
#============================================
pool_hight = 2.1            # wysokosc basenu
pool_width = 5.0              # szerokosc basenu
pool_length = 10.0             # dlugosc basenu
P = 1000.0                  # Nastawa regulatora P
I = 0.001                   # Nastawa regulatora I
D = 0.5                     # Nastawa regulatora D
Q = 49000/36000             # [l/0.1s]
Tp = 0.1                    # czas próbkowania

app = Flask(__name__)
pid = PID(P, I, D, output_limits=(-100, 100))
pool = Pool(Q, Tp, pool_length, pool_width, pool_hight, )

now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M:%S")
templateData = {
    'title' : 'Olimpic Pool Regulator',
    'time' : timeString,
    'pool_height' : pool.height,
    'pool_width' : pool.width,
    'pool_length' : pool.length,
    'P' : P,
    'I' : I,
    'D' : D
}

@app.route('/',methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        twl = request.form['target_water_level']
        pool.target_water_level = float(twl)

    return render_template('temp.html', **templateData, current_water_level = pool.current_water_level, target_water_level = pool.target_water_level)

@app.route('/update_date', methods=['POST'])
def update_date():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify('', render_template('update_time.html', time=timeString))


@app.route('/update_current_water_level', methods=['POST'])
def update_current_water_level():
    pid.setpoint = pool.target_water_level
    u=pid(pool.current_water_level)
    pool.CalculateLevelChange(u)
    return jsonify('', render_template('update_current_water_level.html', current_water_level=pool.current_water_level))

@app.route('/update_img', methods=['POST'])
def update_image():
    pool.SetImagePath()
    return jsonify('', render_template('update_img.html', image_path=pool.image_path))


if __name__ == "__main__":
    app.run(debug=True)