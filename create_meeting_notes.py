from string import Template
from datetime import datetime as dt
import argparse
import typer
from typing import List, Optional

people= {
    'MA': 'Michael Aye',
    'JC': 'Joshua Colwell',
    'GH': 'Greg Holsclaw',
    'JE': 'Josh Elliot',
    'TB': 'Todd Bradley',
    'BW': 'Bob West'
}

calib_template= Template("""
# UVIS Calib meeting

Date: $date

## Participants
* Michael Aye (MA)
* $name1 ($id1)
* $name2 ($id2)
* $name3 ($id3)
* $name4 ($id4)

## Action items from last meeting
* [ ]
* [ ]
* [ ]

## Agenda

*
*
*

## AOB

## New Action Items

*
*

"""
)

def main(ids: Optional[List[str]] = typer.Option(None)):

    # Get the current date
    date = dt.now().strftime("%Y-%m-%d")

    d = {
        'date': date,
    }

    for i, id in enumerate(ids):
        d['name{}'.format(i+1)] = people[id]
        d['id{}'.format(i+1)] = id        

    s = calib_template.safe_substitute(d)
    print(s)

if __name__ == "__main__":
    typer.run(main)