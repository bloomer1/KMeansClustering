import sys


def process_dataset(dataset):

	data_records = dict()

	for datapoint in dataset:
		data_records[dataset.index(datapoint)] = datapoint


	#print data_records
	return data_records



def read_inputDataset(input_file):
	file_ptr = open(input_file)

	dataset = file_ptr.readlines()
	#print dataset

	dataset = [datapoint.rstrip('\n') for datapoint in dataset]
	#print dataset
	return process_dataset(dataset)



def main():





	if len(sys.argv) != 6:
		print "Usage: python KMeans.py <num_clusters> <intilization_method> <convergence_threshold> <max_iterations> <input_filename>"
		return

	if len(sys.argv) == 6:
		num_clusters = int(sys.argv[1])
		init_method  = sys.argv[2]
		con_thrlsd	 = sys.argv[3]
		max_itr 	 = sys.argv[4]
		input_file   = sys.argv[5]




	#print num_clusters
	#print init_method
	#print con_thrlsd
	#print max_itr
	#print input_file

	data_records = read_inputDataset(input_file)
	








if __name__ == '__main__':
	main()