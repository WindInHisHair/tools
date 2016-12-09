import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

from numpy import array 
from sklearn import preprocessing, cross_validation, metrics

from local_config import columns, others, file_name, default_cluster_value_top, default_cluster_value_bottom, approve_code, reject_code, recent_six_month

def _cluster_index(df):

	raw_index= array(df.index)
	index = [int(round(each/100.0)) for each in raw_index]
	return index

def clean_data(raw_data, column_name, top=default_cluster_value_top, bottom=default_cluster_value_bottom):
        import ipdb; ipdb.set_trace()
        data = raw_data[(raw_data[column_name]) >= bottom & (raw_data[column_name] <= top)]
        return data


def analyze_data(data, column_name, cluster_data=False):

	if not cluster_data:
		approve = data[column_name][data.apply_status == approve_code].value_counts()
		reject = data[column_name][data.apply_status == reject_code].value_counts()
                #approve = clean_data(approve, column_name)
                #reject = clean_data(reject, column_name)
	else:
		raw_approve = data[column_name][data.apply_status == approve_code].value_counts()
		raw_reject = data[column_name][data.apply_status == reject_code].value_counts()

		raw_approve.index = _cluster_index(raw_approve)
		raw_reject.index = _cluster_index(raw_reject)

		approve = raw_approve.groupby(raw_approve.index).sum()
		reject = raw_reject.groupby(raw_reject.index).sum()


	approve = approve[approve.index >= 0]
	reject = reject.fillna(0)
	dt = pd.DataFrame({'Approve':approve, 'Reject':reject})
	dt.plot(kind='bar', stacked=True)

	fig = plt.Figure()
	plt.title(column_name)

	plt.ylabel('Approve or Reject')
	plt.xlabel(column_name)

	# plt.show()
	file = '_'.join([column_name, 'png'])
	plt.savefig(file)


def main():
	data = pd.read_table(file_name)

	# for each_attribute in columns:
	# 	analyze_data(data, each_attribute)

	for each in recent_six_month:
		analyze_data(data, each, True)


if __name__ == '__main__':
	main()
