from flask import Flask,render_template, request, redirect,url_for
import cv2
import boto3
from botocore.exceptions import Nocredentialerror

app=Flask(_name_)

#AWS S3 credentials 
AWS_ACCESS_KEY_ID =‘YOUR_AWS_KEY_ID’
AWS_SECRET_ACCESS_KEY = ‘YOUR_AWD_SECRET_ACCESS_KEY’
AWS_BUCKET_NAME =‘YOUR_AWS_BUCKET_NAME’

#Create an S3 client 
S3 = boto3.client (‘s3’,aws_access_key_id=ACCESS _KEY_ID,
      aws_secret_access_key=AWS_SCREAT_ACCESS_KEY)

#Video upload endpoint 
@app.route(‘/upload ’, methods=[‘POST’])
def upload _video():
    video _file = request.files[‘video_file,’]
try: 
    # Get the video file from S3 
    Video _file = s3.get_object(Bucket=AWS_BUCKET_NAME,KEY =VIDEO_FILE_NAME)
   #Stream the video file 
   return video _flie[‘Body’].read(),200,{‘content-Type’:‘video/mp4’}
   except NoCredentialserror:
     return ‘Invalid AWS Credentials ’

if _name_==‘_main_’:
    app.run(debug=True)

templates/index.html

<! DOCTYPE html>
<html>
  <head>
  <title> CLOUD BASED VIDEO STREAMING APPLICATION<title>
</head>
<body>
 <h1>upload a video:<h1>
<from action“/upload ”method=“post”enctype=“multipart/from-data”>
 < input type = “file”name=“video_file” accept=“video/*”>
<button type=“submit”>upload</button>
</from>
<h1>Stream a video:</h1>
<from action=“/stream ”method=“get”>
  <input type=“text” name="video _file_ name”placeholder=“Enter video file name ”>
   <button type=“submit”>Stream</button>
   </from>
 </body>
</html>