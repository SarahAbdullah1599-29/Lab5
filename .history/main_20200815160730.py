from Html_Manager import HtmlManager

manager=HtmlManager()
manager.htmlCreation()
manager.save()

AwS=AWSManager()
AWS.save_to_s3()
