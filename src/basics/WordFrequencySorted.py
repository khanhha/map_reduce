from mrjob.job import MRJob
from mrjob.job import MRStep
import re

WORD_REGEXP = re.compile(r"[\w']+")
class WordFrequencySorted(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                    reducer=self.reducer_count_words),
            MRStep(mapper=self.mapper_make_counts_key,
                   reducer=self.reducer_output_words)
        ]

    def mapper_get_words(self, _, line):
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w.lower(), 1

    def reducer_count_words(self, word, occurences):
        #print(occurences)
        yield word, sum(occurences)

    def mapper_make_counts_key(self, word, count):
        yield '%04d'%int(count), word

    def reducer_output_words(self, count, words):
        for word in words:
            yield count, word

if __name__ == '__main__':
    WordFrequencySorted.run()
