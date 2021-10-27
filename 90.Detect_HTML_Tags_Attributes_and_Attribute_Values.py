# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr,val in attrs:
            print("->",attr,">",val)
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr,val in attrs:
            print("->",attr,">",val)

parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())
