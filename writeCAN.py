import os
import os.path


class fileOperate:
    def __init__(self,file_test = None):
        pass
    def open(self):
        current_path = os.getcwd()
        # print(current_path)

        file_test = open(current_path + '/' + 'test.txt', 'w', encoding='utf-8')
# 注意如果是在WIN系统，在写入中文时，需要设置编码格式;如果不是WIN系统，则不需要设置编码格式
    def write(self, file_test=None):
        file_test.write('Python 是一门优雅的编程语言')
        file_test.close()