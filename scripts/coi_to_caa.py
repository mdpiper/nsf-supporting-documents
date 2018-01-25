#! /usr/bin/env python
from __future__ import print_function

import os
import argparse
import csv

_TEMPLATE = """
# Collaborators and Other Affiliations #

## Mark Piper ##

*Institute of Arctic and Alpine Research*  
*University of Colorado Boulder*

### Collaborators and Co-Editors ({number_of_collaborators}) ###

{collaborators}

### Graduate Advisors ({number_of_advisors}) ###

{advisors}

### PhD Advisor ({number_of_sponsors}) ###

{sponsors}
""".strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'),
                        help='CSV-file of conflicts')
    parser.add_argument('--output',
                        type=argparse.FileType('w'),
                        help='Output markdown file')
    
    args = parser.parse_args()

    reader = csv.reader(args.file, delimiter=';')

    collaborators = []
    advisors = []
    sponsors = []
    for row in reader:
        name, institute, ctype = (row[2].strip(), row[3].strip(),
                                  row[4].strip())
        if ctype == 'Collaborator':
            collaborators.append("1. {name} ({institute})".format(
                name=name, institute=institute))
        elif row[-1].strip() == 'Advisor':
            advisors.append("1. {name} ({institute})".format(
                name=name, institute=institute))
        elif row[-1].strip() == 'ThesisAdvisor':
            sponsors.append("1. {name} ({institute})".format(
                name=name, institute=institute))
        else:
            warnings.warn(
                '{type}: conflict type not understood'.format(type=ctype))

    print(_TEMPLATE.format(collaborators=os.linesep.join(collaborators),
                           number_of_collaborators=len(collaborators),
                           advisors=os.linesep.join(advisors),
                           number_of_advisors=len(advisors),
                           sponsors=os.linesep.join(sponsors),
                           number_of_sponsors=len(sponsors)),
         file=args.output)


if __name__ == '__main__':
    main()
