__author__ = 'bruno'
import os
import filecmp


files_dir = '/home/bruno/Downloads/wazap videos/'


def check_files():
    sizes = {}
    files_checksum = {}
    for f in os.listdir(files_dir):
        file_size = os.stat(files_dir + f).st_size
        if file_size not in sizes:
            sizes[file_size] = [f]
        else:
            sizes[file_size].append(f)

    for key in sizes.keys():
        if len(sizes[key]) > 1:
            files = 'Files: '
            for f in sizes[key]:
                files += f + ' ,'

            print 'Files size: ', key, ' - ', files

            for i in range(len(sizes[key])):
                f = sizes[key][i]
                for j in range(i, len(sizes[key])):
                    f2 = sizes[key][j]
                    if f != f2:
                        if filecmp.cmp(files_dir + f, files_dir + f2):
                            print 'Equals ', f, f2
                        else:
                            print 'Different ', f, f2
            print ' '

check_files()