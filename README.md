 This reposritory holds my learning experiments with MapReducer
 
# install requirements
pip install mrjob
 
# more advanced experiments
__Find the most rated movie__: this example runs two mapreduce steps. the first one calculate the number of rating per movieID.
the second one first map MOVIEID to MOVIENAME and the find the movie with the maximum rating.
```python
python most_rated_movie.py --items=../../datasets/ml-100k/u.item ../../datasets/ml-100k/u.data
```

__Find the most loved friends__: this example find the friend who has the largest size of social network. It first loads the friends graph
and count the the number of friends per person. In the second mapreduce stage, it maps the peopleID to names and then output the person with the maximum number of friends
```python
python most_loved_friends.py --names=../../datastes/Marvel-Names.txt ../../datasets/Marvel-Graph.txt
```

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