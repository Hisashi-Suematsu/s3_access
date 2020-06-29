from s3access import S3Access

# s3_accessライブラリの使用例

# インスタンス生成（test_s3accessバケットにアクセスするためのインスタンス）
s3access = S3Access(bucketName="test_s3access")

# オブジェクトリスト取得（demoディレクトリ以下のファイル、フォルダ一覧を取得）
objectList = s3access.getObjectList(prefix="demo/")

# ファイルアップロード（S3のdemoディレクトリにs3access.pyをアップロード）
s3access.uploadFile(filePath="./s3access.py", uploadPath="demo/")

# ファイルダウンロード（S3のdemo/s3access.pyファイルをカレントディレクトリにダウンロード）
s3access.downloadFile(filePath="demo/s3access.py", downloadPath=".")
