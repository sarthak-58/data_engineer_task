## **Task :**
To create a small app in python, An application that processes two data files [students.csv , teachers.parquet]. The application should use both files to output a report in json listing each student and the teacher.
The application will be used with both local and files stored in aws S3, so there should be an easy way to specify the location of these files and the output json.


## **Modules used :**
- os : to access files from local directory
- json : to output a proper json formatted data
- pandas : for processing csv and parquet files
- pyarrow : to access parquet files 
- botocore : for accessing S3 bucket files and exception handling corresponding to S3 functionalities
 

## **Set up environment :**
**Create an environment :**
```python
python -m virtualenv venv
```

 
**Activate environment :**
```python
source venv/bin/activate
```

 
**Install requirements**
```python
pip install -r requirements.txt
```


## Environment variable setting :
If file is in local :
```bash
export FILE_LOCATION=<location of folder where files are located>
```
If file is in S3 :
```bash
export FILE_LOCATION=s3://bucketname
```
 

## **Commands to run :**
**Git clone** :
```git
git clone <url>
```

**Command to run :**
```python
python3 -m venv /path/to/venv        # could be any path
source /path/to/venv/bin/activate
pip install -r requirements.txt
python3 app.py
```


**Docker commands :**
```dockerfile
$ docker build -t task-app .
$ docker run -it --rm --name my-running-task task-app
```