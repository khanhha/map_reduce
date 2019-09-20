from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+")

class WordFrequencyCbn(MRJob):
    def mapper(self, key, line):
        #words = line.findall(WORD_REGEXP)
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w.lower(), 1

    def combiner(self, word, occrences):
        yield word, sum(occrences)

    def reducer(self, word, occurences):
        #print(occurences)
        yield word, sum(occurences)

if __name__ == '__main__':
    WordFrequencyCbn.run()
