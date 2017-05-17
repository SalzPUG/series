#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from series import series, sum_diff


def test_series():
    pass

    
def test_list_with_one_element():
    assert_equals(series([1]),[[1]]) 


def test_list_with_two_elements():
    assert_equals(series([1, 2]),[[1, 2]])


def test_non_monotonic_list_with_two_elements():
    assert_equals(series([2, 1]),[[2], [1]])


def test_non_monotonic_list_with_three_elements():
    assert_equals(series([2, 1, 0]),[[2], [1], [0]])
 
def test_non_monotonic_list_interleaved():
    assert_equals(series([1, 5000, 2, 5001]), [[1, 2], [5000, 5001]])
    
def test_sum_differences():
    assert_equals(sum_diff([1, 2, 3]), 2)
    
#def test_non_monotonic_list_interleaved():
#    assert_equals(series([1, 3, 2, 4]), [[1, 2], [3, 4]])
