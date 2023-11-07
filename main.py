import argparse

from src.generators.PayloadGenerator import PayloadGenerator
from src.utils.payload_args import parse_payload_args

parser = argparse.ArgumentParser(description='Streamlines the process of hijacking DLL\'s with configurable payloads.')
parser.add_argument('target', help='the target DLL you want to proxy to')
parser.add_argument('-p', '--payload', help='the name of the payload to use', required=True)
parser.add_argument('-a', '--args', help='the arguments for the payload to use e.g ip=127.0.0.1,port=4444')


def main():
    args = parser.parse_args()
    payload_args = parse_payload_args(args.args)
    PayloadGenerator.generate_payload(args.payload, args.target, payload_args)


if __name__ == '__main__':
    main()
