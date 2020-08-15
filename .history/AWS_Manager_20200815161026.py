import boto3
class AWSManager:
    def __init__(self):

    def save_to_s3(self):
        boto3.client('s3').upload_file('helloworld.html', 'lmtd-class','helloworld.html'
        )

    def load_from_s3(self):
        boto3.client('s3').download_file('lmtd-class','helloworld.html','helloworld.html')

    def read_from_s3(self):
        obj = boto3.resource('s3').Object('lmtd-class','heyshafan.json')
        print(type(obj))
        data = json.load(obj.get()['Body'])
        print(data) 
