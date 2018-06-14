# Example-for-Fasttext

A workable example for fasttext based on python version

fasttext模型示例（基于python）


## 运行
```
python fasttext_classifier.py
```

## 示例运行结果
```
Start training model, training file: data/news_fasttext_train.txt, saved model path: model/news_model.
Training over. cost 3.93s
Start evaluating model, load model from "model/news_model.bin".

Current evaluation class: "__label__affairs".
Test sample size: 1000.
Target sameple size: 1000.
TP: 1000, FP: 0, FN: 0, TN: 0.
Accuracy: 1.000
Precision: 1.000, Recall: 1.000, F1: 0.999.

Finally, model accuracy: 1.000, precision: 1.000, recall: 1.000.
Start predicting model, load model from "model/news_model.bin".
[[u'affairs'], [u'affairs'], [u'affairs'], [u'affairs'], [u'affairs'], [u'affairs'], [u'affairs'], [u'affairs'], [u'affairs'], [u'affairs']]
[[(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)], [(u'affairs', 1.0)]]

```

## 数据输入格式


1. **training data and test data**

- each line represents a sample 

例如：
```
“想请他出任赛事嘉宾。他们决定答应佩纳的要求并请他前来参赛”。它的label是affairs。
```
需要处理为如下：
```

想 请 他 出任 赛事 嘉宾 。 他们 决定 答应 佩纳 的 要求 并 请 他 前来 参赛 。  __label__affairs
```

其中每一个词之间用空格隔开，最后一个词和‘\_\_label\_\_’之前用‘\t’隔开



2. **predict data**

例如：
```
“想请他出任赛事嘉宾。他们决定答应佩纳的要求并请他前来参赛”。
```
需要处理为如下：
```

想 请 他 出任 赛事 嘉宾 。 他们 决定 答应 佩纳 的 要求 并 请 他 前来 参赛 。


