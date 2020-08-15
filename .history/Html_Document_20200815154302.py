class HtmlDocument:
    def __init__(self, content):
        #self.msg = """<html><head></head><body><p><Hey Sarah!!</p></body></html>"""
        #self.save1 = HtmlManager()
        self.content=content

    def __str__(self):
        return(f'{self.content}')


    