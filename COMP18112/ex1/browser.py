#!/usr/bin/env python
#!/usr/bin/python

import urllib

def recursive(n):
    url = 'http://studentnet.cs.manchester.ac.uk/ugt/COMP18112' + n
    data = urllib.urlopen(url)
    tokens = data.read().split()

    bold = "\033[1m"
    reset = "\033[0;0m"

    startPrinting = False

    for token in tokens:
        if token == '</title>':
            startPrinting = False
            print '\n'
        elif token == '</h1>':
            startPrinting = False
        elif token == '</a>':
            startPrinting = False
        elif token == '</p>':
            startPrinting = False
        elif token == '</em>':
            startPrinting = False
            print reset
        elif token == '<title>':
            print '\n TITLE: ',
            startPrinting = True
        elif token == '<h1>':
            print '\n HEADING: ',
            startPrinting = True
        elif token == '<p>':
            print '\n PARAGRAPH: ',
            startPrinting = True
        elif token == '<a':
            print tokens[tokens.index('<a') + 2],
            startPrinting = False
        elif token == '<em>':
            print bold,
            startPrinting = True
        elif startPrinting:
            print token,
            continue

    print '\n'

    links = []

    for x in tokens:
        sth = x.find('/page')
        if sth != -1:
            links.append(x[sth : sth + 11])

    nr = 0

    while nr < len(links):
        print nr + 1, ": ", links[nr]
        nr = nr + 1

    myMessage = raw_input('Select a link :')

    print '\n'

    if myMessage == '1':
        recursive(links[0])
    elif myMessage == '2':
        recursive(links[1])



recursive('/page3.html')
