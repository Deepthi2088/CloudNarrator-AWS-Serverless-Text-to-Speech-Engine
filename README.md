<h1>Cloud Narrator-AWS-Serverless-Text-to-Speech-Engine</h1>

<h2>✅ Project Description :</h2>
Serverless Blog/Book Narrator is a cloud-based text-to-speech application built using AWS services that converts written content (blogs, articles, newsletters, and book excerpts) into high-quality audio files. The system processes text inputs and dynamically generates speech output, enabling scalable and on-demand audio content creation.
The architecture leverages AWS Lambda for serverless compute and Amazon Polly for neural text-to-speech synthesis, ensuring cost-efficient, event-driven processing without managing servers.

🎯 Key Use Cases
Accessibility Enhancement: Generates audio versions of written content to support visually impaired users and inclusive content delivery.
Educational Support: Enables learners to consume study materials in audio format, improving retention and flexibility.
Multi-Channel Content Distribution: Expands content reach by providing both text and audio formats.
On-the-Go Consumption: Allows users to listen to articles or book excerpts during commutes, workouts, or multitasking. Designed and deployed a serverless architecture using AWS Lambda and Amazon Polly to dynamically convert text content into MP3 audio files. Project 

<h2>Architure diagram</h2>
 
Steps to Build the Project: 
Step 1: Set Up an AWS Account
Step 2: Create two S3 Buckets (Source S3 Bucket Name: amc-polly-source-bucket, Destination S3 Bucket Name: amc-polly-destination-bucket)
Step 3: Create an IAM Policy 
Step 4: Create an IAM Role (IAM Role Name: amc-polly-lambda-role) and attach amc-polly-lambda-policy and AWSLambdaBasicExecutionRole Policies
Step 5: Create and Configure the Lambda Function (Lambda Function Name: TextToSpeechFunction)
Set the runtime to Python 3.8. Set the execution role with necessary permissions for S3 and Polly. (Step 4) Add Environment Variables (SOURCE_BUCKET: Name of your source S3 bucket and DESTINATION_BUCKET: Name of your destination S3 bucket. 
Step 6: Configure S3 Event Notification
Set up an event notification in the source S3 bucket to trigger the Lambda function on new object creation events with the .txt suffix.
 Step 7: Write Lambda Function Code
Step 8: Test the System
