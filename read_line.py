# -*- coding: utf-8 -*-
import numpy as np

def read_line(filename):
    '''
    :param filename:文件名
    :return:测线数据
    '''
    file_fp = open(filename, 'r')
    all_data = file_fp.readlines()

    all_lines = dict()

    for i in range(0,len(all_data)):
        oneline = all_data[i]
        line = oneline.split()
        linedata = [float(line[2]), float(line[3])]

        if line[0] in all_lines.keys():
            all_lines[line[0]] = np.row_stack((all_lines[line[0]], linedata))
        else:
            all_lines[line[0]] = np.array(linedata)

    return all_lines



