import logging
import argparse
import pyperclip


def get_clas(arg=None):
    """return: Argparse class.
    """
    desc   = 'Mobiutils Windows Valid File Name.'
    parser = argparse.ArgumentParser(prog='muwvfn.py', description=desc, epilog='')
    parser.add_argument('infilename', type=str, help='str: input filename.')
    parser.add_argument('-d', '--deplace', action='store_true', help='flag: Convert filename back.')
    parser.add_argument('-n', '--noclip', action='store_true', help='flag: Don\'t output to clipboard.')
    return parser.parse_args(arg)


def main(args):
    new_filename = windows_valid_file_name(args.infilename)
    log.info(f'{new_filename}')
    if not args.noclip:
        pyperclip.copy(new_filename)


def windows_valid_file_name(filename, char_table=None, deplace=False):
    if char_table is None:
        char_table = {
            "\"": "\'\'",
            "\\": "＼",
            "/": "／",
            ":": "：",
            "*": "＊",
            "?": "？",
            "<": "＜",
            ">": "＞",
            "|": "｜"
        }
    if deplace is True:
        char_table = {v: k for k, v in char_table.items()}
    for k, v in char_table.items():
        filename = filename.replace(k, v)
    return filename


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s]: %(message)s')  # filename='main.log'
    log = logging.getLogger(__name__)
    try:
        args = get_clas()
        main(args)
    except Exception as e:
        log.exception(e)
