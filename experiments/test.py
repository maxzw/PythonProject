import os
import context
from time import sleep
from functions.logbook import Logbook
from argparse import ArgumentParser

# set this directory as working directory
os.chdir(os.path.dirname(__file__))

# arguments
parser = ArgumentParser()
parser.add_argument('-p',
                dest='path',
                help='which path to log to',
                default='project1/experiments/logs/testf.txt', type=str)
args = parser.parse_args()


def main():
    output_path = args.path
    
    lb = Logbook(output_path, incl_time=True)
    
    for i in range(10):
        lb.log(str(f"This is the number {i}"))
        sleep(1)

if __name__ == '__main__':
    main()