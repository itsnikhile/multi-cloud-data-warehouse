# Multi-Cloud DWH Infrastructure
terraform {
  required_providers {
    aws   = { source = "hashicorp/aws",   version = "~> 5.0" }
    azurerm = { source = "hashicorp/azurerm", version = "~> 3.0" }
    google = { source = "hashicorp/google", version = "~> 5.0" }
  }
}

# AWS Redshift
resource "aws_redshift_cluster" "main" {
  cluster_identifier = "${var.env}-analytics"
  node_type          = "ra3.4xlarge"
  number_of_nodes    = 2
  database_name      = "analytics"
  master_username    = var.redshift_user
  master_password    = var.redshift_password
  tags = { Environment = var.env }
}
