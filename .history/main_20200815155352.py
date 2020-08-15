from Html_Manager import HtmlManager

manager=HtmlManager()
manager.htmlCreation()
manager.save()

AwS=AWS_Manager()
AWS.save_to_s3()
