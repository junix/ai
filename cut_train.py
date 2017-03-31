import jieba.posseg
import os

if __name__ == '__main__':
    out_dir = '/Users/junix/products_pos'
    for root, _, files in os.walk('/Users/junix/products'):
        for f in files:
            with open(root + '/' + f, 'r') as fd:
                content = f + ''.join(fd.readlines())
                cs = list(jieba.posseg.cut(content))
                cs = ['{word}/{pos}'.format(word=w, pos=p) for (w, p) in cs if w and p]
                with open(out_dir+'/'+f, 'w') as wfd:
                   segs = ' '.join(cs)
                   wfd.write(segs)

