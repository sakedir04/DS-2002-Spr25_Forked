#!/usr/bin/env python3
import sys
import requests
import boto3 # type: ignore

def main():
    url = sys.argv[1]
    bucket = sys.argv[2]
    key = sys.argv[3]
    exp = int(sys.argv[4])
    r = requests.get(url)
    with open('temp_file', 'wb') as f:
        f.write(r.content)
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.put_object(Body=open('temp_file','rb'), Bucket=bucket, Key=key)
    p = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': key}, ExpiresIn=exp)
    print(p)

if __name__ == "__main__":
    main()
