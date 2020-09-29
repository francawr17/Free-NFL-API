from flask import Flask, jsonify, request, render_template
import os
from templates import *


app = Flask(__name__, template_folder='templates')
upload = os.getcwd()


@app.route('/')
def teste():
    return render_template('index.html')


# AFC EAST LEAGUE


@app.route('/buf')
def bills():
    return jsonify(render_template('buf.html'))


@app.route('/mia')
def dolphins():
    return jsonify(render_template('mia.html'))


@app.route('/ne')
def patriots():
    return jsonify(render_template('ne.html'))


@app.route('/nyj')
def jets():
    return jsonify(render_template('nyj.html'))


# AFC NORTH LEAGUE


@app.route('/bal')
def ravens():
    return jsonify(render_template('bal.html'))


@app.route('/cin')
def bengals():
    return jsonify(render_template('cin.html'))


@app.route('/cle')
def browns():
    return jsonify(render_template('cle.html'))


@app.route('/pit')
def steelers():
    return jsonify(render_template('pit.html'))


# AFC WEST LEAGUE


@app.route('/den')
def broncos():
    return jsonify(render_template('den.html'))


@app.route('/kc')
def chiefs():
    return jsonify(render_template('kc.html'))


@app.route('/lv')
def raiders():
    return jsonify(render_template('lv.html'))


@app.route('/lac')
def chargers():
    return jsonify(render_template('lac.html'))


# AFC SOUTH LEAGUE

@app.route('/hou')
def texans():
    return jsonify(render_template('hou.html'))


@app.route('/ind')
def colts():
    return jsonify(render_template('ind.html'))


@app.route('/jax')
def jaguars():
    return jsonify(render_template('jax.html'))


@app.route('/ten')
def titans():
    return jsonify(render_template('ten.html'))

# NFC EAST LEAGUE


@app.route('/dal')
def cowboys():
    return jsonify(render_template('dal.html'))


@app.route('/nyg')
def giants():
    return jsonify(render_template('nyg.html'))


@app.route('/phi')
def eagles():
    return jsonify(render_template('phi.html'))


@app.route('/wsh')
def redskins():
    return jsonify(render_template('wsh.html'))


# NFC NORTH LEAGUE

@app.route('/chi')
def bears():
    return jsonify(render_template('chi.html'))


@app.route('/det')
def lions():
    return jsonify(render_template('det.html'))


@app.route('/gb')
def packers():
    return jsonify(render_template('gb.html'))


@app.route('/min')
def vikings():
    return jsonify(render_template('min.html'))


# NFC WEST LEAGUE

@app.route('/ari')
def cardinals():
    return jsonify(render_template('ari.html'))


@app.route('/lar')
def rams():
    return jsonify(render_template('lar.html'))


@app.route('/sf')
def sanf():
    return jsonify(render_template('sf.html'))


@app.route('/sea')
def seahawks():
    return jsonify(render_template('sea.html'))


# NFC SOUTH LEAGUE

@app.route('/atl')
def falcons():
    return jsonify(render_template('atl.html'))


@app.route('/car')
def panthers():
    return jsonify(render_template('car.html'))


@app.route('/no')
def saints():
    return jsonify(render_template('no.html'))


@app.route('/tb')
def buccaneers():
    return jsonify(render_template('tb.html'))


if __name__ == "__main__":
    app.run()
