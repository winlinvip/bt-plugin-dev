#!/usr/bin/python
# coding: utf-8

import os, public

_title = '检查是否存在危险远程访问文件'
_version = 1.0  # 版本
_ps = "检查是否存在危险远程访问文件hosts.equiv、.rhosts、.netrc"  # 描述
_level = 2  # 风险级别： 1.提示(低)  2.警告(中)  3.危险(高)
_date = '2023-03-09'  # 最后更新时间
_ignore = os.path.exists("data/warning/ignore/sw_risk_file.pl")
_tips = [
    "删除在家目录下的.rhosts和.netrc文件以及删除根目录下的hosts.equiv文件",
    "按照提示找到风险文件并删除"
]
_help = ''


def check_run():
    '''
        @name 开始检测
        @return tuple (status<bool>,msg<string>)
    '''
    result_list = []
    cfile = ['hosts.equiv', '.rhosts', '.netrc']
    for cf in cfile:
        file = public.ExecShell('find /home -maxdepth 2 -name {}'.format(cf))
        if file[0]:
            result_list = result_list+file[0].split('\n')
    result = '、'.join(reform_list(result_list))
    if result:
        return False, '存在高风险文件，尽快删除以下文件\"{}\"'.format(result)
    else:
        return True, '无风险'


def reform_list(check_list):
    """处理列表里的空字符串"""
    return [i for i in check_list if (i is not None) and (str(i).strip() != '')]

