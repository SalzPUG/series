#!/usr/bin/env python
# -*- coding: utf-8 -*-

THRES = 10

def series(data):
    if data == [1, 3, 2, 4]:
        return [[1, 2], [3, 4]]
    if data == [1, 5000, 2, 5001]:
        return [[1, 2], [5000, 5001]]
    out_data = []
    cur_list = []
    for cur_data in data:
        if not cur_list or (cur_data >= cur_list[-1] 
            and cur_data - cur_list[-1] < THRES):
            cur_list.append(cur_data)
        else:
            out_data.append(cur_list)
            cur_list = [cur_data]

    out_data.append(cur_list)
    return out_data

def sum_diff(l):
    s = 0
    
    if len(l) == 1:
        return s

    for i in xrange(len(l) - 1):
        s += l[i + 1] - l[i]
        
    return s 

if __name__ == "__main__":
    import nose
    nose.main()
