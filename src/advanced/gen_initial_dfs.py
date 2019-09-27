import sys

if __name__ == '__main__':
    print('start creating BFS for the person with ID =  ', sys.argv[1])
    with open("BFS-iter-0.txt", 'w') as fout:
        with open('../../datasets/Marvel-Graph.txt') as file:
            for line in file:
                fields = line.split()
                id = fields[0]
                nfriends = len(fields) - 1
                friends = fields[-nfriends:]
                color = 'WHITE'
                distance = 999999
                if id == sys.argv[1]:
                    color = 'GRAY'
                    distance = 0
                if id != '':
                    friends = ','.join(friends)
                    out_line = '|'.join((id, friends, str(distance), color))
                    fout.write(out_line)
                    fout.write('\n')
