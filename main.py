import re
import fileinput
import fire


def sub_in_file(filename, regex, sub=''):
    r = re.compile(regex)
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(r.sub(sub, line), end='')


if __name__ == '__main__':
    fire.Fire(sub_in_file)
