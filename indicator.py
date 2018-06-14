#! coding:utf-8
"""
 Filename @ indicator.py
 Author @ huangjunheng
 Create date @ 2018-06-06 19:24:29
 Description @ calculate accuracy, precision and recall indicator
"""

import sys


def cal_precision_recall_F1(y=[], y_predict=[]):
    """
    计算准召
    :param y: label list
    :param y_predict: predict label list
    :return: 
    """
    TP, TN, FP, FN = 0, 0, 0, 0

    print >> sys.stderr, 'Test sample size: %d.' % len(y)
    print >> sys.stderr, 'Target sameple size: %d.' % sum(y)

    if len(y) != len(y_predict):
        print >> sys.stderr, 'Error: Length is not equal.'
        return -1;

    for i in range(len(y)):
        if y[i] == y_predict[i] and y[i] == 1:
            TP += 1
        elif y[i] == y_predict[i] and y[i] == 0:
            TN += 1
        elif y[i] != y_predict[i] and y[i] == 1:
            FN += 1
        else:
            FP += 1

    accuracy = float(TP + TN) / (TP + FP + TN + FN)
    precision = float(TP) / (TP + FP + 0.001) #避免除零异常
    recall = float(TP) / (TP + FN + 0.001)
    F1 = float(2 * precision * recall) / (precision + recall + 0.001)

    print >> sys.stderr, 'TP: %d, FP: %d, FN: %d, TN: %d.' % (TP, FP, FN, TN)
    print >> sys.stderr, 'Accuracy: %.3f' % (accuracy)
    print >> sys.stderr, 'Precision: %.3f, Recall: %.3f, F1: %.3f.' % (precision, recall, F1)

    return accuracy, precision, recall, F1


def label2int(eval_label, y_label_list, predict_label_list, threshold=0.5):
    """
    标签转换为整型
    :param eval_label: 当前评估的label, 评估的label为1，其他都是0。
    :param y_label_list: 
    :param predict_label_list: 
    :param threshold: 大于 threshold 为 1
    :return: 
    """
    if len(y_label_list) != len(predict_label_list):
        print >> sys.stderr, 'Error: Length is not equal.'
        return -1

    y_list = []
    predict_list = []

    for y_label, predict_label_tuple in zip(y_label_list, predict_label_list):

        if y_label == eval_label:
            y_list.append(1)
        else:
            y_list.append(0)

        (predict_label, predict_pro) = predict_label_tuple[0] # 取第一个, k=1

        if predict_label == eval_label and predict_pro >= threshold:
            predict_list.append(1)
        else:
            predict_list.append(0)

    # print y_list, predict_list
    return y_list, predict_list


if __name__ == '__main__':
    # cal_precision_recall_F1()

    label2int('__label__law', [u'__label__law', u'__label__law'], [[(u'__label__law', 0.896484)], [(u'__label__others', 0.421875)]])
