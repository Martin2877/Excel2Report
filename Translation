#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re
import xlrd
import xlwt
import optparse

reload(sys)
sys.setdefaultencoding('utf-8')


def getfile(cur_path):
    list_dirs = os.walk(cur_path)
    for root, dirs, files in list_dirs:
        for d in dirs:
            # print os.path.join(root, d)
            pass
        for f in files:
            print os.path.join(root, f)
            # grep_getusername(os.path.join(root, f))
            grep_getdotword(os.path.join(root, f))


def translation(input, output, tfile="Translation.xlsx"):
    print input
    input = cur_file_dir() + "/" + input
    output = cur_file_dir() + "/" + output
    tfile = cur_file_dir() + "/" + tfile
    # 打开文件
    wbk_read = xlrd.open_workbook(input, encoding_override="utf-8")
    tfile_read = xlrd.open_workbook(tfile, encoding_override="utf-8")
    print "open successed"
    wbk_new = xlwt.Workbook()
    # copy the sheet name
    sheet_name = wbk_read.sheet_names()[0]
    wbk_new_sheet_add = wbk_new.add_sheet(sheet_name, cell_overwrite_ok=True)
    # read the first sheet
    sheet = wbk_read.sheet_by_index(0)  # sheet索引从0开始
    t_sheet = tfile_read.sheet_by_index(0)  # sheet索引从0开始
    # init
    risk_sys = [0, 0, 0, 0, 0]  # Critical, High, Medium, Low, None
    risk_form = []
    # sheet的名称，行数，列数
    print ('sheet name:', sheet.name, "nrows:", sheet.nrows, "ncols", sheet.ncols)
    # every row
    row = 2
    while row <= sheet.nrows:
        # this seq is for base exchange
        seq = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
        # pb->position before , pa -> position after
        for pb, pa in seq:
            x = row - 1
            y = pb - 1
            print "x:", x, "y:", y
            putvalue = sheet.cell(x, y).value
            wbk_new_sheet_add.write(x, pa - 1, putvalue)
            print putvalue
            # count
            if y == 6:
                if putvalue == "Critical":
                    risk_sys[0] += 1
                elif putvalue == "High":
                    risk_sys[1] += 1
                elif putvalue == "Medium":
                    risk_sys[2] += 1
                elif putvalue == "Low":
                    risk_sys[3] += 1
                elif putvalue == "None":
                    risk_sys[4] += 1
        print 'Translating'
        # this seq is (position of Translation.xls,position for exchange of output.xls)
        t_seq = [(3, 4), (4, 5), (5, 7), (6, 8), (8, 9)]
        # find the row
        print "name:",sheet.cell(row - 1, 3).value
        for t_row in range(t_sheet.nrows):
            if t_sheet.cell(t_row - 1, 1).value == sheet.cell(row - 1, 3).value:
                print "Find!"
                # Exchange the value
                for tpb, tpa in t_seq:
                    x = row - 1
                    y = tpa - 1
                    putvalue = t_sheet.cell(t_row-1, tpb-1).value
                    wbk_new_sheet_add.write(x, y, putvalue)
                    print "t_row:", t_row, "x:", x, "y:", y, putvalue
                break
        print 'Translated'
        row += 1
        risk_form.append(risk_sys)
    print risk_form
    # save the new workbook
    wbk_new.save(output)


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def main():
    parser = optparse.OptionParser('[-] Usage %prog ' + '-f <Input File> [-o <Output File>]')
    parser.add_option('-f', dest='input', type='string', help='specify the target file')
    parser.add_option('-o', dest='output', type='string', help='specify the output file')

    (options, args) = parser.parse_args()

    if options.input == None:
        print parser.usage
        exit(0)

    input = options.input
    output = options.output
    if output is None:
        output = 'output.xls'
    translation(input, output)


if __name__ == '__main__':
    main()
