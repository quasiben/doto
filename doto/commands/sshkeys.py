'''
List all sshkeys
'''

from doto import connect_d0

def main(args):
    d0 = connect_d0()
    print d0.get_all_ssh_keys(table=True)

def add_parser(subparsers):
    parser = subparsers.add_parser('sshkeys',
                                      help='list all sshkeys',
                                      description=__doc__)
    # parser.add_argument('--create', nargs=2, action='append', default=[], help='sets a new variable: name value', metavar=('name', 'value'))
    parser.add_argument('--create', help='create and upload ssh keys to digital ocean')
    parser.set_defaults(main=main, sub_parser=parser)
