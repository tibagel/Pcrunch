import itertools
import argparse
import sys



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--minc', type=str, default=1,help='minimum lenght')
    parser.add_argument('--maxc', type=str, default=1, help='maximum lenght')
    parser.add_argument('--char', type=str, default='ABCabc123', help='character to crunch in the file')
    args = parser.parse_args()
    sys.stdout.write(str(write_file(args)))

def write_file(args):
    f = open('output.txt','a+')
    for n in range(int(args.minc),int(args.maxc) + 1):
        for xs in itertools.product(args.char, repeat=n):
            output = ''.join(xs)
            f.write('{} \n'.format(output))
            print(output)
    f.close()

if __name__ == '__main__':
    main()