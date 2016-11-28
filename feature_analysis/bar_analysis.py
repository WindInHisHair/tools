import pandas as pd
import matplotlib.pyplot as plt
from numpy import array


from local_config import columns, others, file_name

def _cluster_index(df):

	raw_index= array(df.index)
	index = [int(round(each/100.0)) for each in raw_index]
	return index

def analyze_data(data, column_name, cluster_data=False):

	if not cluster_data:
		approve = data[column_name][data.status == approve_code].value_counts()
		reject = data[column_name][data.status == reject_code].value_counts()
	else:
		raw_approve = data[column_name][data.status == approve_code].value_counts()
		raw_reject = data[column_name][data.status == reject_code].value_counts()

		raw_approve.index = _cluster_index(raw_approve)
		raw_reject.index = _cluster_index(raw_reject)

		apprve = raw_approve.groupby(raw_approve.index).sum()
		reject = raw_reject.groupby(raw_reject.index).sum()


	approve = approve[approve.index >= 0]
	reject = reject[reject.index >= 0]
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

	for each_attribute in columns:
		analyze_data(data, each_attribute)



if __name__ == '__main__':
	main()
