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
        yield from map(str.upper, super().__iter__())


class TokenizerWithoutMixin(BaseTokenizer):
    def __iter__(self):
        yield from [token.upper() for token in self.str_token.split("-")]


class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass


class Tokenizer2(UpperIterableMixin, BaseTokenizer2, BaseTokenizer):
    pass


class OnlyAlphabetTokenizer(SubtractStrExceptAlphabetMixin, BaseTokenizer):
    pass


class OnlyUppercaseAlphabetTokenizer(UpperIterableMixin, SubtractStrExceptAlphabetMixin, BaseTokenizer):
    pass


if __name__ == "__main__":
    example_str = "ab/c-d/e-f/gh-ij/klm-nop"
    print(f"original string: {example_str}\n")

    tk_without_mixin = TokenizerWithoutMixin(example_str)
    print("without mixin) separate delimiter is '-'\n", list(tk_without_mixin))
    print()

    tk1 = Tokenizer(example_str)
    print("separate delimiter is '-'\n", list(tk1))
    print()

    tk2 = Tokenizer2(example_str)
    print("separate delimiter is '/' and '-'\n", list(tk2))
    print()

    tk3 = OnlyAlphabetTokenizer(example_str)
    print("separate delimiter is '-' and remove other character except alphabet\n", list(tk3))
    print()

    tk4 = OnlyUppercaseAlphabetTokenizer(example_str)
    print("separate delimiter is '-' and remove other character except alphabet and change result to uppercase\n",
          list(tk4))

