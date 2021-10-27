# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr,val in attrs:
            print("->",attr,">",val)
            
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr,val in attrs:
            print("->",attr,">",val)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())
