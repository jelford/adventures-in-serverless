# AWS lambda + API Gateway

Tried this out first - I was going to try Google Functions first, but support was limited to Node, and
I wanted to use (modern) python. Even AppEngine is still on Python 2.7, so Google felt like a bit of
a non-starter. Hopefully I'll come back to it later.

## structure:

* `hello-world.yaml` describes the infrascruture required in cloud-formation format
* `lambda_function.py` contains the handler with some sample code
* `serverless-output.yaml` is the result of `aws-cli` processing `hello-world.yaml` (more on that below)

## setup

* added a new user, which was member of the group: serverless-app-trial, which had policy perms:
  * AWSLambdaFullAccess
  * AmazonAPIGatewayInvokeFullAccess
  * serverless-trial-manage-cloudformation-stack (allow on all cloud-formation actions/resources)
  * AmazonAPIGatewayAdministrator
  * AWSLambdaBasicExecutionRole
  * serverless-trial-access-code-bucket (access the bucket where code is uploaded and stored)
* added an S3 bucket for code to be uploaded and stored (hence permission)
* added an execution role (now deleted) for the lambda to run as (`hello-world.yaml/Resources.helloworld.Properties.Role`)
  * granted the role AWSLambdaBasicExecution, AWSLambdaS3Execution, AWSLambdaMicroserviceExecution
* make local dir mountable by docker (thanks to docker/selinux integration): `chcon -Rt svirt_sandbox_file_t .`

## usage

    # Package code and upload to bucket defined above. produces `serverless-output.yaml`
    aws cloudformation package --template-file ./hello-world.yaml --output-template-file serverless-output.yaml--s3-bucket <s3_bucket_name>
    # tear up the infrastructure defined in `serverless-output.yaml` and define a lambda to use the packaged code
    aws cloudformation deploy --template-file ./serverless-output.yaml --stack-name serverless-trial-stack

The rendered `serverless-output.yaml` is identical to `hello-world.yaml` except the `CodeUri` points to an S3 bucket.

## obvious fixups

* The S3 bucket could be defined in `hello-world.yaml` and torn up with the rest of the cloud-formation
* the permissions are far too broad

## things I got wrong

* Not defining an API event in `hello-world.yaml` - no API gateway endpoint
* Output of `lambda_function.lambda_handler` needs to be in format prepared for consumption by API Gateway, not end client (and `body` is a string, not an object)

## I still don't know

* where do my logs go?! They don't seem to be in cloudwatch and friends
