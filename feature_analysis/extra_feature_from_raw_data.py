import csv
import pandas as pd
import xgboost as xgb
from sklearn import cross_validation, metrics, linear_model, preprocessing
from sklearn.tree import DecisionTreeClassifier

from local_config import *

	
def load_data(f=file_name , cols=columns, st=status_name, clustered_data=True):
	data =pd.read_table(f)

	if clustered_data:
		return generate_feature_matrix(data, columns_selected=cols, st_name=st)
	else:
		return generate_feature_matrix(data, columns_selected=recent_six_month, st_name=st, clustered_data=clustered_data)


def normalize_data(data):

	x = data.values
	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(x)
	data_norm = pd.DataFrame(x_scaled)
	return data_norm


def generate_feature_matrix(raw_data, columns_selected, st_name, clustered_data=True):

	st = raw_data[st_name]
	st[st == approve_code] = 0
	st[st == reject_code] = 1
	raw_data[st_name] = st
	tmp_data = raw_data.loc[:,columns_selected +[st_name]]
	if clustered_data:
		tmp = tmp_data[(tmp_data>=0) & (tmp_data <= 11)]
	else:
		tmp = tmp_data[tmp_data >= 0]

	data = tmp.dropna(axis=0, how='any')

	label = data[st_name]
	data = data.loc[:, columns_selected]
	return normalize_data(data), label


def cv(clf, data, label):	

	train_x, test_x, train_y, test_y = cross_validation.train_test_split(data, label)

	clf.fit(train_x, train_y)
	predict = clf.predict(test_x)
	auc = metrics.roc_auc_score(test_y, predict)
	return auc


def xgb_cv(data, label):
	train_x, test_x, train_y, test_y = cross_validation.train_test_split(data, label)

	dtrain = xgb.DMatrix(train_x, label=train_y)
	dtest = xgb.DMatrix(test_x, label=test_y)

	param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
	num_round = 2
	bst = xgb.train(param, dtrain, num_round)
	predict = bst.predict(dtest)
	bst.save_model('all_ykd_feature.model')
	bst.dump_model('all_ykd_feature.txt')
	return metrics.roc_auc_score(test_y, predict)


def main():

	tr = DecisionTreeClassifier()
	lr = linear_model.LogisticRegression()

	with open('selected_column_name.csv', 'r') as f:
		r = csv.reader(f)
		feature_col = [each for each in r][0]
	data, label = load_data(cols=feature_col, clustered_data=False)

	print "the data size is %s" %(len(data))
	# data, label = load_data()
	# data = feature_data.loc[:, columns]
	# label = feature_data[status_name]


	print 'Decision Tree auc: %s' %(cv(tr, data, label))
	print 'Logstic Regrssion auc: %s' %(cv(lr, data, label))

	print 'xgboost auc: %s' %(xgb_cv(data, label))


if __name__ == '__main__':
	main()

