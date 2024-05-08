provider "aws" {
  region = "your_aws_region"
}

resource "aws_emr_cluster" "example" {
  name          = "example-cluster"
  release_label = "emr-6.15.0"
  service_role  = "EMR_DefaultRole"
  log_uri       = "s3://your-bucket/logs/"

  ec2_attributes {
    instance_profile = "EMR_EC2_DefaultRole"
    instance_type    = "m5.xlarge"
    instance_count   = 1
    subnet_id        = "subnet-1231231313"
  }

  scale_down_behavior = "TERMINATE_AT_TASK_COMPLETION"

  tags = {
    Backup            = "None"
    "Application Name" = "Hadoop"
    "Name"            = "Hive"
  }

  applications {
    name = "Hadoop"
  }

  applications {
    name = "Hive"
  }
}
