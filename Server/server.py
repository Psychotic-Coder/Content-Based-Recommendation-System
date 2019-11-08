#USING FLASK TO CREATE A SERVER ON LOCALHOST
#CORS IS USED TO REMOVE CORS ERROR

# -------------------IMPORTS---------------------
# IMPORT FOR SERVER SUPPORT
from flask import Flask, jsonify
from flask_cors import CORS

# IMORT TO GET USER HISTORY
import scr
# IMPORT TO GET FORMATTED PREDICTED DATA
import getData as eng

# INITIALISE FLASK SERVER
app = Flask(__name__)
CORS(app)

# --------------ROUTING FUNCTIONS----------------

# GET REQUEST FOR HISTORY
@app.route('/history', methods = ['GET'])
def getHistory():
    res, key = {}, 0
    for i in scr.data:
        if 'Flipkart' in i:
            res['F'+str(key)] = i
        else:
            res['A'+str(key)] = i
        key += 1
    data = res
    return jsonify(data)

# GET REQUEST FORRECOMMENDER ENGINE
@app.route('/rec', methods = ['GET'])
def getRecommendation():
    #access your DB get your results here
    data = eng.res
    return jsonify(data)

# ----------------DRIVER CODE-----------------
if __name__ == '__main__':
    port = 8000 #CUSTOM PORT FOR SERVER
    app.run(host='0.0.0.0', port=port)
    