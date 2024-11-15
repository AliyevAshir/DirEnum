import requests
from queue import Queue
import threading
import sys
import time
import itertools

def log_output(message):
    print(message)
    with open("directory_scan_results.log", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

def animate_scan(queue):
    for char in itertools.cycle(["|", "/", "-", "\\"]):
        if queue.empty():
            break
        sys.stdout.write(f"\rScanning {char} ")  # Dynamic animation
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r")  # Clear line when done

def check_directory(base_url, directory, queue):
    full_url = f"{base_url}/{directory.strip()}"
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code != 404:  # Ignore 404 statuses
            print(f"\033[92m[+] Found: {full_url} - HTTP Status: {response.status_code}\033[0m")
            log_output(f"[+] Found: {full_url} - HTTP Status: {response.status_code}")
        else:
            log_output(f"[-] {full_url} - HTTP Status: 404")
    except requests.exceptions.Timeout:
        pass  # Skip timeout errors
    except requests.exceptions.RequestException as e:
        log_output(f"[!] Error: {full_url} - {str(e)}")
    finally:
        queue.task_done()

def directory_enum(base_url, wordlist):
    queue = Queue()
    threads = []

    with open(wordlist, "r") as file:
        directories = file.readlines()

    log_output(f"\n[*] Directory enumeration started... ({len(directories)} potential directories)")

    animation_thread = threading.Thread(target=animate_scan, args=(queue,))
    animation_thread.start()

    for directory in directories:
        thread = threading.Thread(target=check_directory, args=(base_url, directory, queue))
        thread.start()
        threads.append(thread)
        queue.put(directory)

    for thread in threads:
        thread.join()

    animation_thread.join()

    log_output("\n[*] Enumeration completed.")

def main():
    if len(sys.argv) == 3:
        base_url = sys.argv[1]
        wordlist = sys.argv[2]
    else:
        base_url = input("Enter the target URL (e.g., http://example.com): ").strip()
        wordlist = input("Enter the path to your wordlist file (e.g., common.txt): ").strip()

    log_output(f"\n[*] Target URL: {base_url}")
    log_output(f"[*] Wordlist: {wordlist}")

    directory_enum(base_url, wordlist)

if __name__ == "__main__":
    main()
