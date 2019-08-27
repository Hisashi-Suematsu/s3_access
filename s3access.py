import boto3


class S3Access:
    # 引数：バケット名
    def __init__(self, bucketName):
        self.bucketName = bucketName
        self.bucket = boto3.resource('s3').Bucket(self.bucketName)

    # オブジェクトリストを取得する（引数：プレフィックス）
    def getObjectList(self, prefix):
        s3client = boto3.Session().client('s3')
        objectList = []
        respose = s3client.list_objects(
            Bucket=self.bucketName,
            Prefix=prefix
        )
        if 'Contents' in respose:
            objectList = [content['Key'] for content in respose['Contents']]
        return objectList

    # ファイルをアップロードする（引数：アップロード元[local]ファイルパス、アップロード先[S3]のパス）
    def uploadFile(self, filePath, uploadPath):
        self.bucket.upload_file(filePath, uploadPath)

    # ファイルをダウンロードする（引数；ダウンロード元[S3]のファイルパス、ダウンロード先[local]のパス）
    def downloadFile(self, filePath, downloadPath):
        self.bucket.download_file(filePath, downloadPath)
