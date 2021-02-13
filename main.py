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
}

@app.route('/',methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        twl = request.form['target_water_level']
        pool.target_water_level = float(twl)

    return render_template('temp.html', **templateData, current_water_level = pool.current_water_level)

@app.route('/update_date', methods=['POST'])
def update_date():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify('', render_template('update_time.html', time=timeString))

# @app.route('/set_target_water_level', methods=['POST'])
# def set_target_water_level():
#     if request.method == 'POST':
#         pool.target_water_level = request.form['target_water_level']
#         templateData.update(pool.target_water_level)
#     return render_template('temp.html', **templateData)

@app.route('/update_current_water_level', methods=['POST'])
def update_current_water_level():
    pid.setpoint = pool.target_water_level
    u=pid(pool.current_water_level)
    pool.CalculateLevelChange(u)
    return jsonify('', render_template('update_current_water_level.html', current_water_level=pool.current_water_level))

# @app.route('/update', methods=['POST'])
# def update_values():
#     if request.method == 'POST':
#         twl = request.form['target_water_level']
#         twl = pool.CalculateLevelChange(twl)
#         # pool.SetImagePath
#         # templateData['target_water_level'] = target_water_level

#     return jsonify('', render_template('update_pool.html', current_water_level = pool.current_water_level))





# @app.route('/update')
#     pool.

# @app.route('/', methods=['GET', 'POST'])
# def homepage():
#     now = datetime.datetime.now()
#     timeString = now.strftime("%Y-%m-%d %H:%M:%S")
#     templateData = {
#             'title' : 'Olimpic Pool Regulator',
#             'time' : timeString,
#             #'image_path' : pool.image_path,
#             #'image_path' : 'img/water_level_0.0.png',
#             'current_water_level' : pool.current_water_level,
#             'target_water_level' : pool.target_water_level

#         }
#     if request.method == 'POST':
#         twl = request.form['target_water_level']
#         print(pool.target_water_level,flush=True)
#         pool.target_water_level = twl
#         print(pool.target_water_level)
#         pool.current_water_level = twl
        
        
#         return render_template('temp.html', **templateData)
#     else:
#         return render_template('temp.html', **templateData)
    #return render_template('home.html', img=image_path, water_level=wt, set_water_level=swl, approx_time=a_time)



# @app.route('/update_values', methods=['POST', 'GET'])
# def updatevalues():
#     if request.method == 'POST':






if __name__ == "__main__":
    app.run(debug=True)