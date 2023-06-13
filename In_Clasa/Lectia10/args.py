import argparse

def create_args():
    parser = argparse.ArgumentParser(
        prog='BTC calculator',
        description='Un program care acumuleaza date despre pret',
    )
    parser.add_argument(
        '-f',
        '--flow',
        type=str,
        choices=['harvest', 'exchange'],
        help='Alege ce vrei sa faci',
        required=True
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=60,
        help='timeout pentru refresh la date'
    )
    parser.add_argument(
        '--target',
        type=str,
        choices=['USD', 'BTC'],
        help='Converteste USD in BTC invers la pret curent'
    )
    parser.add_argument(
        '--amount',
        type=float,
        help='Cantitatea de BTC sau USD pe care o convertim'
    )
    return parser.parse_args()