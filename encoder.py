#!/usr/bin/python3
# -*- coding: utf-8 -*-
# by Orik:3
from itertools import cycle

key = 'SoftServe'


def form_dict():  # формуємо словник з букв
    return dict([(i, chr(i)) for i in range(128)])


def comparator(value, key):
    return dict([(idx, [ch[0], ch[1]])
                 for idx, ch in enumerate(zip(value, cycle(key)))])


def encode_val(word):
    d = form_dict()
    return [k for c in word for k, v in d.items() if v == c]


def full_encode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] + v[1]) % l for v in d.values()]


def decode_val(list_in):
    l = len(list_in)
    d = form_dict()
    return [d[i] for i in list_in if i in d]


def full_decode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] - v[1]) % l for v in d.values()]
