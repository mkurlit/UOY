import re

def check_on_file(file, rx = None):
    """Read file and check regex patterns
        Params:
            file -> file path
            (rx) -> regex pattern
            (word) -> word to be looked for"""
    try:
        with open(file, 'r') as file:
            absorbed = file.read()
            if word:
                match = re.search(r'\b'+word+r'\b', absorbed.lower())
                if match:
                    print(f'{word} found in the file')
                else:
                    print(f'{word} not in the file')
            elif rx:
                matches = re.findall(rx, absorbed.lower())
                print(matches)
    except IOError:
        print('File does not exist')
 
## Count words with 'pp'
matches = re.findall('\w*p{2}\w*',raven.lower())

## Change ! to #
swap = re.sub('!','#',raven)

## Words starting with 't' and ending with anything but 'e'
match_words = re.findall('^t[a-z]*[^e]$|\st[a-z]*[^e]\s|^t[a-z]*[^e]\s|\st[a-z]*[^e]$', raven.lower())

