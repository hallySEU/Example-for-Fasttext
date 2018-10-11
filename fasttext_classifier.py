# -*- coding: utf-8 -*-
"""
 Filename @ fasttext_classifier.py
 Author @ huangjunheng
 Create date @ 2018-06-06 19:24:29
 Description @
"""

# Script starts from here

import fasttext
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import indicator
import data_process
from config import Config


class FasttextClassifier(object):
    """基于fasttext的文档分类器.

        文档分类

        """
    def __init__(self):
        """
        初始化
        """
        self.config = Config()

    def train(self):
        """
        训练函数
        :return: 
        """
        start_time = time.time()
        traing_file = self.config.train_file
        save_path = self.config.save_model
        print >> sys.stderr, 'Start training model, training file: %s, saved model path: %s.' \
                             % (traing_file, save_path)

        classifier = fasttext.supervised(traing_file, save_path, label_prefix='__label__', 
                                         dim=100, word_ngrams=2, bucket=2000000, loss='softmax')

        end_time = time.time()
        print >> sys.stderr, 'Training over. cost %.2fs' % (end_time - start_time)
        return classifier

    def eval_model(self, model_path, eval_data_file):
        """
        评估模型
        :param model_path: 模型存放地址
        :param eval_data_file: 评估的文件路径
        :return: 
        """
        print >> sys.stderr, 'Start evaluating model, load model from "%s".' % (model_path + '.bin')
        classifier = fasttext.load_model(model_path + '.bin')
        content_array, label_array = data_process.get_model_input_by_data(eval_data_file)
        predict_array = classifier.predict_proba(content_array)

        eval_label_list = list(set(label_array))
        accuracy_total = 0.0
        precision_total = 0.0
        recall_total = 0.0
        for label in eval_label_list:
            print >> sys.stderr, '\nCurrent evaluation class: "%s".' % label
            y_list, predict_list = indicator.label2int(label, label_array, predict_array, threshold=0.5)
            accuracy, precision, recall, F1 = indicator.cal_precision_recall_F1(y_list, predict_list)

            accuracy_total += accuracy
            precision_total += precision
            recall_total += recall

        time.sleep(1)
        class_size = len(eval_label_list)
        print "\nFinally, model accuracy: %.3f, precision: %.3f, recall: %.3f." \
              % (accuracy_total / class_size, precision_total / class_size, recall_total / class_size)

    def predict(self, model_path, predict_file):
        """
        预测函数
        :param model_path: 模型存放地址
        :param predict_file: 预测文件路径
        :return: 
        """
        print >> sys.stderr, 'Start predicting model, load model from "%s".' % (model_path + '.bin')
        classifier = fasttext.load_model(model_path + '.bin', label_prefix='__label__')
        test_data_array, _ = data_process.get_model_input_by_data(predict_file)

        y_predict = classifier.predict(test_data_array)
        print y_predict

        y_predict_pro = classifier.predict_proba(test_data_array)
        print y_predict_pro

    def main(self):
        """
        主函数
        :return: 
        """
        self.train()
        self.eval_model(self.config.save_model, self.config.test_file)
        self.predict(self.config.save_model, self.config.predict_file)


if __name__ == '__main__':
    classifier = FasttextClassifier()
    classifier.main()
