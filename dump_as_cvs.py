import jieba.posseg
import os
import pandas
import pandas as pd


def clean(text):
    text = text.replace(',', '')
    text = text.replace('\n', '')
    return text


if __name__ == '__main__':
    corpus_dir = '/Users/junix/products'
    columns = ['category', 'description']
    df = pd.DataFrame(data=[], index=[], columns=columns)
    for root, _, files in os.walk(corpus_dir):
        category = os.path.basename(root)
        for product in files:
            with open(root + '/' + product, 'r') as fd:
                content = ''.join(fd.readlines())
                record = [clean(category), clean(product + ':' + content)]
                rec = pd.DataFrame(data=[record], index=[clean(product)], columns=columns)
                df = df.append(rec)

    df.to_csv('/Users/junix/products_pos.csv')
