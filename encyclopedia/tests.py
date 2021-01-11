from django.test import TestCase
from . import util

# Create your tests here.


def entry(request, entry):
    entry = util.get_entry(entry)
    print(entry)
