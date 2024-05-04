from g2p import make_g2p

import sys

transducer = make_g2p('hun', 'hun-ipa')

if __name__ == "__main__":
    print(transducer(sys.argv[1]).output_string)