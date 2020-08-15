from AWS_Manager import AWSManager
from Html_Manager import HtmlManager

manager=HtmlManager()
manager.htmlCreation()
manager.save()

AWS=AWSManager()
AWS.save_to_s3()
