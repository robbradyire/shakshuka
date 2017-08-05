# shakshuka
A website for recipes

## Requirements/Dependencies

- Python 3.5
- Python virtualenv
- sqlite 3.11
- File `~/.sqliterc ` containing `PRAGMA foreign_keys = ON;`

## Installation

1.  Clone the repo
2. `cd shakshuka/backend`
3. `virtualenv venv` - Create virtual environment
4. `source venv/bin/activate` - Activate virtual environment
5. `pip install -r requirements.txt` - Install python dependencies

## Run Things

Source files located in `shakshuka/backend/recipes`, can be run from `backend` using `python path/to/file`.
Tests located in `shakshuka/backend/tests`, can be run from `backend` using `python -m unittest discover`.

All developed and tested on Ubuntu 16.04, it might work on other distros/OSes but who knows...
