#! /home/disk2/huangjunheng/.jumbo/bin/python
# -*- coding: utf-8 -*-
"""
 Filename @ config.py
 Author @ huangjunheng
 Create date @ 2018-06-06 19:24:29
 Description @
"""

# Script starts from here


class Config(object):
    """配置文件

        """
    def __init__(self):

        self.train_file = 'data/news_fasttext_train.txt'

        self.test_file = 'data/news_fasttext_test.txt'

        self.predict_file = 'data/news_fasttext_predict.txt'

        self.save_model = 'model/news_model'


if __name__ == '__main__':
    pass
