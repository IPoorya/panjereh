# Panjereh APIs

Panjereh is a real estate platform providing various features to analyze the real estate market 

## Setup

The first thing to do is to clone the repository:

```bash
git clone https://github.com/IPoorya/panjereh
cd panjereh
```
Create a virtual environment to install dependencies in and activate it:
```bash
python3 -m venv env
source env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```
Once pip has finished downloading the dependencies create migrations and apply them:
```bash
python manage.py makemigrations
python manage.py migrate
```

and run server:
```bash
python manage.py runserver
```
## Liara Bucket Configs
Liara (amazonS3) bucket is used for this project. so fill your bucket credentials in the .env file:

```bash
LIARA_ENDPOINT= # bucket endpoint
LIARA_BUCKET_NAME= # bucket name
LIARA_ACCESS_KEY= # bucket access key
LIARA_SECRET_KEY= # bucket secret key
```
[pip](127.0.0.1:8000/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.