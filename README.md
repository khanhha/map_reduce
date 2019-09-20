 This reposritory holds my learning experiments with MapReducer
 
# install requirements
pip install mrjob
 
# run examples

- calculate average number of friends by age
```python
python FriendsByAge.py ./datasets/fakefriends.csv
```

- calculate min temperature thorugh out the year by location
```python
python MinTemperature.py ./datasets/1800.csv
```

- count word frequencies using regular expression
```python
python WordFrequency.py ./datasets/Book.txt
```
- demonstrate a map reduce pipeline of two stages that first, count the occurency of words and then order unique words by their popularity.
```python
python WordFrequencySorted.py ./datasets/Book.txt
```