---
title : "Testing & Policy"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---
# 5.5. Testing & Verification

In this module, you will run an end-to-end test of the entire serverless facial emotion recognition pipeline, verifying that each stage executes correctly.

---

## Step 1: Run the Streamlit Interface

1. Start your application locally if it is not already running:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to `http://localhost:8501`.
![Picture_50](/images/5-Workshop/50.png)
3. Locate a test image containing a clear face (e.g., a happy/smiling person).
4. Drag and drop the image into the Streamlit uploader.
5. Verify the **File Info** and the **Preview** image render correctly in the UI.
6. Click the primary button **🚀 Upload to S3 & Analyze**.
![Picture_51](/images/5-Workshop/51.png)
7. Confirm that the UI displays a success banner: `✅ Image uploaded successfully!` and balloons float up on the screen.
![Picture_52](/images/5-Workshop/52.png)

---

## Step 2: Verify Image in Amazon S3

Ensure that the Streamlit application successfully wrote the object to your cloud storage bucket.

1. Open the **Amazon S3 Console**.
2. Click on the name of your bucket (e.g., `my-facial-emotion-recognition-<unique-suffix>`).
![Picture_53](/images/5-Workshop/53.png)
3. Navigate into the folder structure: `uploads/` -> `<Current-Date> (YYYY-MM-DD)/`.
![Picture_54](/images/5-Workshop/54.png)
![Picture_55](/images/5-Workshop/55.png)
4. Verify that your uploaded image is listed in this directory.
![Picture_56](/images/5-Workshop/56.png)

---

## Step 3: Check Lambda Function Logs (AWS CloudWatch)

Verify that the S3 event trigger was successfully delivered and that the Lambda function processed the image.

1. Open the **AWS Lambda Console** and navigate to your function: `FaceEmotionRecognitionHandler`.
![Picture_57](/images/5-Workshop/57.png)
2. Select the **Monitor** tab.
3. Click the **View CloudWatch logs** button (this opens the CloudWatch Log Groups console).
![Picture_58](/images/5-Workshop/58.png)
4. Select the latest log stream.
5. Look for log statements matching the pipeline execution:
   ```text
   INFO Lambda invoked. Event: {"Records": [...]}
   INFO Processing image: s3://my-facial-emotion-recognition-.../uploads/2026-07-27/test_face.png
   INFO Calling Rekognition for s3://my-facial-emotion-recognition-...
   INFO Rekognition detected 1 face(s) in test_face.png
   INFO Top emotion for test_face.png: HAPPY (99.54%)
   INFO Saved record LogID=... to DynamoDB table FaceEmotionLogs
   ```

---

## Step 4: Verify Analysis Data in Amazon DynamoDB

Confirm that the analyzed metadata was successfully persisted in the NoSQL table.

1. Open the **Amazon DynamoDB Console**.
2. In the left navigation pane, click **Explore items**.
![Picture_59](/images/5-Workshop/59.png)
3. Select your table: `FaceEmotionLogs`.
![Picture_60](/images/5-Workshop/60.png)
4. Click on the items search to display all items.
5. Verify that a new row has been written containing:
   - `LogID` (a unique UUID string)
   - `Timestamp` (ISO-8601 UTC format)
   - `ImageName` (the base name of the uploaded image)
   - `FaceCount` (number of detected faces)
   - `TopEmotion` (e.g., `HAPPY`, `SAD`, `ANGRY`)
   - `Confidence` (the confidence percentage score of the dominant emotion)
![Picture_61](/images/5-Workshop/61.png)
