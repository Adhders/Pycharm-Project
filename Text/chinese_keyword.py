#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright by 
# Author: Jokercrow
# Time : 2019/6/28 11:21

# https://github.com/lancopku/PKUSeg-python
import pkuseg

seg = pkuseg.pkuseg()  # 程序会自动下载所对应的细领域模型

# pkuseg.pkuseg(model_name = "default", user_dict = "default", postag = False)
# 	model_name		模型路径。
# 			        "default"，默认参数，表示使用我们预训练好的混合领域模型(仅对pip下载的用户)。
# 				"news", 使用新闻领域模型。
# 				"web", 使用网络领域模型。
# 				"medicine", 使用医药领域模型。
# 				"tourism", 使用旅游领域模型。
# 			        model_path, 从用户指定路径加载模型。
# 	user_dict		设置用户词典。
# 				"default", 默认参数，使用我们提供的词典。
# 				None, 不使用词典。
# 				dict_path, 在使用默认词典的同时会额外使用用户自定义词典，可以填自己的用户词典的路径，词典格式为一行一个词。
# 	postag		        是否进行词性分析。
# 				False, 默认参数，只进行分词，不进行词性标注。
# 				True, 会在分词的同时进行词性标注。


text = seg.cut('我爱北京天安门')              # 进行分词
print(text)
# pkuseg.test('input.txt', 'output.txt', nthread=20)
