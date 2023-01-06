import re


class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


class BaseTokenizer2:
    def __iter__(self):
        for tokenized_str in super().__iter__():
            yield from tokenized_str.split("/")


class SubtractStrExceptAlphabetMixin:
    def __iter__(self):
        yield from [re.sub(r'[^a-zA-Z]', '', tokenized_str) for tokenized_str in super().__iter__()]


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer2, BaseTokenizer):
    pass


class OnlyAlphabetTokenizer(UpperIterableMixin, SubtractStrExceptAlphabetMixin, BaseTokenizer):
    pass


if __name__ == "__main__":
    example_str = "ab/c-d/e-f/gh-ij/klm-nop"
    print(f"original string: {example_str}\n")

    tk = Tokenizer(example_str)
    print("separate delimiter is '/' and '-'\n", list(tk))
    print()

    tk2 = OnlyAlphabetTokenizer(example_str)
    print("separate delimiter is '-' and remove other character except alphabet\n", list(tk2))

