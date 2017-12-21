# -*- coding: utf-8 -*-
import read_line as rl
import coordinate as cdi

data_dict = rl.read_line("yk-G.txt") #读取数据
file_wt = open('yk_G_move.txt', 'w')
thea = 39.4
distance = 38.3
for linename, data in data_dict.items():
    if 'L' in linename or 'l' in linename:
        thea = 39.4
    elif 'Z' in linename or 'z' in linename:
        thea = 90.0
    else:
        print "Line name is wrong: linename:%s" %linename

    if data[0 , 0] < data[1 , 0]:
        distance = 38.3
    elif data[0 , 0] > data[1 , 0]:
        distance = -38.3
    else:
        print "distance name is wrong"

    movedata = cdi.move_coordinate(data, distance, thea)
    for i in range(0, len(movedata)):
        wline = linename + ',' + str(i + 1) + ',' + str(movedata[i , 0])+ ','  + str(movedata[i , 1]) + '\n'
        file_wt.writelines(wline)

file_wt.close()
