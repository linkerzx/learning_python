
import random 
random.seed(1)

class point():
	def __init__(self, coordinates):
		self._coordinates = tuple(coordinates)
		self._dimensions = len(self._coordinates)
	def __getitem__(self):
		return dict((['coordinates',self._coordinates],['dimensions',self._dimensions]))
	def get(self, attr = None):
		return self.__getitem__()[attr] if attr in ('coordinates','dimensions') else self.__getitem__()
	def distance(self, point):
		try:
			if self._dimensions <> point._dimensions:
				raise ValueError
			pdistance = sum([(self.get('coordinates')[i] - point.get('coordinates')[i])**2 
				for i in xrange(0, self.get('dimensions'))])**.5
			return pdistance
		except ValueError:
			print("The point is not of the correct dimensions")
	def distances(self, points):
		return map(self.distance, points)
	def closest(self, points):
		dis = self.distances(points)
		for i in xrange(0,len(dis)):
			if dis[i] == min(dis):
				return i

class cluster_point(point): 
	def __init__(self, coordinates):
		#A cluster point is defined as a point
		#Assignable to a cluster
		point.__init__(self, coordinates)
		self._cluster_assignment = None
	def __getitem__(self):
		return dict((['coordinates', self._coordinates]
			, ['cluster', self._cluster_assignment]
			, ['dimensions',self._dimensions]))
	def get(self, attr = None):
		return self.__getitem__()[attr] if attr in ('coordinates','cluster','dimensions') else self.__getitem__()
	def set_cluster(self, ckey):
		self._cluster_assignment = ckey

class cluster():
	def __init__(self, c_key):
		self._key = c_key
		self._mean = dict((['current',None],['previous',None]))
	def get(self, attr = None):
		results = None
		results = {
			'mean': self._mean['current']
			,'previous_mean': self._mean['previous']
			,'key': self._key
		}.get(attr)
		return results
	def means_changed(self):
		#Determines if the mean changed
		results = None
		if self.get('previous_mean'):
			results = not self.get('mean').get('coordinates') == self.get('previous_mean').get('coordinates')
		else: 
			results = False 
		return results
	def set_mean(self, cluster_points):
		#Recalculates the mean of a cluster based
		#on the cluster points assigned to the cluster
		#Takes as input an Array of cluster_points
		try:
			if [u for u in cluster_points if u.get('dimensions') <> cluster_points[0].get('dimensions')]:
				raise ValueError
			cp = cluster_points
			mean = [sum([u.get('coordinates')[i] for u in cp])/len(cp) for i in xrange(0,len(cp[0].get('coordinates')))]
			if mean:
				self._mean['current'], self._mean['previous'] = point(mean), self._mean['current']
			return self.means_changed()
		except ValueError:
			print("There are points of different dimensionality in the dataset")

class cluster_gen():
	def __init__(self, nbr, arr_dataset):
		self._nbr = nbr
		self._dataset = arr_dataset
		#generate the clusters
		self._clusters = [cluster(i) for i in xrange(0,nbr)]
		self._means_changed = None
		#for each row in the array/dataset assign a point
		self._cluster_points = [cluster_point(u) for u in arr_dataset]
		#initialize the clusters and assign points to clusters
		self.set_means()
		self.assign_closest_mean()
	def get(self, attr = None, cluster_nbr = None):
		if attr in ('all_points','clusters'):
			results = {
				'all_points': self._cluster_points
				,'clusters': self._clusters
			}.get(attr, 'all_points')
		elif attr == 'cluster_points': 
			results = [x for x in self.get('all_points') if x.get('cluster') == cluster_nbr]
		elif attr == 'cluster': 
			results = self.get('clusters')[cluster_nbr]
		elif attr == 'means':
			results = [x.get('mean') for x in self.get('clusters')]
		elif attr == 'means_coordinates':
			results = [x.get('coordinates') for x in self.get('means')]
		return results
	def set_means(self):
		#Calculates the means of each clusters
		clusters = self.get('clusters')
		if self._means_changed:
			self._means_changed = [x.set_mean(self.get('cluster_points',x.get('key'))) for x in clusters]
		else:
			#If the means were not previously defined
			#Assign them to points at random
			random_means = random.sample(self.get('all_points'),self._nbr)
			self._means_changed = [x.set_mean([random_means[x.get('key')]]) for x in clusters]
	def assign_closest_mean(self):
		#For all the points in the dataset 
		#Assign the points to the cluster with the closest mean
		for x in self.get('all_points'):
			closest_mean = x.closest(self.get('means'))
			x.set_cluster(closest_mean)
	def kmeans(self):
		#Performs the K-means clustering
		i = 0
		while True:
			n.set_means()
			n.assign_closest_mean()
			print(n.get('means_coordinates'))
			if i >= 100 or (max(n._means_changed) == 0 and i <> 0):
				break
			i = i + 1



#Generating our sample 
y = random.sample(xrange(1,100001),100)
y = [(u,u^2-2*u) for u in y]	
n = cluster_gen(5,y)	

n.get('means_coordinates')
n.kmeans()

y =[(1,1),(2,1),(0,1),(10,15),(13,10),(4,10),(5,11),(4,11),(12,16)]
n = cluster_gen(3,y)
n.get('means_coordinates')
n.kmeans()
[(x.get('coordinates'),x.get('cluster')) for x in n.get('all_points')]



