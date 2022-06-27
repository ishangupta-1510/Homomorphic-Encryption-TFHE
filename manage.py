#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from test import *
import textutils
from textutils import views
def main():
    # print("fsdijsoijfsdi")
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'textutils.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # val1 = views.valone()
    # val2 = views.valtwo()
    # print(val1)
    # print(val2)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
