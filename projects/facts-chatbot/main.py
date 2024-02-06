from src.db.db import db
from os.path import exists

def main():
    # Evitando a criação de outro Vector Store.
    if exists('data/'):
        print('hey')
    else:
        db()
        print('ho')

if __name__ == '__main__':
    main()