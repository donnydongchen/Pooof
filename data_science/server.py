from flask import Flask, redirect, url_for, request
from prediction import preprocess_input, make_prediction

app = Flask(__name__)

# Files Location
filename_path = ''
filename_metadata = filename_path + 'data/metadata.csv'
filename_pickle = filename_path + 'model/final_model.pkl'


@app.route('/')
def index():
    return app.send_static_file('form.html')


@app.route('/form', methods=['POST'])
def form():
    DATE = request.form['DATE']
    CRS_DEP_TIME = request.form['CRS_DEP_TIME']
    UNIQUE_CARRIER = request.form['UNIQUE_CARRIER']
    FL_NUM = request.form['FL_NUM']
    ORIGIN = request.form['ORIGIN']
    DEST = request.form['DEST']
    return redirect(url_for('success',
                            DATE=DATE,
                            CRS_DEP_TIME=CRS_DEP_TIME,
                            UNIQUE_CARRIER=UNIQUE_CARRIER,
                            FL_NUM=FL_NUM,
                            ORIGIN=ORIGIN,
                            DEST=DEST
                            ))
    # the url redirect to is
    # 'http://0.0.0.0:5000/success?ORIGIN=ATL&CRS_DEP_TIME=1103&UNIQUE_CARRIER=UA&DATE=06%2F26%2F17&DEST=BOS&FL_NUM=292'


@app.route('/success', methods=['GET'])
def success():
    DATE = request.args.get('DATE') # get the key/value pairs in the URL query string from /form
    CRS_DEP_TIME = request.args.get('CRS_DEP_TIME')
    UNIQUE_CARRIER = request.args.get('UNIQUE_CARRIER')
    FL_NUM = request.args.get('FL_NUM')
    ORIGIN = request.args.get('ORIGIN')
    DEST = request.args.get('DEST')
    df_input = preprocess_input(DATE, CRS_DEP_TIME, UNIQUE_CARRIER, FL_NUM, ORIGIN, DEST, filename_metadata)
    res = make_prediction(df_input, filename_pickle)
    return res


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)