import re

def check_magic_code(line, obj):
    if -1 != line.find('#'):
        return False
    line = line.strip()
    pattern = re.compile(r'[^\[-zA-Z](\d){2,20}[^\]a-zA-Z]')
    if None != pattern.search(line):
        print('find magic code', obj.filename, str(obj.line_num), line)
        return True
    return False