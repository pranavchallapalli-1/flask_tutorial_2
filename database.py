from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
load_dotenv()
db_info=os.getenv("db_info")
engine = create_engine(db_info)
def load_jobs_from_db():
    with engine.connect() as conn:
        result=conn.execute(text("select * from jobs"))
        result_all= result.all()
        jobs=[]
        for rows in result_all:
            row_dict=rows._asdict()
            jobs.append(row_dict)
        return jobs
j=load_jobs_from_db()
print(j)