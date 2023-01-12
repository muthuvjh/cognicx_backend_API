from base import Base_Load
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import pyodbc 
import json
from pathlib import Path
import os
import openpyxl
class Loadrecord_Get(Base_Load):
    def __init__(self, stop_event):
        super().__init__(stop_event)
    def download_file(self,url, data,li):
        try:
            
            
            headers = {"Content-Type": "application/json; charset=utf-8"}
            response = requests.post(url, headers=headers, json=data)
            data=response.json()
            data.update({'id':li['id']})
            # print(data)
            return data
        except requests.ConnectionError as e:
            print(e)
            pass
        # except requests.exceptions.RequestException as e:
        #     print(e)
        #     return e
    def process(self,query):
        try:
            cnxn=pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};'
                                    'SERVER=localhost;'
                                    'PORT=3306;'
                                    'DATABASE=cognicx;'
                                    'UID=root;'
                                    'PASSWORD=vjh0304$;')
            cursor = cnxn.cursor()
            cursor.execute("SELECT id,agent_id from contact_Agent_Master where is_status=true") 
            columns = [column[0] for column in cursor.description]
            data_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
            BASE_DIR = Path(__file__).resolve().parent.parent
            PROJECT_PATH=os.path.join(BASE_DIR, "cognicx_backend/cognicx_backend/media")
            MEDIA_ROOT = os.path.join(PROJECT_PATH, "agent")   
            for ai in data_list:
                checkpath = os.path.join(MEDIA_ROOT,str(ai['agent_id']))
                if os.path.exists(checkpath):
                    query = "INSERT INTO contact_Agent_Master (agent_id,email,phone,address,is_status,added_at) VALUES (?,?,?,?,?)"
                    print('hiii')
                    dir_list =os.listdir(checkpath)
                    for fi in dir_list:
                        fil=os.path.join(checkpath,fi)
                        file_extension = Path(fil).suffix
                        if file_extension =='.bak':
                            continue
                        if not os.path.isfile(fil): continue
                        with open(str(fil), 'rb') as f:
                            files = {'file': f}
                            values = {'agent_id':ai['agent_id']}
                            url= 'http://127.0.0.1:8000/cognicx/api/file_upload/'
                            r = requests.post(url, files=files, data=values)
                            print(r.text)
                        
                        oldbase = os.path.splitext(fi)
                        newname = fil.replace('.xlsx', '.xlsx.bak')
                        output = os.rename(fil, newname)

            #Campaign Check with thread
            threads= []
            cursor.execute("SELECT id,name,phone,agent_id,xl_data,campaign,is_status from contact_file_data where is_processed=false") 
            columns = [column[0] for column in cursor.description]
            data_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
            with ThreadPoolExecutor(max_workers=10) as executor:
                #file List
                for li in data_list:
                    salry='0'
                    loc=""
                    li['xl_data']=json.loads(li['xl_data'])
                    if 'Salary' in li['xl_data']:
                        salry=li['xl_data']['Salary']
                    if 'Location' in li['xl_data']:
                        loc=li['xl_data']['Location']
                    pas_data={"utilId":15,"utilName":"CampaignUtility","rowValue":loc,"columnValue":salry,"channel":"CTI"}
                    
                    url = "http://43.241.62.118:8080/rule/ruleEngine/validateRuleUtil"
                    threads.append(executor.submit(self.download_file, url, pas_data,li))
                    
                for task in as_completed(threads):
                    
                    data=task.result()
                    
                    if data['status']==200:
                        if data['value'] is  None:
                            cursor.execute("UPDATE contact_file_data set campaign='',is_processed=true WHERE id = "+str(data['id']))
                        else:
                            cursor.execute("UPDATE contact_file_data set campaign='"+data['value']+"',is_processed=true WHERE id = "+str(data['id']))
                        cursor.commit()
            cnxn.close()
        except Exception as e:
             
             print(e)
             pass
            
        
        