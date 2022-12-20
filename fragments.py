#A small project for my cloud computing class
#Replace TargetArn with your desired sns arn
#This function takes HTTP post requests through an API gateway that come with a json body containing an "order" and a "fragment." Order must be 0-9, and once the function reaches 10 words it will put them in order and send it to the target sns arn.
#this is not robust to faulty inputs or errors, and if you take to long to do the post requests then it will reset and lose its ephermeral storage, to fix this, you could store the order and words in an s3 bucket or some other form of permanent storage


import json
import boto3

count = 0
arr = []
arr = ["" for i in range(10)] 
final = ""
def lambda_handler(event, context):
    
    global arr
    
    global count
    
    global final
    # TODO implement
   
    order = event['order']
    fragment = event['fragment']
    
    arr[int(order)] = fragment
  
    count = count+1
    
    
    if count==10:
        
    
        for i in range(10):
            
            if i==9:
                final+=arr[i]
            
            else:
                final+=arr[i] + ' '
            
            
            
        final.replace("\u2019", "'")
        notification = "test"
        client = boto3.client('sns')
        response = client.publish (
        TargetArn = "TARGET ARN HERE",
        Message = json.dumps({'default': notification}),
        MessageAttributes={
            'uid': {
                'DataType': 'String',
                'StringValue': '1',
            },
        
            'quote': {
                'DataType': 'String',
                'StringValue': final,
            }
        },   
        MessageStructure = 'json'
    )
    
    
    
    
    return {
        'statusCode': 200,
        'body': str(count) + ' ' + order + ' ' + fragment + ' ' + str(arr) + ' ' + final
    }
