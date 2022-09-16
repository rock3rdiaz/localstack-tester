terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
        }
    }
}

provider "aws" {
    region                      = "us-east-1"
    access_key                  = "access_key"
    secret_key                  = "secret_key"
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    s3_use_path_style           = true
    skip_requesting_account_id  = true

    endpoints {
        sns         = "http://localstack:4566"
        sqs         = "http://localstack:4566"
        dynamodb    = "http://localstack:4566"
        s3          = "http://localstack:4566"
        events      = "http://localstack:4566"
        iam         = "http://localstack:4566"
    }
}

module "eventbridge" {
  source = "terraform-aws-modules/eventbridge/aws"

  bus_name = "my-bus"

  create_permissions = true

  permissions = {
    "099720109477 DevAccess" = {}
    
    "099720109466 ProdAccess" = {
        action = "events:PutEvents"
    }
  }

  tags = {
    Name = "my-bus"
  }
}

resource "aws_s3_bucket" "test-bucket" {
    bucket = "my-bucket"
}
