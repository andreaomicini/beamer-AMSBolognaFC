import re
import sys
from functools import lru_cache


@lru_cache()
def latex_command_re(command):
    return re.compile("\\newcommand{\\" + command + '}{(\\d+)}')


# does not work, need to investigate
def get_command_value2(string, command, default=None):
    regex = latex_command_re(command)
    matches = regex.findall(string)
    print(f"Testing {string} against {regex} = {matches}")
    if len(matches) > 0:
        return matches[0]
    else:
        return default


def get_command_value(string, command, default=None):
    if command in string:
        return string.split('}{')[1][0:-1]
    else:
        return default


major = None
minor = None
patch = None


def none_is_none(*args):
    return all((it is not None for it in args))


with (open(sys.argv[1], mode='r') if len(sys.argv) > 1 else sys.stdin) as file:
    for line in file.readlines():
        line = line.strip()
        if not line.startswith("%"):
            major = get_command_value(line, "stylemajor", major)
            minor = get_command_value(line, "styleminor", minor)
            patch = get_command_value(line, "stylepatch", patch)
            # print(f"'{line.strip()}' -> major={major}, minor={minor}, patch={patch}")
            if none_is_none(major, minor, patch):
                break


print(major, minor, patch, sep='.')
