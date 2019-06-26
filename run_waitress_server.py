#run_waitress_server.py
import os
from waitress import serve
from App import app
from werkzeug.contrib.profiler import ProfilerMiddleware

app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
serve(app,host="0.0.0.0",port=os.environ["PORT"])
#serve(app,host="0.0.0.0")
