# Simple Static Site with EC2 Logging (AWS Free Tier Project)

This project demonstrates a beginner-friendly AWS architecture using only **Free Tier** services. It hosts a **static website** via **Amazon S3** and uses an **EC2 instance** to generate logs that are uploaded to a separate **S3 bucket**. It’s a great first project after passing the **AWS Certified Cloud Practitioner** (CCP) exam.

## 🧠 Key Concepts
- Static hosting with **S3**
- Basic EC2 setup with **IAM Role** permissions
- Logging from EC2 to S3 using **boto3 (Python SDK)**
- Simple, real-world **cloud architecture**
- All within the **AWS Free Tier**

## 📦 Architecture Overview
[User]
|
▼
[Static Website on S3] <--- (Frontend, Public)
|
▼
[EC2 Instance with IAM Role]
|
▼
[Log Files pushed to a Logging S3 Bucket]


## 🔧 What It Does
- Hosts a public HTML page via S3 static website hosting.
- EC2 instance runs a Python script that logs system or custom data.
- The logs are pushed securely to another S3 bucket via IAM permissions.
- All automated using simple Python and CLI tools.

## 🚀 Skills I'll Practice
- Launching and SSH’ing into an EC2 instance
- Setting up and testing S3 static website hosting
- Writing Python scripts with `boto3`
- Creating and attaching IAM roles securely
- Uploading and verifying logs in S3
