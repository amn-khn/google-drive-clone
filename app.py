from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

BUCKET_NAME = "amzn-google-drive"

s3 = boto3.client("s3")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        file.filename
    )

    return f"{file.filename} uploaded successfully!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)









