from mrjob.job import MRJob
from mrjob.step import MRStep

class CustomerOrder(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_customer_spend,
                   reducer=self.reducer_customer_spend),
            MRStep(mapper=self.mapper_customer_sort,
                   reducer=self.reducer_customer_sort)
        ]

    def mapper_customer_spend(self, _, line):
        (id, item, amount) = line.split(',')
        yield id, float(amount)

    def reducer_customer_spend(self, id, amounts):
        yield id, sum(amounts)

    def mapper_customer_sort(self, id, total):
        yield '%04.01f'%float(total), id

    def reducer_customer_sort(self, total, ids):
        for id in ids:
            yield id, total

if __name__ == '__main__':
    CustomerOrder().run()