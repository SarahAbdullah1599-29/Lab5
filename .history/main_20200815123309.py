import os
import sys

class HtmlDocument:
    def__init__(self):
        pass

class HtmlManager:
    def__init__(self):
        pass

    def writehtml(self):
        samplehtml = open('helloworld.html','w')
        message = """<html><head></head>
        <body><p>Hello WOrld!</></body><html>"""
        samplehtml.write(message)
        samplehtml.close()
class AWSManager:  
    def __init__(self):
        pass      



s1 = HtmlManager()
s1.writehtml()  
