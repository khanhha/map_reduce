from mrjob.job import MRJob
from mrjob.step import MRStep

class MostLovedFriends(MRJob):

    def configure_args(self):
        super(MostLovedFriends,self).configure_args()
        self.add_file_arg('--names', help="path to friend names: Marvel-names.txt")

    def steps(self):
        return [
            MRStep(mapper=self.mapper_num_friends, reducer=self.reducer_sum_friends),
            MRStep(mapper_init = self.load_friends_name_dict, mapper=self.mapper_init_sorting, reducer=self.reducer_most_loved_friends)
        ]

    # counter the number of friend of each person
    # 1 2 3 4 9 10 7: this line describe the freinds of the person ID 1
    def mapper_num_friends(self, _, line):
        ids = line.split()
        main_id = ids[0]
        n_friends = len(ids)-1
        yield int(main_id), int(n_friends)

    def reducer_sum_friends(self, key, values):
        yield key, sum(values)

    def load_friends_name_dict(self):
        self.names = {}
        with open("Marvel-Names.txt", encoding='ascii', errors='ignore') as file:
            for l in file:
                fields = l.split('"')
                id = int(fields[0])
                self.names[id] = fields[1]

    def mapper_init_sorting(self, id, friends):
        yield None, (friends, self.names[id])

    def reducer_most_loved_friends(self, key, value):
        yield max(value)


if __name__ == '__main__':
    MostLovedFriends().run()