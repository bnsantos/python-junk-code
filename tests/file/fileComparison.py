__author__ = 'bruno'
import os
import filecmp
import shutil


#files_dir = '/home/bruno/Downloads/wazap videos/'
#repeated_files_dir = '/home/bruno/Downloads/wazap videos/repeated/'

files_dir = '/home/bruno/Downloads/Wazapphotos/'
repeated_files_dir = '/home/bruno/Downloads/Wazapphotos/repeated/'


def check_files():
    sizes = {}
    for f in os.listdir(files_dir):
        file_size = os.stat(files_dir + f).st_size
        if file_size not in sizes:
            sizes[file_size] = [f]
        else:
            sizes[file_size].append(f)
    repeated_folder_name = 1
    for key in sizes.keys():
        if len(sizes[key]) > 1:
            files = 'Files: '
            for f in sizes[key]:
                files += f + ' ,'

            print 'Files size: ', key, ' - ', files
            i = 0
            while i < len(sizes[key]):
                f = sizes[key][i]
                equals = [f]
                for j in range(i, len(sizes[key])):
                    f2 = sizes[key][j]
                    if f != f2:
                        if filecmp.cmp(files_dir + f, files_dir + f2):
                            print 'Equals ', f, f2
                        else:
                            print 'Different ', f, f2
                            equals.append(f2)
                if len(equals) > 1:
                    os.mkdir(repeated_files_dir + str(repeated_folder_name))
                    destination = repeated_files_dir + str(repeated_folder_name) + '/'
                    for moving_file in equals:
                        shutil.move(files_dir+moving_file, destination + moving_file)
                        sizes[key].remove(moving_file)
                        i += 1
                    repeated_folder_name += 1
                else:
                    i += 1
            print ' '

check_files()