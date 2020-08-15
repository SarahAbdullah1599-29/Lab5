from Html_Document import HtmlDocument

class HtmlManager:
    def __init__(self):
        self.document= None
        
    def htmlCreation(self):
        message = """<html><head></head>
        <body><p>Hello Sarah</p></body>
        </html>"""
        new_doc=HtmlDocument(message)
        self.document=new_doc
        
        #htmlexample = open('helloworld.html','w')
        #htmlexample.write(message)
        #htmlexample.close()
        #webbrowser.open_new_tab('helloworld.html')

    def save(self):
        #self.to_save=self.msg
        #self.save1.htmlCreation(self.to_save)  
        f = open('helloworld.html','w')
        f.write(self.document.content)
        f.close