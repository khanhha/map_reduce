from mrjob.job import MRJob
from mrjob.step import MRStep

class MostRatedMovie(MRJob):

    def configure_args(self):
        super(MostRatedMovie, self).configure_args()
        self.add_file_arg('--items', help='file path of u.item')

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings, reducer_init=self.reducer_init, reducer=self.reducer_count_ratings),
            MRStep(mapper=self.mapper_get_through, reducer=self.reducer_max_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        (uid, mid, rating, timestamp) = line.split('\t')
        yield mid, 1

    def mapper_get_through(self, key, value):
        yield key, value

    def reducer_init(self):
        self.movieNames = {}
        with open('u.item', encoding='ascii', errors='ignore') as f:
            for line in f:
                fields = line.split('|')
                self.movieNames[fields[0]] = fields[1]

    def reducer_count_ratings(self, key, values):
        yield None, (sum(values), self.movieNames[key])

    def reducer_max_ratings(self, key, values):
        yield max(values)

if __name__ == '__main__':
    MostRatedMovie.run()
