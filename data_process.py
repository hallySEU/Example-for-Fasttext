# -*- coding: utf-8 -*-
"""
 Filename @ data_process.py
 Author @ huangjunheng
 Create date @ 2018-06-10 11:24:29
 Description @
"""


def file2array(filename):
    """
    :param filename: 文件名
    :return: ret_array: 
    """
    ret_array = []
    fr = open(filename)
    for line in fr:
        line = line.rstrip("\n")
        ret_array.append(line)

    fr.close()
    return ret_array


def get_model_input_by_data(data_file):
    """
    :param data_file: 
    :return: 
    """
    eval_model = True
    ret_labels = []
    ret_contents = []
    data_array = file2array(data_file)
    if len(data_array) > 0 and '__label__' not in data_array[0]:
        eval_model = False

    for line in data_array:
        if eval_model is True:
            split_datas = line.split('\t__label__')
            label = '__label__' + split_datas[1]
            content = split_datas[0]
            ret_labels.append(label)
        else:
            content = line

        ret_contents.append(content)

    return ret_contents, ret_labels