import os
from mobula import rmdir
from mobula import HASH_FILENAME, GRAPH_FILENAME


def find_all_build(path):
    result = []
    for name in os.listdir(path):
        fname = os.path.join(path, name)
        if os.path.isdir(fname):
            if os.path.basename(fname) in ['build', HASH_FILENAME, GRAPH_FILENAME]:
                result.append(fname)
            else:
                result.extend(find_all_build(fname))
    return result


if __name__ == '__main__':
    res = find_all_build('./')
    for r in res:
        rmdir(r)
