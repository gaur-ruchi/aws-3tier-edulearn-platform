# aws-3tier-edulearn-platform

## Overview

EduLearn is a production-inspired 3-tier web application deployed on AWS.

The solution demonstrates secure network design, application deployment, load balancing, content delivery, and database integration using AWS services. The frontend is hosted on Amazon S3 and distributed through CloudFront, while a Flask-based API processes registration requests and stores user data in a MariaDB database hosted within a private subnet.

---

## Architecture

### Presentation Tier

* Amazon Route 53
* Amazon CloudFront
* Amazon S3 Static Website Hosting

### Application Tier

* Application Load Balancer (ALB)
* Amazon EC2 (Flask API)
* Private Application Subnets

### Database Tier

* MariaDB on Amazon EC2
* Private Database Subnets

### Networking & Security

* Custom VPC
* Public and Private Subnets
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* AWS Systems Manager Session Manager (SSM)

---

## Architecture Flow

User
 ↓
Route53
 ↓
CloudFront
 ↓
Amazon S3 Static Website

Application Load Balancer
 ↓
Flask API (EC2)
 ↓
MariaDB Database (EC2)

---

## Key Features

* Static website hosting using Amazon S3
* Global content delivery through CloudFront
* REST API built with Flask
* Secure private application and database tiers
* Database-driven registration workflow
* Load balancing using ALB
* Session Manager access without SSH
* Security Group-based tier isolation

---

## AWS Services Used

| Category       | Services                                                  |
| -------------- | --------------------------------------------------------- |
| DNS            | Route 53                                                  |
| CDN            | CloudFront                                                |
| Storage        | Amazon S3                                                 |
| Compute        | Amazon EC2                                                |
| Load Balancing | Application Load Balancer                                 |
| Database       | MariaDB                                                   |
| Networking     | VPC, Subnets, Route Tables, Internet Gateway, NAT Gateway |
| Security       | IAM, Security Groups, SSM                                 |

---

## Network Design

### Public Layer

* CloudFront
* Application Load Balancer
* NAT Gateway

### Private Layer

* Application EC2 Instance
* Database EC2 Instance

---

## Security Controls

* Application server deployed in a private subnet
* Database server deployed in a private subnet
* Security Group-based communication between tiers
* No SSH access exposed publicly
* AWS Session Manager used for administration
* Database accessible only from the application tier

---

## Application Workflow

1. User accesses the website through Route53.
2. Static content is served from Amazon S3.
3. Registration form submits data to the Flask API through the ALB.
4. Flask validates and processes the request.
5. Registration data is stored in MariaDB.
6. Records can be queried directly from the database tier.

---

## Production Considerations

This project uses MariaDB hosted on a dedicated EC2 instance inside a private database subnet for learning purposes.

For production environments, the database layer should be replaced with:

* Amazon RDS MySQL
* Multi-AZ deployment
* Automated backups
* Automated failover
* Read replicas (if required)
---

## Lessons Learned

* Designing secure 3-tier AWS architectures
* Configuring VPC networking and routing
* Implementing application tier and database tiers using multi-az environment.
* Deploying Flask applications on EC2
* Integrating applications with relational databases
* Configuring ALB health checks and target groups
* Troubleshooting SSM connectivity
* Resolving CloudFront, CORS, and browser security issues
* Applying AWS security best practices

---

