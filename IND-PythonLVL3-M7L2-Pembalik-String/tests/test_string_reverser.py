# test_string_reverser.py

import pytest
from reverse_string.string_reverser import reverse_string

# Pengujian fungsi reverse_string dengan string normal
def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh", "String 'hello' diharapkan dibalik menjadi 'olleh'"

# Pengujian fungsi reverse_string dengan string yang mengandung spasi
def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh", "String 'hello world' diharapkan dibalik menjadi 'dlrow olleh'"

# Pengujian fungsi reverse_string dengan string kosong untuk memastikan tidak ada error
def test_reverse_string_empty():
    assert reverse_string("") == "", "String kosong diharapkan tetap menjadi string kosong"
