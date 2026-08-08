---
title : "Prerequiste"
date : 2024-01-01 
weight : 2 
chapter : false
pre : " <b> 5.2. </b> "
---

# 5.2. Prerequisites

Before starting this workshop, make sure you have prepared the required environment, tools, and AWS permissions.

---

## 1. AWS Account & IAM Configuration

To deploy and run resources in this workshop, you need an active AWS Account. If you are participating in a student cohort, you can use **AWS Academy Learner Labs**.

### Step 1.1: Create an IAM User (for Local Development)
If you are using a standard AWS account:
1. Navigate to the **IAM Console**.
![Picture_1](/images/5-Workshop/1.png)
2. Click **Users** -> **Create user**.
![Picture_2](/images/5-Workshop/2.png)
![Picture_3](/images/5-Workshop/3.png)
3. Name your user (e.g., `workshop-developer`) and check **Provide user access to the AWS Management Console - optional** if you need console access, or simply create it without management access for API use.
![Picture_4](/images/5-Workshop/4.png)
4. Attach the following managed policies directly to the user (for workshop convenience, though least-privilege is recommended in production):
   - `AmazonS3FullAccess`
   - `AmazonDynamoDBFullAccess`
   - `AmazonRekognitionFullAccess`
   - `AWSLambda_FullAccess`
   - `IAMFullAccess`
![Picture_5](/images/5-Workshop/5.png)
![Picture_6](/images/5-Workshop/6.png)
![Picture_7](/images/5-Workshop/7.png)
![Picture_8](/images/5-Workshop/8.png)
![Picture_9](/images/5-Workshop/9.png)
![Picture_10](/images/5-Workshop/10.png)

### Step 1.2: Generate Access Keys
1. In the user details, click on the **Security credentials** tab.
![Picture_11](/images/5-Workshop/11.png)
![Picture_12](/images/5-Workshop/12.png)
2. Under **Access keys**, click **Create access key**.
![Picture_13](/images/5-Workshop/13.png)
3. Choose **Command Line Interface (CLI)** and check the confirmation box.
![Picture_14](/images/5-Workshop/14.png)
4. Download the `.csv` file containing the `Access key ID` and `Secret access key`.
![Picture_15](/images/5-Workshop/15.png)

{{% notice warning %}}
Never commit your AWS Access Keys or your `.env` file to public Git repositories (e.g., GitHub). These credentials grant full administrative control over your resources and can result in high billing charges if compromised.
{{% /notice %}}

---

## 2. Local Environment Setup

### Step 2.1: Install Python
Ensure that Python **3.12+** is installed on your local computer. You can check your version in a terminal:
```bash
python --version
```

### Step 2.2: Setup AWS CLI
1. Download and install the AWS CLI for your Operating System:
   - [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Open your terminal (Command Prompt, PowerShell, or bash) and run:
   ```bash
   aws configure
   ```
3. Enter your credentials when prompted:
   ```text
   AWS Access Key ID [None]: <YOUR_ACCESS_KEY_ID>
   AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
   Default region name [None]: ap-southeast-1
   Default output format [None]: json
   ```

---

## 3. Project Initialization & Dependencies

### Step 3.1: Initialize the Project Directory
Create a project folder and navigate inside it:
```bash
mkdir Emotion-recognition-app
cd Emotion-recognition-app
```

### Step 3.2: Create a Virtual Environment
It is highly recommended to isolate your project dependencies using a Python virtual environment:

**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3.3: Install Libraries
Create a file named `requirements.txt` with the following content:
```text
streamlit
boto3
Pillow
python-dotenv
```

Then install the packages using `pip`:
```bash
pip install -r requirements.txt
```
