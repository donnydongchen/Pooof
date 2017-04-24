import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

def preprocess_input (DATE, CRS_DEP_TIME, UNIQUE_CARRIER, FL_NUM, ORIGIN_CITY_NAME, DEST_CITY_NAME, filename_metadata):
	# format user input
	DepHr = CRS_DEP_TIME//100
	date_obj = datetime.strptime(DATE,'%m/%d/%y')
	MONTH = date_obj.month
	DAY_OF_WEEK = date_obj.weekday()+1 #DAY_OF_WEEK in original data 1-7

	# add metadata required for model prediction
	input_var = ('MONTH','DAY_OF_WEEK','DepHr','UNIQUE_CARRIER','FL_NUM','ORIGIN_CITY_NAME','DEST_CITY_NAME')
	input_dict = {}
	for i in input_var:
	    input_dict[i] = locals()[i]
	metadata = pd.read_csv(filename_metadata)
	df_lookup = pd.DataFrame(input_dict, index=['i',])
	on_cols = ['UNIQUE_CARRIER','FL_NUM','ORIGIN_CITY_NAME','DEST_CITY_NAME']
	df_input = pd.merge(df_lookup, metadata, how='left', on=on_cols)
	if df_input.isnull().values.any():
	    print 'Historic metadata (ORIGIN/DEST/DISTANCE) needed for modeling not found!'

	return df_input

def make_prediction (df_input, filename_pickle):
	# load trained model
	with open(filename_pickle, 'rb') as handle:
	    model = pickle.load(handle)
	# predict
	# print (model.classes_)
	predictions = model.predict_proba(df_input)
	# print (predictions)
	print ('The probability of delay is {:.0%}'.format(predictions[0][1]))

def main():
	# Preprocess raw user input and make prediction
	df_input = preprocess_input(DATE, CRS_DEP_TIME, UNIQUE_CARRIER, FL_NUM, ORIGIN_CITY_NAME, DEST_CITY_NAME, filename_metadata)
	make_prediction(df_input, filename_pickle)


# User Input Variables
DATE = '06/26/17'
CRS_DEP_TIME = 1103
UNIQUE_CARRIER = 'UA'
FL_NUM = 292
ORIGIN_CITY_NAME = 'San Francisco, CA'
DEST_CITY_NAME = 'Orlando, FL'

# Files Location
filename_path = '/Users/dongchen/Google_Drive/sptp/project/data_science/'
filename_metadata = filename_path+'data/metadata.csv'
filename_pickle = filename_path+'model/final_model.pkl'

main()



