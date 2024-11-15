<!--https://github.com/darsaveli/Readme-Markdown-Syntax-->

### Collaborators:
* **[Lochlann O Neill](https://github.com/lochlannoneill)**
  
-----
  
### Running the project

1. Install **'boto3'**
   ```bash
   pip install boto3

2. Install **'tabulate'** for enhanced terminal output
   ```bash
   pip install tabulate

3. **(Optional)** Include pre-supplied user information in **'src/config/passwords.json'** or create new users during runtime.
   ```bash
   [
      {
         "name": "David",
         "password": "12345pass",
         "access key": "PPB7952+AmaYUd+824nmW",
         "secret key": "AmaYUd"
      },
      {
         "name": "John",
         "password": "aaaaaaaaa",
         "access key": "AKOP67NKAF",
         "secret key": "CpA9752SDF+709+fa09faAfG"
      },
      {
         "name": "Joan",
         "password": "bcbcbcddddddd",
         "access key": "AIL67NK8NM",
         "secret key": "KMALF75+95mml+7+89052"
      }
   ]

4. Execute the application
   ```bash
   python -m src.app

-----

### AWS Menu - EC2 Instances:  

List Instances:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/instance_list.png)

Start Instance:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/instance_start.png)

Stop Instance:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/instance_stop.png)

Delete Instance:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/instance_delete.png)

List AMIs of Instance:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/ami_list.png)

Create AMI:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/ami_create.png)

Delete AMI:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/ec2/ami_delete.png)

### AWS Menu - EBS Storage:  

List Volumes:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/volume_list.png)

Create Volume:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/volume_create.png)

Attach Volume:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/volume_attach.png)

Detach Volume:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/volume_detach.png)

Modify Volume:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/volume_modify.png)

Delete Volume:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/volume_delete.png)

List Snapshots:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/snapshot_list.png)

Create Snapshot:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/snapshot_create.png)

Delete Snapshot:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/snapshot_delete.png)

Create Volume From Snapshot:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/volumes/snapshot_create_volume.png)

### AWS Menu - S3 Storage:  

List Buckets:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/s3/bucket_list.png)

Delete Bucket:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/s3/bucket_delete.png)

List Objects in Bucket:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/s3/object_list.png)

Download Object:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/s3/object_download.png)

Delete Object:  
![image](https://github.com/lochlannoneill/COMP9076-CloudAutomationAndOrchestration-AWS/blob/main/screenshots/s3/object_delete.png)
