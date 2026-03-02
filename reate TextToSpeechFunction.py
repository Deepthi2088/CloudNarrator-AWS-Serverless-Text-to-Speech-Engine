import json
import time
import boto3

polly = boto3.client("polly")
s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        record = event["Records"][0]["s3"]
        source_bucket = record["bucket"]["name"]
        file_key = record["object"]["key"]

        # Get text file from S3
        obj = s3.get_object(Bucket=source_bucket, Key=file_key)
        text = obj["Body"].read().decode("utf-8")

        # Convert text to speech
        polly_response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        if "AudioStream" not in polly_response:
            raise Exception("Polly did not return audio data")

        audio_bytes = polly_response["AudioStream"].read()
        audio_key = f"speech-{int(time.time()*1000)}.mp3"

        # Upload audio file to another bucket
        s3.put_object(
            Bucket="buket-of-polly-audio-files",  # replace with your bucket
            Key=audio_key,
            Body=audio_bytes,
            ContentType="audio/mpeg"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Conversion successful",
                "source_file": file_key,
                "audio_file": audio_key
            })
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
