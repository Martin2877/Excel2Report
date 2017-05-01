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


def read_excel(xls_read):
    txt_wirte = 'output.txt'
    # 打开文件
    workbook = xlrd.open_workbook(xls_read, encoding_override="utf-8")
    sheet_count = len(workbook.sheets())  # sheet数量
    risk_form = []
    f = open(txt_wirte, 'w')
    for s_index in range(0, sheet_count):
        # every sheet
        risk_sys = [0, 0, 0]  # high, medium, low
        sheet = workbook.sheet_by_index(s_index)
        print 'sheetname:', sheet.name, 'rows:', sheet.nrows, 'cols:', sheet.ncols
        # system name
        putvalue = sheet.cell(2 - 1, 2 - 1).value
        f.write("\r\r\r\r" + putvalue + '\r')
        print putvalue
        # risk_sys[0] = putvalue
        # every row
        i = 2
        while i <= sheet.nrows:
            seq = [(i, 5), (i, 6), (i, 7), (i, 8), (i, 9), (i, 10)]
            for x, y in seq:
                # print x, y
                head_name = sheet.cell(0, y - 1).value.strip()
                f.write(head_name + ':')
                print head_name
                putvalue = sheet.cell(x - 1, y - 1).value.strip()
                f.write(putvalue + '\r')
                print putvalue
                # count
                if y - 1 == 6:
                    if putvalue == "高":
                        risk_sys[0] += 1
                    elif putvalue == "中":
                        risk_sys[1] += 1
                    elif putvalue == "低":
                        risk_sys[2] += 1
            i += 1
        risk_form.append(risk_sys)
    print risk_form
    # f.write("风险统计信息："+ risk_form)
    f.close()


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
    wbk_new = xlwt.Workbook()
    # copy the sheet name
    sheet_name = wbk_read.sheet_names()[0]
    wbk_new_sheet_add = wbk_new.add_sheet(sheet_name, cell_overwrite_ok=True)
    # read the first sheet
    sheet = wbk_read.sheet_by_index(0)  # sheet索引从0开始
    # init
    risk_sys = [0, 0, 0, 0, 0]  # Critical, High, Medium, Low, None
    risk_form = []
    # sheet的名称，行数，列数
    print (sheet.name, sheet.nrows, sheet.ncols)
    # every row
    i = 3
    while i <= sheet.nrows:
        seq_read = [(i, 1), (i, 2), (i, 3), (i, 4), (i, 5), (i, 6)]
        seq_write = [(i, 1), (i, 2), (i, 3), (i, 4), (i, 5), (i, 6)]
        for x, y, wx, wy in [(x, y, wx, wy) for x, y in seq_read for wx, wy in seq_write]:
            print x, y, wx, wy
            putvalue = sheet.cell(x - 1, y - 1).value.strip()
            wbk_new_sheet_add.write(wx - 1, wy - 1, sheet.cell(x - 1, y - 1).value)
            print putvalue
            # count
            if y - 1 == 6:
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
        i += 1
        risk_form.append(risk_sys)
    print risk_form

    # save the new workbook
    wbk_new.save(output)
    wbk_read.close()


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
        output = 'output.xlsx'
    translation(input, output)


if __name__ == '__main__':
    main()
