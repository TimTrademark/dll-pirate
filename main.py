import argparse
from src.utils.gen_dll import gen_def,read_template_content

parser = argparse.ArgumentParser(description='Streamlines the process of hijacking DLL\'s with configurable payloads.')
parser.add_argument('target', help='the target DLL you want to proxy to')
parser.add_argument('-p','--payload', help='the name of the payload to use')


def main():
    args = parser.parse_args()
    dll_def = gen_def(args.target)
    def_filename = args.target + ".def"
    with open(def_filename, 'w', encoding='utf-8') as f:
        f.write(dll_def)
    #TODO: compile template and link with compiled assembly


if __name__ == '__main__':
    main()
