from argparse import ArgumentParser

from context import Context
from process.generate_dump import Process


def define_args():
    parser = ArgumentParser()
    parser.add_argument('-env')

    return parser.parse_args()


if __name__ == '__main__':
    args = define_args()
    process = Process(Context.clone(args.env))
    process.exec_dump()
    print(process.dump)

