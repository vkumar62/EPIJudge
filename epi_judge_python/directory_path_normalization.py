from test_framework import generic_test

import pdb
def shortest_equivalent_path(path):
    # TODO - you fill in here.
    #pdb.set_trace()
    fullpath = []
    if path[0] == '/':
        fullpath.append(path[0])

    for p in path.split('/'):
        if p == '.' or p == '':
            continue
        if p == '..':
            if not fullpath or fullpath[-1] == '..':
                fullpath.append(p)
            elif fullpath[-1] == '/':
                assert 0
            else:
                fullpath.pop()
        else:
            fullpath.append(p)
#    pdb.set_trace()
    result = '/'.join(fullpath)
#    return result[result.startswith('//'):]
    if result.startswith('//'):
        return result[1:]
    else:
        return result
#    return '/' + '/'.join(fullpath) if fullpath[0] == '/' else '/'.join(fullpath)
#    return '/'.join(fullpath if fullpath[0] != '/' else fullpath[1:])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
