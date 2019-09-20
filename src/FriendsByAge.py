from mrjob.job import MRJob

class FriendsByAge(MRJob):
    def mapper(self, _, line):
        (ID, name, age, numFriends) = line.split(',')
        yield age, float(numFriends)

    def reducer(self, age, numFriends):
        total = 0.0
        n = 0
        for f in numFriends:
            total += f
            n += 1
        avg = total/n
        yield age, avg

if __name__ == '__main__':
    FriendsByAge().run()