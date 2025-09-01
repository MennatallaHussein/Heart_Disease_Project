import subprocess
import threading
from pyngrok import ngrok, conf
import time
import os
import sys

# Set Ngrok configuration to skip CRL checks
conf.get_default().monitor_thread = False
conf.get_default().crl_check = False

def run_streamlit():
    try:
        subprocess.run(["streamlit", "run", "ui/app.py", "--server.port", "8501"])
    except Exception as e:
        print(f"Streamlit error: {e}")
        sys.exit(1)

def start_ngrok():
    try:
        # Create secure tunnel with static domain
        ngrok.set_auth_token("31O5Jg3tEeewHuUt7CEzH3ELSls_6mc1zs75Wsmz8DiUQowoC")
        public_url = ngrok.connect(8501, "http", options={"region": "eu"})
        print(f"\n{'='*50}")
        print(f"✅ Public URL: {public_url}")
        print(f"{'='*50}\n")
        print("App is live! Use Ctrl+C to stop")
        return public_url
    except Exception as e:
        print(f"Ngrok error: {e}")
        return None

if __name__ == "__main__":
    # Install required packages
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.run([sys.executable, "-m", "pip", "install", "streamlit", "pyngrok", "joblib", "pandas", "matplotlib"])
    
    # Start Streamlit in background thread
    thread = threading.Thread(target=run_streamlit, daemon=True)
    thread.start()
    
    # Give Streamlit time to initialize
    time.sleep(8)
    
    # Start Ngrok
    public_url = start_ngrok()
    
    if public_url:
        # Open browser automatically
        subprocess.Popen(f"start {public_url}", shell=True)
    
    # Keep the script running
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nStopping server...")
        ngrok.kill()
