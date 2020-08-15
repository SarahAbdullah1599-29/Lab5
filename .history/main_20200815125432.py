class HtmlDocument:
    def __init__(self):
        pass



class HtmlManager:
    def __init__(self):
        pass
        
    def htmlCreation(self):
        htmlexample = open('helloworld.html','w')
        
        message = """<html><head></head>
        <body><p>Hello World Sarah Abdullah!</p></body>
        </html>"""
        
        htmlexample.write(message)
        htmlexample.close()

class AWSManager:
    def __init__(self):
        pass


s1 = HtmlManager()
s1.htmlCreation()

