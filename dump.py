import jieba.posseg
import os
import pandas
import pandas as pd

if __name__ == '__main__':
    out_dir = '/Users/junix/products_pos'
    df = pd.DataFrame(data=[], index=[], columns=['category', 'description'])
    for root, _, files in os.walk('/Users/junix/products'):
        category = os.path.basename(root)
        for product in files:
            with open(root + '/' + product, 'r') as fd:
                content = product + ''.join(fd.readlines())
                product = product.replace(',', '')
                content = content.replace(',', '')
                content = content.replace('\n', '')
                df2 = pd.DataFrame(data=[[category, content]], index=[product], columns=['category', 'description'])
                df = df.append(df2)

    df.to_csv('/Users/junix/products_pos.csv')
    print(df)
