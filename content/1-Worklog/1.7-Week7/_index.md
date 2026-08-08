---
title: "Week 7 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

# WEEK 7 (03/08-09/08): DEVELOPING THE STREAMLIT FRONTEND AND CONDUCTING END-TO-END SYSTEM TESTING

## 1. Weekly Objectives

* Develop an intuitive and interactive web interface for end users using Streamlit.
* Securely connect the local web application to AWS cloud resources.
* Refactor the source code to improve project structure and maintainability.
* Perform comprehensive end-to-end testing across the entire system, from the frontend to the backend.

## 2. Tasks Completed

### Streamlit Frontend Development

* Developed the web interface using the Python Streamlit framework.
* Designed a sidebar displaying system configuration information, including:

  * S3 Bucket Name
  * AWS Region
* Implemented a drag-and-drop image upload area to improve user experience.
* Integrated the Pillow library to display image previews along with metadata such as:

  * File name
  * File size (KB)
  * Image dimensions (pixels)
* Developed the **"🚀 Upload to S3 & Analyze"** button, which reads the selected image as bytes and uploads it to Amazon S3 using the AWS SDK for Python (`boto3`).

### Security Configuration and Environment Variables

* Installed and configured the `python-dotenv` package.
* Created a `.env` file to securely store sensitive configuration values:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `S3_BUCKET_NAME`
* Updated the application to automatically execute `load_dotenv()` during startup, eliminating the need to hardcode credentials directly within the source code.

### Source Code Refactoring and Modularization

* Identified that the original `app.py` and `lambda_function.py` files had become excessively large and difficult to maintain.
* Refactored the project into a modular structure with clear separation of responsibilities:

#### Frontend Modules

* `config.py`

  * Loads configuration values from environment variables.

* `validation.py`

  * Contains file validation logic.

* `s3_service.py`

  * Handles Amazon S3 initialization and file upload operations.

* `ui_components.py`

  * Contains reusable Streamlit UI components.

* `app.py`

  * Serves as the lightweight application entry point.

#### Lambda Backend Modules

* `rekognition_service.py`

  * Encapsulates Amazon Rekognition integration logic.

* `dynamodb_service.py`

  * Handles DynamoDB data storage operations.

### End-to-End System Testing

* Executed the Streamlit application locally.
* Used a portrait image of a smiling woman as a sample test input.
* Performed a complete workflow validation:

  1. Upload image through the web interface.
  2. Verify successful upload to Amazon S3.
  3. Confirm automatic Lambda invocation.
  4. Validate image analysis through Amazon Rekognition.
  5. Verify successful storage of analysis results in DynamoDB.

## 3. Knowledge and Skills Acquired

### Modular Programming

* Learned how to design clean and maintainable software architectures.
* Gained experience separating:

  * Presentation Layer (UI)
  * Business Logic Layer (Services)
  * Configuration Layer
* Improved code reusability and simplified future unit testing efforts.

### Integration Debugging Skills

* Developed the ability to troubleshoot issues occurring between local applications and cloud services.
* Learned how to trace and diagnose failures involving AWS APIs, authentication, and service integrations.

## 4. Challenges and Troubleshooting

### Challenge 1

While uploading images through Streamlit, the application displayed the following error:

```text
Upload Failed: AWS credentials not found
```

#### Resolution

* Determined that the application was not loading the `.env` configuration file containing AWS credentials.
* Installed the `python-dotenv` package.
* Imported and executed `load_dotenv()` at the beginning of `app.py`.

---

### Challenge 2

After resolving the credential issue, image uploads failed with an AWS:

```text
AccessDenied
```

error.

#### Resolution

* Identified that the IAM user `streamlit-s3-uploader` did not have the required `s3:PutObject` permission for the newly created S3 bucket.
* Updated the IAM policy by adding an inline policy granting `PutObject` permissions on the target bucket.
* Restarted the application and verified successful uploads.

---

### Challenge 3

Encountered a package compatibility issue while installing Pillow on a local environment running Python 3.14.3.

The version specified in `requirements.txt`:

```text
Pillow==10.3.0
```

did not support the newer Python release.

#### Resolution

* Upgraded Pillow to version:

```text
Pillow==12.3.0
```

which provided full compatibility with the local Python environment.

## 5. Outcomes

* Successfully developed a fully functional Streamlit frontend running smoothly on port **8501**.
* Completed source code modularization, resulting in a cleaner and more maintainable project structure.
* Successfully validated the entire serverless workflow through comprehensive end-to-end testing.
* Confirmed that the system operates reliably from the web interface through Amazon S3, AWS Lambda, Amazon Rekognition, and Amazon DynamoDB with a 100% successful test execution rate.
