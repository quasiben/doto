'''
doto - (http://github.com/quasiben/doto)


doto command line utility

'''

from argparse import ArgumentParser
from doto.commands import sub_commands

def main(args=None, exit=True):
    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(help='commands')

    for command in sub_commands():
        command.add_parser(subparsers)

    args = parser.parse_args(args)

    try:
        return args.main(args)

    except:
        print 'there was an error'

        args.sub_parser.print_help()

        if exit:
            raise SystemExit(1)
        else:
            return 1

if __name__ == '__main__':
    main()
