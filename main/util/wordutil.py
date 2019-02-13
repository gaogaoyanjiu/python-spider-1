# -*-coding:utf-8-*-
"""语句拆分工具"""
import jieba


# 将语句拆分成词语
def cut_word(word):
    return list(jieba.cut(word))