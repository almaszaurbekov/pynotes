#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyNotes.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    # import sqlite3

    # conn = sqlite3.connect("db.sqlite3") # или :memory: чтобы сохранить в RAM
    # cursor = conn.cursor()

    # cursor.execute('SELECT * FROM notes_category')

    # print(cursor.fetchall())

    # cursor.execute('DELETE FROM notes_category')

    # cursor.execute('SELECT * FROM notes_category')

    # conn.commit();

    # print(cursor.fetchall())