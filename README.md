 This reposritory holds my learning experiments with MapReducer
 
# install requirements
pip install mrjob
 
# more advanced experiments
## the most rated move
this example runs two mapreduce steps. the first one calculate the number of rating per movieID.
the second one first map MOVIEID to MOVIENAME and the find the movie with the maximum rating.
```python
python most_rated_movie.py --items=../../datasets/ml-100k/u.item ../../datasets/ml-100k/u.data
```

## the most loved friends 
this example find the friend who has the largest size of social network. It first loads the friends graph
and count the the number of friends per person. In the second mapreduce stage, it maps the peopleID to names and then output the person with the maximum number of friends
```python
python most_loved_friends.py --names=../../datastes/Marvel-Names.txt ../../datasets/Marvel-Graph.txt
```

## bread first search 
this experiment shows the application of mapreduce in solving the bread first search problem. It calculates the degree of separation or the length of the shortest path
from one friend to another from a social graph. 
- the input to the algorithm is a source person ID and a destination person ID.
- from the source ID, we generate a graph, traveling states and travelling distances for every people in the network. At this stage, only the source vertex is touched, so its state is "VISITED"
and its distance is zero. All the other vertices have distance of infinity and states of "UNVISITED"
- each iteration of BFS is done by mapreduce as following. First, the mapper will emit/yield nodes for each person in the graph and all of its adjacent nodes.
The sort/shuffle step will then merge all the incoming nodes for each node. The shortest distance so far will be
extracted from all of the incoming nodes.
- __problem__: this BFS mapreduce approach will expolore all paths in parallel in a graph, which causes a lot of uncessary travelling
because only travelling on the frontier is useful. 
- __instruction__:
    - run gen_initial_dfs.py to generate the inital travelling graph state for a source person.
    - run dos_bfs.py to calculate the distance of the first DFS iteration.

# fundamental experiments
calculate average number of friends by age
```python
python FriendsByAge.py ./datasets/fakefriends.csv
```

calculate min temperature thorugh out the year by location
```python
python MinTemperature.py ./datasets/1800.csv
```

count word frequencies using regular expression
```python
python WordFrequency.py ./datasets/Book.txt
```
demonstrate a map reduce pipeline of two stages that first, count the occurency of words and then order unique words by their popularity.
```python
python WordFrequencySorted.py ./datasets/Book.txt
```

calculate the total spending amount and then sort the output by the calculated amount.
```python
python CustomerOrder.py ./datasets/customer-orders.csv
```

combiner: this code illustrates the usage of combiner, which is run on the same machie before they date is sent out to other machines for reduction. This technique helps
reduce the amount of data travelling among machines. One thing to notice is that the combiner should not do anything that the reducer doesn't do because the combiner might be
not called at one, depending on the setup of the Hadoop. 
```python
python WordFrequencyCbn.py ./datasets/Book.txt
``` 