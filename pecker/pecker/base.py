#coding=gb2312

class base:
    def __init__(self):
        self.filename = ''
        self.fp = None
        self.depth = 0
        self.mini_depth = 0
        self.depth_stack = 0
        self.func_list = []  # [name, beginline, endline]
        self.func_begin = 0
        self.func_name = ''
        self.line_num = 0
        self.commente_begin = 0
        self.func = []
        return

    #打开需要解析的文件
    def open(self, filename):
        self.filename = filename
        self.fp = open(filename)
        if None == self.fp:
            return
        return

    #读取函数深度
    def read_depth(self, line):
        tmp = line.replace(' ', '')
        if tmp == 'extern\"c\"{':  #extern "c" { 不是正常的函数起始
            self.mini_depth = self.mini_depth + 1

        for i in range(len(line)):
            if line[i] == '{':
                self.depth = self.depth + 1
            elif line[i] == '}':
                if 0 == self.depth:
                    print("error depth 0, line:", line, self.line_num)
                    continue
                self.depth = self.depth - 1
            else:
                continue
        return

    #函数名是包含(的，且depth最小，不能是注释
    def read_func_name(self, line):
        if self.mini_depth != self.depth:
            return

        if -1 == line.find('('):
            return

        line = line.strip()

        if '#' == line[0]:
            return

        func_name = ''
        tmp = line.split(" ")
        for name_tmp in tmp:
            if -1 != name_tmp.find('('):
                func_name = name_tmp.split('(')[0]
                break
            else:
                if -1 != name_tmp.find('('):
                    break
                func_name = name_tmp
        if '' != func_name:
            self.func_list.append([func_name, 0, 0])
        pass

    def read_func_begin(self, line):
        if 0 == len(self.func_list):
            return False

        item = self.func_list[len(self.func_list) - 1]
        if 0 != item[1]:
            return False

        if -1 == line.find("{"):
            return False

        self.func_begin = self.line_num
        item[1] = self.line_num
        return True

    def read_func_end(self, line):
        if 0 == len(self.func_list):
            return

        if 0 == self.func_begin:
            return

        if self.mini_depth == self.depth:
            #print (self.depth, self.line_num, line)
            self.func_begin = 0
            self.func_list[len(self.func_list) - 1][2] = self.line_num

    def skip_comment(self, line):
        if True == self.commente_begin:
            t = line.find("*/")
            if -1 == t:
                return '', True
            self.commente_begin = False
            return line[t+2:], True
        else:
            t = line.find('/*')
            if -1 == t:
                return line, False
            self.commente_begin = True
            return line[0:t],True

    def readfile(self):
        for line in self.fp:
            self.line_num = self.line_num + 1

            while True:
                line, comment = self.skip_comment(line)
                if '' == line:
                    break
                if False == comment:
                    break
            if '' == line:
                continue

            for func in self.func:
                func(line, self)

            self.read_func_name(line)
            self.read_depth(line)
            if True == self.read_func_begin(line):
                continue
            self.read_func_end(line)
            pass

