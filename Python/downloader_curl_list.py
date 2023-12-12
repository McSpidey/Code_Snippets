import subprocess
import time
from pathlib import Path
from urllib.parse import urlparse

def download_file(url, download_folder, max_retries=3):
    file_name = get_filename_from_url(url)
    file_path = download_folder / file_name

    retries = 0
    while retries < max_retries:
        try:
            result = subprocess.run(["curl", "-o", str(file_path), url], check=True)
            if result.returncode == 0:
                print(f"Download successful: {url}")
                return True
            else:
                print(f"Failed to download {url}, return code: {result.returncode}")
        except subprocess.CalledProcessError as e:
            print(f"Error during download: {e}")
        
        retries += 1
        print(f"Retrying... ({retries}/{max_retries})")
        time.sleep(1)  # wait 1 second before retrying

    print(f"Failed to download {url} after {max_retries} retries.")
    return False

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    return Path(parsed_url.path).name

def validate_downloads(urls, download_folder):
    missing_files = False
    for url in urls:
        file_name = get_filename_from_url(url)
        file_path = download_folder / file_name
        if not file_path.exists():
            print(f"File not found: {file_name}")
            missing_files = True
        else:
            print(f"File validated: {file_name}")

    if missing_files:
        print("Some files were not downloaded successfully.")
    else:
        print("All files were downloaded and validated successfully.")

def download_files_from_file(file_path, download_folder):
    with open(file_path, 'r') as file:
        urls = [url.strip() for url in file.readlines() if url.strip()]
    
    for url in urls:
        download_file(url, download_folder)
    
    return urls

if __name__ == "__main__":
    #Input text file and output folder
    url_list_file = "C:\\Temp\\url_list.txt"
    output_folder = Path("C:\\Temp\Downloads")

    urls = download_files_from_file(url_list_file, output_folder)
    validate_downloads(urls, output_folder)
