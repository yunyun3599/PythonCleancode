if __name__ == "__main__":
    sample_dict = {'a': 'A', 'b': 'B'}
    print(sample_dict.get('b'))
    print(sample_dict.get('b', 'BB'))
    print(sample_dict.get('c', 'C'))
    print(sample_dict.get('c'))
