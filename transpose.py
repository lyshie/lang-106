#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv

items = dict()


def main():
    for i in range(ord('A'), ord('J')):
        items[chr(i)] = list()

    with open('座位編號_20171031.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            area = row['座位區域']
            rs = re.search(r'(\d+)排(\d+)號', row['座位全名'])
            xx, yy = rs.group(2), rs.group(1)
            xx = 8 - int(xx)
            yy = int(yy) - 1
            name = row['全名'].replace("（", "\r\n（").replace("）", "）\r\n")
            items[area].append({'x': xx, 'y': yy, 'name': name})

    for i in range(ord('A'), ord('J')):
        w, h = 8, 10
        table = [["" for x in range(w)] for y in range(h)]

        for item in items[chr(i)]:
            table[item['y']][item['x']] = item['name']

        with open('{}.csv'.format(chr(i)), "wb") as output:
            writer = csv.writer(output)
            for item in table:
                writer.writerow(item)


if __name__ == '__main__':
    main()
