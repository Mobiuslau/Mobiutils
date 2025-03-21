import logging
import argparse


def get_clas(arg=None):
    """return: Argparse class.
    """
    desc   = 'Mobiutils Byte Unit Calculator.'
    parser = argparse.ArgumentParser(prog='mubpc.py', description=desc, epilog='')
    parser.add_argument('inNum', type=float, help='float: input number.')
    parser.add_argument('unitFrom', type=str, help='str: Convert from unit.')
    parser.add_argument('unitTo', type=str, help='str: Convert to unit.')
    return parser.parse_args(arg)


def main(args):
    calculated_num_to = binary_prefix_calculator(args.inNum, args.unitFrom, args.unitTo)
    log.info(f'{args.inNum} {args.unitFrom} = {calculated_num_to} {args.unitTo}')


def binary_prefix_calculator(in_num, unit_from, unit_to):
    prefixes = {
        "": 1,
        "K": 10 ** (3 * 1),
        "M": 10 ** (3 * 2),
        "G": 10 ** (3 * 3),
        "T": 10 ** (3 * 4),
        "P": 10 ** (3 * 5),
        "E": 10 ** (3 * 6),
        "Z": 10 ** (3 * 7),
        "Y": 10 ** (3 * 8),
        "R": 10 ** (3 * 9),
        "Q": 10 ** (3 * 10),
        "Ki": 2 ** (10 * 1),
        "Mi": 2 ** (10 * 2),
        "Gi": 2 ** (10 * 3),
        "Ti": 2 ** (10 * 4),
        "Pi": 2 ** (10 * 5),
        "Ei": 2 ** (10 * 6),
        "Zi": 2 ** (10 * 7),
        "Yi": 2 ** (10 * 8),
        "Ri": 2 ** (10 * 9),
        "Qi": 2 ** (10 * 10)
    }
    suffixes = {
        "B": 8,
        "b": 1
    }
    try:
        unit_bits_from = prefixes[args.unitFrom.split(unit_from[-1])[0]] * suffixes[unit_from[-1]]
    except KeyError:
        log.error(f'unitFrom {unit_from} not a proper unit.')
        exit()
    try:
        unit_bits_to   = prefixes[args.unitTo.split(unit_to[-1])[0]] * suffixes[unit_to[-1]]
    except KeyError:
        log.error(f'unitTo {unit_to} not a proper unit.')
        exit()
    calculated_num_to = in_num * unit_bits_from / unit_bits_to
    return calculated_num_to


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s]: %(message)s')  # filename='main.log'
    log = logging.getLogger(__name__)
    try:
        args = get_clas()
        main(args)
    except Exception as e:
        log.exception(e)
