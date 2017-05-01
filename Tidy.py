# -*-coding:utf-8-*-
import os
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

usernames = ""
username_dot = False
tidy_rton_file = "tidy_rton.txt"


def grep_url(file_name):
    f = open(cur_file_dir() + '/' + file_name, 'r')
    col1 = list()
    col2 = list()
    re_quo = re.compile(r'^.+(用户名)\s+(\w*)$')
    for line in f.readlines():
        line = line.strip()
        if re_quo.match(line):
            col1.append(re_quo.match(line).group(1))
            col2.append(re_quo.match(line).group(2))
    co_col = col1, col2
    f.close()
    return co_col


def tidy_line(ustring):
    global usernames
    global username_dot
    ustring = ustring.strip()
    # 1,"存在多个帐户"，把下面的帐户名的换行符换成、
    # 2，风险名称——> 去掉并在行未加（）
    # 3，去掉×
    # 4，去掉多空格
    flag1 = "================flag1======================"
    flag2 = "================flag2======================"
    # 1,"存在多个帐户"，把下面的帐户名的换行符换成、
    if "存在多个帐户" in ustring:
        username_dot = True
        usernames = ustring
        return ""
    if username_dot:
        if "问题描述:应严格限制默" in ustring:
            username_dot = False
            output_usernames = usernames
            usernames = ""
            print ustring
            return output_usernames + "\n" + ustring
        usernames += ustring + "、"
        print usernames
    # 2，风险名称——> 去掉并在行未加（）
    if '风险名称' in ustring:
        ustring = ustring.replace('风险名称:', '')
        ustring = ustring + '()'
    # 3，去掉×
    ustring = ustring.replace('×', '')
    # 4，去掉多空格（）
    if "密码" or "锁定" in ustring:
        ustring = ustring.replace('  ', '')
    return ustring


def rton(ustring):
    ustring = ustring.strip()
    ustring = ustring.replace('\r', '\n')
    return ustring


def tidy_rton(open_file):
    global tidy_rton_file
    # 因为UTF-8是用\n的，所以这里全部\r换成\n，不然这个txt里有\r和\n，但这里的读行是读\n的，所以很乱
    f_open = open(open_file, 'r')
    f_write = open(tidy_rton_file, 'w')
    for line in f_open.readlines():
        # line = tidy_line(line)
        line = rton(line)
        f_write.write(line + '\n')
    f_open.close()
    f_write.close()
    tidy()


def tidy():
    global tidy_rton_file
    f_open = open(tidy_rton_file, 'r')
    f_write = open('tidy.txt', 'w')
    for line in f_open.readlines():
        line = tidy_line(line)
        # line = rton(line)
        if username_dot:
            pass
        else:
            f_write.write(line + '\n')
    f_open.close()
    f_write.close()


def getfile(cur_path):
    list_dirs = os.walk(cur_path)
    for root, dirs, files in list_dirs:
        for d in dirs:
            # print os.path.join(root, d)
            pass
        for f in files:
            if f == get_selfname() or f == 'tidy.txt'or f == tidy_rton_file:
                pass
            else:
                findfile = os.path.join(root, f)
                print "now we tidy:", findfile.decode("GB2312")
                tidy_rton(findfile)


def get_selfname():
    re_quo = re.compile(r'^.+/(\w*).py$')
    script_name = re_quo.match(sys.argv[0]).group(1) + ".py"
    return script_name


if __name__ == '__main__':
    read_path = os.getcwd()
    getfile(read_path)  # get every file
    # eurl = grep_url(file)  # get every url
