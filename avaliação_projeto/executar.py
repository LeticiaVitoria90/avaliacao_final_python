import subprocess
import threading
from flask import Flask, jsonify, request
import os

def run_flask():
    os.system('python app.py')

def run_streamlit():
    os.system('streamlit run streamlit_app.py')

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_streamlit()
