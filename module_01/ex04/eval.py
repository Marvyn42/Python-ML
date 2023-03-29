from sys import exit


class Evaluator:
    def __init__(self, coefs, words):
        self.check_args(coefs, words)
        self.zip_evaluate(coefs, words)
        self.enumerate_evaluate(coefs, words)

    @staticmethod
    def check_args(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list)\
           or len(coefs) != len(words) or len(coefs) == 0:
            exit("-1")
        for elem in coefs:
            if not isinstance(elem, (int, float)):
                exit("-1")
        for elem in words:
            if not isinstance(elem, str):
                exit("-1")

    @staticmethod
    def zip_evaluate(coefs, words):
        sum = 0
        words_coefs = zip(words, coefs)
        for word, coef in words_coefs:
            sum += len(word) * coef
        print(sum)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        sum = 0
        words_iter = enumerate(words)
        for index, word in words_iter:
            sum += len(word) * coefs[index]
        print(sum)
