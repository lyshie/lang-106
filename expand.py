#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import xlrd


def main():
    wb = xlrd.open_workbook("優勝錄取人數統計表.xls")
    sh = wb.sheet_by_index(0)
    for rx in xrange(1, sh.nrows - 1):
        cat = sh.cell(rx, 0).value
        for cx in xrange(1, sh.ncols - 1):
            n = 0
            if sh.cell(rx, cx).value:
                n = int(sh.cell(rx,  cx).value)
            if (n > 0):
                degree = re.sub(r'[\n\r\s]', '', sh.cell(0, cx).value)
                for i in xrange(1, n + 1):
                    desc = u"%s\t%s\t%d" % (cat, degree, i)
                    print(desc.encode("UTF-8"))


if __name__ == '__main__':
    main()
