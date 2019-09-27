from mrjob.job import MRJob
from mrjob.step import MRStep

class MostRatedMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings, reducer=self.reducer_count_ratings),
            MRStep(mapper=self.mapper_get_through, reducer=self.reducer_max_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        (uid, mid, rating, timestamp) = line.split('\t')
        yield mid, 1

    def mapper_get_through(self, key, value):
        yield key, value

    def reducer_count_ratings(self, key, values):
        yield None, (sum(values), key)

    def reducer_max_ratings(self, key, values):
        yield max(values)

if __name__ == '__main__':
    MostRatedMovie.run()
