from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol

class Vertex:
    def __init__(self):
        self.id = ''
        self.edges = ''
        self.dst = 9999
        self.state = 'WHITE'

    def from_string(self, value):
        fields = value.split('|')
        if (len(fields) == 4):
            self.id = fields[0]
            self.edges = fields[1].split(',')
            self.dst = int(fields[2])
            self.state = fields[3]

    def to_string(self):
        edges = ','.join(self.edges)
        return '|'.join((self.id, edges, str(self.dst), self.state))

class DosBfs(MRJob):
    INPUT_PROTOCOL = RawValueProtocol
    OUTPUT_PROTOCOL = RawValueProtocol

    def configure_args(self):
        super(DosBfs, self).configure_args()
        self.add_file_arg('--dest', help='person destiation ID')

    def mapper(self, _, line):
        vert = Vertex()
        vert.from_string(line)
        if vert.state == 'GRAY':
            for e in vert.edges:
                ve = Vertex()
                ve.id = e
                ve.dst = int(vert.dst) + 1
                ve.state = 'GRAY'
                if self.options.dest == e:
                    counter_name = "destiantion ID " + e + " was reached through steps: " + str(ve.dst)
                    self.increment_counter("DOS", counter_name, 1)
                yield ve.id, ve.to_string()
            vert.state = 'BLACK'

        yield vert.id, vert.to_string()

    def reducer(self, key, values):
        edges = []
        dst = 99999
        state = 'WHITE'
        for val in values:
            v = Vertex()
            v.from_string(val)
            if len(v.edges) > 0:
                edges.extend(v.edges)

            if v.dst < dst:
                dst = v.dst
            if v.state == 'BLACK':
                state = 'BLACK'
            if v.state == 'GRAY' and state == 'WHITE':
                state = 'GRAY'

        v = Vertex()
        v.id = key
        v.dst = dst
        v.state = state
        yield key, v.to_string()

if __name__ == '__main__':
    DosBfs().run()