import os, json
import pandas as pd
from botocore.exceptions import EndpointConnectionError


class CustomValidationError(Exception):
    def __init__(self, arguments=None, message=None):
        self.arguments = arguments
        self.message = message

    def __str__(self):
        for key, val in self.arguments.items():
            return f"Please Specify carefully {val} in env key  export {key}=your_value\n {self.message}"


class ReadFiles:
    FILES = ['teachers.parquet', 'students.csv']

    def __init__(self):
        self.location = os.environ.get('FILE_LOCATION', False)
        if not self.location:
            raise CustomValidationError(arguments={'FILE_LOCATION': 'file_locaiton'}, message=
            "Please mention file location for S3\n "
            "s3://bucket_name/folder or \n"
            " /Users/username/Desktop/folder/ "
            "\n")

    def __red_s3_file(self, file):
        if file.endswith('.csv'):
            read_data = pd.read_csv(f'{self.location}/{file}', delimiter='_')
        else:
            read_data = pd.read_parquet(f'{self.location}/{file}', engine='pyarrow')
        return read_data

    def __readfile(self):
        data_frame = []
        if os.path.isdir(self.location):
            teachers, students = None, None
            for file in os.listdir(self.location):
                if file.endswith('.parquet'):
                    teachers = pd.read_parquet(self.location + '/teachers.parquet',
                                               engine='pyarrow')
                elif file.endswith('.csv'):
                    students = pd.read_csv(self.location + '/students.csv', delimiter='_')

            data_frame.extend((teachers, students))
        elif self.location.startswith('s3'):
            for file in self.FILES:
                out = self.__red_s3_file(file)
                data_frame.append(out)
        return data_frame

    def __parsing(self, teachers, students):
        parse_data = []
        for index, row in teachers.iterrows():
            tmp = {
                'teacher_id': row['id'],
                'teacher_name': row['fname'] + ' ' + row['lname'],
                'class_id': row['cid']
            }
            temp = []
            for ind, r in students[students['cid'] == row['cid']].iterrows():
                x = {'student_id': r['id'],
                     'student_name': r['fname'] + ' ' + r['lname']
                     }
                temp.append(x)

            tmp['students'] = temp
            parse_data.append(tmp)
        return json.dumps(parse_data)

    def output_json(self):
        file_data = self.__readfile()
        out_put_json = self.__parsing(file_data[0], file_data[1])
        return out_put_json


if __name__ == "__main__":
    try:
        obj = ReadFiles()
        data = obj.output_json()
        print(data)
    except EndpointConnectionError:
        print("Please configure your aws on system carefully")
