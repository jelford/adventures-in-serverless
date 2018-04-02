# serverless

[serverless](https://serverless.com) claims to be a cross-provider solution. It lists the big three
(AWS, Google, Azure) along with some solutions I hadn't come across (`kubeless` stands out).

* I'll try it out with AWS, to compare like with like. 
* I'll get going with one of their templates, instead of trying to go from scratch as I did on AWS, since I haven't used serverless before

## Setup

* `npm install -g serverless`
* re-using AWS credentials from AWS-sam setup
* update region in the serverless config

## differences to vanilla AWS setup

* encoded the notion of _stage_ from the off (something I didn't get round to on AWS-sam)
* came with a bunch of ideas about how my infrastructure should be laid out (e.g. wanted to create IAM roles straight off, without asking)
* when it failed to tear up, fully deleted the failed cloud-formation (real rollback without me needing to jump into the console and fix it manually)
* a fully-featured walkthrough tutorial linked from [the docs](https://serverless.com/blog/serverless-express-rest-api/) - rather than un-joined-up reference docs
* Got logs coming through in CloudWatch without doing anything

## commonalities

* Both AWS-native and serverless take the time to talk about the _lambda_'s permissions
  * ... but they don't talk so much about the permissions required by the tooling doing the setup (that is, my local user). I want to know about that, if I'm to automate deployment.
  * serverless does actually have a [page on](https://serverless.com/framework/docs/providers/aws/guide/credentials/?rd=true) this, but basically just recommend granting Admin rights
* still can't find my logs
* separate offline-test tool (`npm install --save-dev serverless-offline` + a `plugin` config line in `serverless.yaml`)
  * but offline mode is *a lot* faster... but I doubt it's doing as much - e.g. no docker container
  * other plugins for cloud resources (e.g. `npm install --save-dev serverless-dynamodb-local` - didn't try it out)

## issues

* Python is less of a 1st-class citizen here
  * e.g. packaging python apps takes the form of [a blog post](https://serverless.com/blog/serverless-python-packaging/)
  * uses a neat workflow for packaging python deps through Docker rather than asking you to build everything on an EC2 host
