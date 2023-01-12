
import requests
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from contact.models import File_Data

def download_file(url, data):
    try:
        
 
        headers = {"Content-Type": "application/json; charset=utf-8"}
 
        data = {
            "id": 1001,
            "name": "geek",
            "passion": "coding",
        }
 
        # response = requests.post(url, headers=headers, json=data)
        # print content of request
        # print(response.json())
        return ""
    except requests.exceptions.RequestException as e:
       return e
 

# @shared_task
def set_reminder_task():
    print('hii')
    threads= []
    data_list = File_Data.objects.filter(is_status=True,contact_status="")
    with ThreadPoolExecutor(max_workers=20) as executor:
        for li in data_list:
            file_name = uuid.uuid1()
            url = "http://127.0.0.1:8000/cognicx/api/create_agent/"
            threads.append(executor.submit(download_file, url, li))
            
        for task in as_completed(threads):
            print(task.result()) 
