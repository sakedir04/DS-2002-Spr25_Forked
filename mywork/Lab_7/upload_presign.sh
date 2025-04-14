#!/usr/bin/env bash
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/"
PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$LOCAL_FILE" --expires-in "$EXPIRATION")
echo "$PRESIGNED_URL"
