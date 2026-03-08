import threading
import webview
import subprocess
import time
import requests


def start_streamlit():
    subprocess.Popen(["streamlit", "run", "bc.py", "--server.headless=true"])


def wait_for_streamlit():
    url = "http://localhost:8501"
    while True:
        try:
            requests.get(url)
            break
        except:
            time.sleep(1)


t = threading.Thread(target=start_streamlit)
t.daemon = True
t.start()

wait_for_streamlit()

webview.create_window("套利计算器", "http://localhost:8501", width=600, height=500)

webview.start()
