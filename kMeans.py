import sys
import math


def new_centroids(initial_clusters):
	updated_centroids = dict()
	avg_list = list()

	for key,value in initial_clusters.iteritems():
		#print key,value
		v_list = list()
		vsum_list = list()
		finalv_list = list()
		
		key_list = key.split(",")
		key_list = [float(a) for a in key_list]
		for i in value:
			x = i.split(",")
			x = [float(a) for a in x]
			v_list.append(x)
		#print v_list
		vsum_list = map(sum, zip(*v_list))
		#print vsum_list
		#print key_list
		finalv_list.append(key_list)
		finalv_list.append(vsum_list)
		#print finalv_list
		finalv_list = map(sum, zip(*finalv_list))
		#print finalv_list
		if finalv_list:
			finalv_list = [x /(len(value) + 1) for x in finalv_list]
			avg_list.append(finalv_list)
		else:
			finalv_list = key_list
			avg_list.append(finalv_list)
	#print avg_list

		

		

	
	



	#return updated_centroids

def eucldn_distance(datapoint, cluster_center):
	#print datapoint
	#print cluster_center
	p1 = datapoint.split(",")
	p2 = cluster_center.split(",")
	
	#print p1
	#print p2
	

	distance = 0
	for cord in zip(p1,p2):

		distance += (float(cord[0]) - float(cord[1]))*(float(cord[0]) - float(cord[1]))

	#print math.sqrt(distance)
	return math.sqrt(distance)



def kmeansClustering(data_records,k,init_method,threshold,maxIterations):

	intial_centroids = list()
	initial_clusters  = dict()
	datapoints = list()
	no_of_itr_completed = 0

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
	
	min_diff = float("inf")
	
	for datapoint in datapoints:
		for center in intial_centroids:
			d = eucldn_distance(datapoint,center)
			if min_diff > d:
				min_diff = d
				ct = center
		initial_clusters[ct].append(datapoint)


	#print initial_clusters
	#print len(initial_clusters['1.5,1.5'])
	no_of_itr_completed += 1


	updated_centroids = dict()
	updated_clusters  = dict()

	updated_centroids = new_centroids(initial_clusters)




			
	




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