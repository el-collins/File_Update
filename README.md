# FastAPI File Operations API

## Overview
This FastAPI project provides a simple yet powerful API for handling file operations. It includes endpoints for checking the size of a file and extracting file extensions from uploaded files.

## Features
- **Check File Size**: Determine the size of a file in bytes.
- **Get File Extensions**: Retrieve the extensions of uploaded files.

## Installation
To run this project, you need to have Python 3.6+ installed. Set up a virtual environment and install the dependencies:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

## Usage
Start the FastAPI server with the following command:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### Check File Size
- **URL**: `/files/`
- **Method**: `POST`
- **Body**: A single file in `bytes`.
- **Response**: The size of the file in bytes.

### Create Upload File
- **URL**: `/uploadfile/`
- **Method**: `POST`
- **Body**: A list of files to upload.
- **Response**: A list of file extensions from the uploaded files.

## Examples

### Check File Size
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/files/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path/to/your/file'
```

### Create Upload File
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/uploadfile/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@path/to/your/file1' \
  -F 'files=@path/to/your/file2'
```

## Development
To contribute to this project, clone the repository, create a new branch for your feature or fix, and submit a pull request.

## License
This project is licensed under the terms of the MIT license.

---
