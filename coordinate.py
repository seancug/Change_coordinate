# -*- coding: utf-8 -*-
import numpy as np

def move_coordinate(data, distance, thea):
    """
    :param linename: 线名
    :param data: 数据
    :distance: 距离
    :thea: 角度
    :return: 结果
    """
    data[:, 0] = data[:, 0] + distance * np.sin(np.pi / 180.0 * thea)
    data[:, 1] = data[:, 1] + distance * np.cos(np.pi / 180.0 * thea)

    return data



