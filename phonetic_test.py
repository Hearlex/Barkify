from g2p.cli import update
from g2p import make_g2p

import sys

#update()

transducer = make_g2p('hun', 'hun-ipa')

if __name__ == "__main__":
    print(transducer(sys.argv[1]).output_string)