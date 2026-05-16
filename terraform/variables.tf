variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "sre-capstone-cluster"
}

variable "node_count" {
  description = "Number of worker nodes"
  type        = number
  default     = 2
}
