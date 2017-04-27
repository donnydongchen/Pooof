from flask import Flask, redirect, url_for, request
from prediction import preprocess_input, make_prediction

app = Flask(__name__)

# Files Location
filename_path = ''
filename_metadata = filename_path+'data/metadata.csv'
filename_pickle = filename_path+'model/final_model.pkl'

@app.route('/success/', methods=['POST', 'GET'])
def success():
    DATE = request.args.get('DATE')
    CRS_DEP_TIME = request.args.get('CRS_DEP_TIME')                           
    UNIQUE_CARRIER = request.args.get('UNIQUE_CARRIER')  
    FL_NUM = request.args.get('FL_NUM') 
    ORIGIN_CITY_NAME = request.args.get('ORIGIN_CITY_NAME') 
    DEST_CITY_NAME = request.args.get('DEST_CITY_NAME') 
    df_input = preprocess_input(DATE, CRS_DEP_TIME, UNIQUE_CARRIER, FL_NUM, ORIGIN_CITY_NAME, DEST_CITY_NAME, filename_metadata)
    res = make_prediction(df_input, filename_pickle)
    return res

@app.route('/')
def index():
    return app.send_static_file('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    DATE = request.form['DATE']
    CRS_DEP_TIME = request.form['CRS_DEP_TIME']
    UNIQUE_CARRIER = request.form['UNIQUE_CARRIER']
    FL_NUM = request.form['FL_NUM']
    ORIGIN_CITY_NAME = request.form['ORIGIN_CITY_NAME']
    DEST_CITY_NAME = request.form['DEST_CITY_NAME']
    return redirect(url_for('success',
    	DATE = DATE,
    	CRS_DEP_TIME = CRS_DEP_TIME,
    	UNIQUE_CARRIER = UNIQUE_CARRIER,
    	FL_NUM = FL_NUM,
    	ORIGIN_CITY_NAME = ORIGIN_CITY_NAME,
    	DEST_CITY_NAME = DEST_CITY_NAME
    ))

if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0", port=5000)