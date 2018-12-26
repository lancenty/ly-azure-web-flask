#run_waitress_server.py
import os  
from waitress import serve  
from App import app

serve(app,host="0.0.0.0",port=os.environ["PORT"]) 
