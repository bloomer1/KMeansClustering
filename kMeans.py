import sys


def eucldn_distance(datapoint, cluster_center):
	#print datapoint
	#print cluster_center
	p1 = datapoint.split(",")
	p2 = cluster_center.split(",")
	
	print p1
	print p2
	
	distance = 0
	for cord in zip(p1,p2):
		distance += (int(cord[0]) - int(cord[1]))*(int(cord[0]) - int(cord[1]))

	print distance



def kmeansClustering(data_records,k,init_method,threshold,maxIterations):

	intial_centroids = list()
	initial_clusters  = dict()
	datapoints = list()

	if init_method == 'first':
		for datapoint_idx in data_records:
			intial_centroids.append(data_records[datapoint_idx])
			if len(intial_centroids) == k:
				break
		for idx in data_records:
			datapoints.append(data_records[idx])
		datapoints = datapoints[k:]

	
	elif init_method == 'rand':
		print ''


	#print intial_centroids
	#print datapoints
	for centroid in intial_centroids:
		initial_clusters[centroid] = list()

	#print initial_clusters
	idx = 0;
	for datapoint in datapoints:
		d1 = eucldn_distance(datapoint,intial_centroids[idx])
		#print d1
		break
	




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

	kmeansClustering(data_records,num_clusters,init_method,con_thrlsd,max_itr)








if __name__ == '__main__':
	main()