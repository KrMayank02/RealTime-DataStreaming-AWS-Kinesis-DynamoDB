# RealTime-DataStreaming-AWS-Kinesis-DynamoDB
Project to generate data for Kinesis Data Stream that can be copied to the DynamoDB database using Lambda Function.

**Objective:** To deploy infrastructure for real-time data management requirements on the AWS Cloud offers a scalable, flexible, and cost-effective solution for organizations aiming to harness the power of real-time data processing. You are given a project to create data in a Kinesis stream that can be copied to the DynamoDB database.

**Services, Tools & Environment Used in this Project:**
•	**AWS Console:** The AWS Management Console is a web application that includes and references several service consoles for managing AWS services.

•	**Kinesis DataStream:** Amazon Kinesis Data Stream is a serverless streaming data solution that enables capturing, processing, and storing data streams at any scale.

•	**Lambda Function:** AWS Lambda is a serverless compute service that executes user code in response to events and manages the underlying compute resources automatically.

•	**AWS DynamoDB Database:** Amazon DynamoDB is a fully managed, serverless NoSQL database service provided by Amazon Web Services (AWS) that supports both key-value and document data structures. It is designed to provide single-digit millisecond latency at any scale, making it a primary choice for high-traffic web applications, gaming, and real-time analytics.

•	**AWS CloudShell** is a browser-based command-line environment within the AWS console, pre-authenticated with your account, offering pre-installed tools (AWS CLI, SDKs, Bash, PowerShell) for easy, secure management and scripting of AWS resources without local setup. In this project, we will be generating Data for Kinesis Data stream by running Python script from CloudShell.

**High Level Tasks/Steps:**
	Create an AWS Kinesis Data Streams.
	Create an AWS DynamoDB database-table.
	Create an IAM Role for Lambda Function.
	Create an AWS Lambda Function and add Trigger.
	Generate Data using Python script running on AWS CloudShell.
	Perform Scan Operation on database-table to verify Real time data. 
