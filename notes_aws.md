This document describes any and all notes pertaining to AWS as well as AWS CLI commands.  
You can find more info AWS CLI, here: https://aws.amazon.com/cli/  


<h2>General</h2>

AWS CLI is a command line interface used to manage your AWS services.
With this tool, you can download and configure multiple AWS services from the command line.
You can access AWS CLI from any terminal and you don’t have to login or do anything different after setting it up.



You can check that you have correctly installed aws cli by typing:
`aws --version`

You can check your aws credentials with:
`aws configure list`

You can update your aws by typing:
`aws configure`
[only do this if you want to update]


Once done, you can start using AWS CLI.
Entering this will update your credentials.

You cannot change directories in aws cli.
Instead, you must enter your directory with each command.

A simple example using the ls command:  
`aws s3 ls`  
This returns the list of all files and folders in your default directory.

To look at some directories in s3, run:  
`aws s3 ls s3://some_path/`

You can add a pipe to take the output of one process and pass it as input for another process.
Examples:  
`aws s3 ls s3://some_path/ | grep -i abc`
`aws s3 ls s3://some_path/test_folder1/ | grep -i name1`

aws s3 mv - moves a file from local machine to aws s3. This copies the file over and then deletes it.  
For example: `aws s3 mv “my_file” “my_s3_uri”`

 

A good s3 folder to test moving files/folders is: s3://mdx-des/ftp/

 

To remove a single file:
aws s3 rm s3://mdx-des/ftp/self_service/member/filename.
Example:
aws s3 rm s3://mdx-des/ftp/self_service/member/BASYSElig_Test_V1.zip --dryrun

To handle AWS connections, use python packages: boto3, botocore

For help, type:
aws help
aws <command> help



To get around case sensitivity in AWS S3:
Put double quotes around any variables being passed in shell, like:
aws s3 ls mdx-sftp-production/pba/incoming/ | grep -i “${file_pattern}”


Copy command example:
/home/some_path/bin/aws s3 cp --region us-east-1 --no-progress "s3://some_path/file1.txt" "/data/name1"

 
To get all metadata on an object in AWS s3, you can run:  
`aws s3api head-object --bucket “bucket_name” --key “key_name”`
Where bucket is the 1st folder in 1s and the key is the remaining folders + the file name.


AWS terms:
EC2 = Elastic Compute Cloud. It uses compute instances of virtual servers on a cloud.
VPC = Virtual Private Cloud.
SCP = secure copy protocol.
AMI = Amazon Machine Image. This is a supported image provided by AWS that provides information required to launch an instance. You must specify an AMI to launch an instance. These are operating system images. 

<h2>EC2</h2>

To copy a file from s3 to your EC2 instance:  
`aws s3 cp s3://my_bucket/my_folder/my_file.ext my_copied_file.ext`

To copy a file from your instance back to s3:  
`aws s3 cp my_copied_file.ext s3://my_bucket/my_folder/my_file.ext`

Copying files from s3 to ec2 is called Downloading the file.
ec2 to s3 is called Uploading the file.

<h2>AWS Glue</h2>

In AWS Glue, namespaces refer to the database name.

<h2>AWS Glue CLI</h2>

If you want to run an aws glue command from CLI, you must first update your aws config.

1) Go to your home directory with: cd ~/.aws
Open your config file with: vi config
Ensure that the output is not “None”. If it is, update it to “text” or another format.
Close with “escape” “:wq”.

2) Open your credentials file with: vi credentials
Enter your aws_access_key_id, aws_secret_access_key_id, aws_session_token
Ensure the line above those credentials is labeled: [default]
Comment out your old credentials if you are switching between aws credentials.


To check the status of your current table in a database, type:  
`aws glue get-table --database-name "test_scott_db" --name "iceberg1"`

You can also look at all databases, with:  
`aws glue get-databases`


To update an s3 path for a table in aws glue, type:
aws glue update-table --database-name test_scott_db --table-input '{
    "Name": "iceberg1",
    "StorageDescriptor": {
        "Location": "s3://some_path/iceberg1"
    }
}'
Note: I would use this command to update folders and move basic files.
Updating the s3 path for a table is not enough to move an iceberg table.
For moving an iceberg table, I recommend trying other methods in AWS Glue.


The syntax to repair a table in AWS Glue with a query, is:  
`MSCK REPAIR TABLE db_name.your-table-name;`

For example:
MSCK REPAIR TABLE test_scott_db.facility_iceberg2;

<h2>Crawlers</h2>

You can use a crawler to crawl your tables and determine the datatypes of your tables.
However, crawler does not have support for Iceberg tables.


<h2>Loading JSON files</h2>

AWS Glue does not natively support SQL INSERT INTO operations for Iceberg tables.
Instead, AWS Glue primarily uses Spark for ETL operations.

So you need to use a Spark dataframe operation to write data to an Iceberg table.