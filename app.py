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

import boto3
import json 

S3 = boto3.client(‘s3’)
lambda_client = boto3.client(‘lambda’)

def lambda _handler ( event,context):
    #Get the video file from S3 
    video _file = s3.get _object(Bucket=‘my-bucket’,key=‘video.mp4’)

#Stream the video file 
return {
      ‘statuscode’:200,
      ‘body’: video_ file [‘body’].read(),
      ‘haeders’: {
           ‘content-Type’: ‘video/mp4’
      } 
  }

2.Google cloud-based video streaming application using python 

import os
from google.cloud import storage 
from flask import send_file

client = storage.client()

def video_streaming(request):
    #Get the video file from cloud storage 
    bucket = client.get_bucket(‘my-bucket’)
  blob = bucket.get_blob(‘video.mp4’)

  #Stream the video file 
return send_file(blob.download_as_string(),mimetype=‘video/mp4’)

3.Microsoft Azure cloud-based video streaming using python uses Azure blob storage, Azure function and Azure API management 

import os
import azure.functions as function
from azure.storage.blob import Blob services client

blob_service_client = 
Blobserviceclient.from_connection_string(os.environ[‘AZURE_STORAGE_CONNECTION_STRING’])

def main(req: function.HttpResponse:
   # Get the video file from Blob storage 
   blob_client = blob_client.gey_blob_client(container=‘my-container’,blob=‘video.mp4’(

  # Stream the video file 
 return 
func.HttpResponse(body=blob_client.downloader_blob(). content _as_bytes(),mimetype=‘video/mp4’)

4.IBM CLOUD BASED VIDEO STREAMING USING PYTHON 
IBM cloud object storage,IBM cloud functions,and IBM cloud API

import os
from ibmcloudant.cloudant_v1 import cloudantV1 
from flask import send_file

client = cloudantV1.new_instance()

def video_streaming(request):
    # Get the video file from cloud object storage 
  bucket = client.get_bucket(‘my-bucket’)...
 file = bucket.get_object(‘video.mp4’)

# Stream the video file 
return send _file(file.get()[‘body’].read(),mimetype=‘video/mp4’)