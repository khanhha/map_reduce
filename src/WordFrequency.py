from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+")
class WordFrequency(MRJob):
    def mapper(self, key, line):
        #words = line.findall(WORD_REGEXP)
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w.lower(), 1

    def reducer(self, word, occurences):
        #print(occurences)
        yield word, sum(occurences)

if __name__ == '__main__':
    WordFrequency.run()
