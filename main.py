from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog='sample', description='sample')
    parser.add_argument('--foo', help='foo help', required=True)

    args = parser.parse_args()
    print(args.foo)


if __name__ == '__main__':
    main()

