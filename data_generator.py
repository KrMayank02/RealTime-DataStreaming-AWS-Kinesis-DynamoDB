import boto3
import time
import json
import random

# Configure your Kinesis stream
stream_name = "CustomerStream"  # Replace with your Data Stream name
region_name = "us-east-1"       # Replace with your AWS region

# Create a Kinesis client
kinesis_client = boto3.client('kinesis', region_name="us-east-1")

def generate_customer_data():
    """Generates random customer data."""
    return {
        "customer_id": random.randint(1000, 9999),
        "name": random.choice(["Alice", "Bob", "Charlie", "David", "Eve", "Mayank", "Kabeer"]),
        "email": f"user{random.randint(1, 100)}@example.com",
        "age": random.randint(18, 60),
        "location": random.choice(["New York", "London", "Sydney", "Mumbai", "Tokyo", "Johannesburg", "Singapore"])
    }

# Send data every 15 seconds
try:
    while True:
        data = generate_customer_data()
        print(f"Sending data: {data}")
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=str(data["customer_id"])  # Use customer_id as PartitionKey
        )
        print(f"Record sent with SequenceNumber: {response['SequenceNumber']}")
        time.sleep(15)      # Wait for 15 seconds
except KeyboardInterrupt:
    print("Stopped sending data!")