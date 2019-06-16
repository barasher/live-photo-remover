import argparse
import logging
import sys
import os

LOG_FORMAT = '%(asctime)s [%(levelname)-5.5s] %(message)s'

JPG_EXT=".JPG"
MOV_EXT=".MOV"

RET_CODE_OK = 0
RET_CODE_ERROR = 2

def main():
    try:
        logging.basicConfig(format=LOG_FORMAT, stream=sys.stdout, level=20)
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', required=True, help='Source folder', metavar="folder")
        parser.add_argument('-d', action="store_true", help='Dry run (simulation)')
        args = parser.parse_args()

        for root, _, files in os.walk(args.f):
            for file in files:
                if file.endswith(JPG_EXT):
                    base, _ = os.path.splitext(file)
                    movFile = os.path.join(root, base + MOV_EXT)
                    if os.path.isfile(movFile):
                        if args.d:
                            logging.info('Should have deleted {}'.format(movFile))
                        else:
                            os.remove(movFile)

        return RET_CODE_OK
    except Exception as e:
        logging.error('Error: {}'.format(e))
        return RET_CODE_ERROR


if __name__ == '__main__':
    sys.exit(main())
