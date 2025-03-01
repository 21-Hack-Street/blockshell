# -*- coding: utf-8 -*-
# ==================================================
# ==================== META DATA ===================
# ==================================================
__author__ = "Daxeel Soni"
__url__ = "https://daxeel.github.io"
__email__ = "daxeelsoni44@gmail.com"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daxeel Soni"

# ==================================================
# ================= IMPORT MODULES =================
# ==================================================
from flask import Flask, render_template, jsonify
import json
import base64

# Init flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('guide.html')

@app.route('/allblocks')
def mined_blocks():
    """
        Endpoint to list all mined blocks.
    """
    f = open("chain.txt", "r")
    data = json.loads(f.read())
    f.close()
    return render_template('blocks.html', data=data)

@app.route('/block/<hash>')
def block(hash):
    """
        Endpoint which shows all the data for given block hash.
    """
    f = open("chain.txt", "r")
    data = json.loads(f.read())
    f.close()
    for eachBlock in data:
        if eachBlock['hash'] == hash:
            return render_template('blockdata.html', data=eachBlock)

@app.route('/annuaire')
def annuaire():
    """
        Endpoint which shows all the data for given block hash.
    """
    f = open("chain.txt", "r")
    data = json.loads(f.read())
    f.close()
    dico = {}
    del data[0]
    for element in data:
        if (element['index'] in dico):
            del dico[element['index']]
        dico[element['index']] = element
    dico = [v for k,v in dico.items()]
    return render_template('annuaire.html', data=dico)

# Run flask app
if __name__ == '__main__':
    app.run(debug=True)
