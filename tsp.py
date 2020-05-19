import numpy as np
from scipy.spatial.distance import squareform
from time import time
import sys


def generator(no_of_cities):
    final_list=[]
    n = no_of_cities

    for x in range(no_of_cities-1):
        a = np.random.randint(low=10, high=100, size=n-1)
        n = (n-1)
        final_list.append(a.tolist())

    raw = np.array(final_list)
    final = squareform(np.hstack(raw))
    return final


def permutations(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
               
def tsp_algorithm(cities, distances):
    city_num_array = np.arange(1,cities)
    city_num_list = city_num_array.tolist()
    list_perm = list(permutations(city_num_list))
    for element in list_perm:
        element.insert(0, 0)
        element.append(0)

    
    minimum_distance = sys.maxsize
    optimal_path = []
    for path_index,path in enumerate(list_perm):
        path_length = len(path)
        previous = 0
        current = 0
        distance = 0
        for city_index, item in enumerate(path):
            if(city_index == 0):
                continue
            current = item
            distance+=distances[previous][current]
            previous = current
        if(distance < minimum_distance):
            minimum_distance = distance
            optimal_path = path
       
    return minimum_distance,optimal_path


cities = 4 
distances = generator(cities)
start = time()
minimum_distance,optimal_path = tsp_algorithm(cities,distances)
print('--------------Optimal Path----------------')    
print('Minimun Distance: ' + str(minimum_distance))
print(optimal_path)
tottime = time() - start


print( "Found path of length %s in %s seconds" % ( round(cities,4), round(tottime, 4) ) )



