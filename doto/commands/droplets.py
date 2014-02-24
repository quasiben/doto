'''
List all Droplets
'''

from doto import connect_d0

def main(args):
    d0 = connect_d0()
    print d0.get_all_droplets(table=True)

def add_parser(subparsers):
    parser = subparsers.add_parser('droplets',
                                      help='list all droplets',
                                      description=__doc__)

    parser.set_defaults(main=main, sub_parser=parser)
