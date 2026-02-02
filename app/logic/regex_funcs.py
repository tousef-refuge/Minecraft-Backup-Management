import re

#these functions work with the assumption that the
#string ends with #<num> and do nothing otherwise
def get_end_num(string):
    num = re.search(r"#(\d+)$", string)
    return int(num.group(1)) if num else 0

def remove_end_num(string):
    return re.sub(r"#\d+$", '', string)