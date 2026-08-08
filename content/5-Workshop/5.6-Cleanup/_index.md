---
title : "Clean up"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

# 5.6. Resource Cleanup

To prevent unexpected billing charges on AWS and keep your cloud environment clean, you must delete all the resources created during this workshop once you have finished testing.

---

## Step 1: Stop the Streamlit Web App

1. Go to your local terminal running Streamlit.
2. Press `Ctrl + C` to stop the web server.
3. Close the browser tab.

---

## Step 2: Empty and Delete Amazon S3 Bucket

AWS S3 buckets cannot be deleted unless they are completely empty.

1. Open the **Amazon S3 Console**.
2. Select your bucket (e.g., `my-facial-emotion-recognition-<unique-suffix>`).
3. Click **Empty**.
![Picture_62](/images/5-Workshop/62.png)
4. Type `permanently delete` in the text field to confirm and click **Empty**.
![Picture_63](/images/5-Workshop/63.png)
5. Once empty, go back to the S3 bucket list, select the bucket, and click **Delete**.
![Picture_64](/images/5-Workshop/64.png)
6. Type the exact name of the bucket to confirm, then click **Delete bucket**.
![Picture_65](/images/5-Workshop/65.png)

---

## Step 3: Delete Amazon DynamoDB Table

1. Open the **Amazon DynamoDB Console**.
2. In the left menu, click **Tables** -> **Update settings** or select **Tables** directly.
![Picture_66](/images/5-Workshop/66.png)
3. Select the `FaceEmotionLogs` table.
4. Click the **Delete** button at the top right.
![Picture_67](/images/5-Workshop/67.png)
5. Confirm by typing `delete` in the prompt, then click **Delete**.
![Picture_68](/images/5-Workshop/68.png)

---

## Step 4: Delete AWS Lambda Function

1. Open the **AWS Lambda Console**.
2. Locate the function `FaceEmotionRecognitionHandler`.
3. Check the checkbox next to it, click **Actions** dropdown, and select **Delete**.
![Picture_69](/images/5-Workshop/69.png)
4. Click **Delete** in the confirmation dialog.
![Picture_70](/images/5-Workshop/70.png)

---

## Step 5: Clean Up IAM Policies & Roles

1. Open the **IAM Console**.
![Picture_71](/images/5-Workshop/71.png)
2. Click **Roles** in the left sidebar. Search for and select `workshop-lambda-role`, then click **Delete**. Confirm by typing the role's name.
![Picture_72](/images/5-Workshop/72.png)
3. Click **Policies** in the left sidebar. Search for `workshop-lambda-policy`, click **Actions** -> **Delete**, and confirm the deletion.
![Picture_73](/images/5-Workshop/73.png)
![Picture_74](/images/5-Workshop/74.png)

---

{{% notice note %}}
**AWS Billing Reminder:**
Deregistering and deleting resources immediately stops further usage accumulation. While services like S3, DynamoDB, and Lambda have generous Free Tier limits (e.g., S3 allows 5GB of storage, DynamoDB allows 25GB, Lambda allows 1 million free requests per month), keeping unused resources idle can eventually lead to active charges once the 12-month Free Tier period expires. Always make cleanup a standard practice in your development workflow.
{{% /notice %}}
