import pandas as pd
import pickle
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")


def preprocess_input(DATE, CRS_DEP_TIME, UNIQUE_CARRIER, FL_NUM, ORIGIN, DEST, filename_metadata):
    # format user input
    DepHr = int(CRS_DEP_TIME) // 100
    date_obj = datetime.strptime(DATE, '%m/%d/%y')
    MONTH = date_obj.month
    DAY_OF_WEEK = date_obj.weekday() + 1  # DAY_OF_WEEK in original data 1-7
    FL_NUM = int(FL_NUM)

    # compile user input into a dict
    input_var_list = ['MONTH', 'DAY_OF_WEEK', 'DepHr', 'UNIQUE_CARRIER', 'FL_NUM', 'ORIGIN', 'DEST']
    input_value_list = [MONTH, DAY_OF_WEEK, DepHr, UNIQUE_CARRIER, FL_NUM, ORIGIN, DEST]
    input_dict = dict(zip(input_var_list, input_value_list))

    # add metadata (distance)
    metadata = pd.read_csv(filename_metadata)
    df_lookup = pd.DataFrame(input_dict, index=['i', ])
    on_cols = ['ORIGIN', 'DEST']
    df_input = pd.merge(df_lookup, metadata, how='left', on=on_cols)
    if df_input.isnull().values.any():
        print 'Historic metadata (DISTANCE) needed for modeling not found!'
    return df_input


def make_prediction(df_input, filename_pickle):
    # load trained model
    with open(filename_pickle, 'rb') as handle:
        model = pickle.load(handle)
    # predict
    predictions = model.predict_proba(df_input)
    return 'The probability of delay is {:.0%}'.format(predictions[0][1])


def main():
    # Pre-process raw user input and make prediction
    df_input = preprocess_input(DATE, CRS_DEP_TIME, UNIQUE_CARRIER, FL_NUM, ORIGIN, DEST,
                                filename_metadata)
    predictions = make_prediction(df_input, filename_pickle)
    print (predictions)


if __name__ == '__main__':
    # execute only if run as a script

    # User Input Variables
    DATE = '06/26/17'
    CRS_DEP_TIME = '1103'
    UNIQUE_CARRIER = 'DL'
    FL_NUM = '104'
    ORIGIN = 'ATL'
    DEST = 'BOS'

    # Files Location
    filename_path = ''
    filename_metadata = filename_path + 'data/metadata.csv'
    filename_pickle = filename_path + 'model/final_model.pkl'

    main()
