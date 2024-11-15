Sure! Here's your directory enumeration tool documentation converted to Markdown format:

```markdown
# Directory Enumeration Tool

## Overview
This tool performs directory enumeration on a given target URL using a provided wordlist. It checks for the existence of directories or files by sending HTTP requests to the target server. If a directory or file is found, the tool logs the result and outputs the found URL along with its HTTP status. It also includes an animated spinner to indicate progress during the scan.

## Features
- **Multi-threaded scanning**: It spawns multiple threads to speed up the scanning process.
- **Dynamic animation**: An animated spinner is displayed while the directories are being scanned.
- **Logging**: The results are logged to both the console and a log file (`directory_scan_results.log`).
- **Customizable wordlist**: You can specify a custom wordlist file for the directory enumeration.

## Requirements
- Python 3.x
- requests library

You can install the necessary library using pip:
```bash
pip install requests
```

## Usage

### Command Line
You can run the script by providing two arguments: the base URL and the path to the wordlist file.
```bash
python main.py <base_url> <wordlist>
```
For example:
```bash
python main.py http://example.com common.txt
```

### Interactive Mode
If you don't want to pass the arguments via the command line, the script will prompt you for the target URL and wordlist file:
```bash
python main.py
```

## Output
The script will print the results to the console. The results are also logged to a file named `directory_scan_results.log`.

### Example output:
```
[*] Directory enumeration started... (200 potential directories)
Scanning |
[+] Found: http://example.com/admin - HTTP Status: 200
[-] http://example.com/uploads - HTTP Status: 404
[+] Found: http://example.com/config - HTTP Status: 200
[*] Enumeration completed.
```

### Example Log File
```
[*] Directory enumeration started... (200 potential directories)
[+] Found: http://example.com/admin - HTTP Status: 200
[-] http://example.com/uploads - HTTP Status: 404
[+] Found: http://example.com/config - HTTP Status: 200
[*] Enumeration completed.
```

## How it Works
1. **Input**: You provide a target URL and a wordlist (e.g., `common.txt`) that contains a list of possible directories (one per line).

2. **Multi-threaded Scanning**: The script creates multiple threads (one for each directory in the wordlist) to send HTTP requests concurrently. This speeds up the scanning process.

3. **Directory Check**: For each directory in the wordlist, the script sends an HTTP GET request to the URL formed by appending the directory to the base URL. If the server responds with a status code other than 404, the directory is considered to be valid and is logged.

4. **Progress Animation**: While the directories are being checked, a dynamic spinner (`|`, `/`, `-`, `\`) is displayed to show that the scan is in progress.

5. **Logging**: Each found directory (with status code) is logged to both the console and the log file `directory_scan_results.log`. Errors (e.g., timeouts) are also logged.

6. **Completion**: Once all directories are checked, the script will output `[*] Enumeration completed.`

## Example Usage
Start the script by providing a target URL and a wordlist file:
```bash
python main.py http://example.com common.txt
```
Results will be shown in the terminal, and all found directories will be logged to `directory_scan_results.log`.

## Code Breakdown

### Main Components
- **log_output**: Logs messages to both the console and a log file (`directory_scan_results.log`).
- **animate_scan**: Displays a dynamic animation in the terminal while the scan is in progress. The spinner (`|`, `/`, `-`, `\`) rotates to indicate activity.
- **check_directory**: For each directory in the wordlist, this function sends a GET request to the full URL (base URL + directory). If the server responds with a status other than 404, it logs the URL as a found directory.
- **directory_enum**: The main function that orchestrates the directory enumeration. It spawns multiple threads to check the directories concurrently, improving performance. It also starts the animation thread to show the progress.
- **main**: The entry point for the script. It processes command-line arguments and starts the directory enumeration.

## Limitations
- **Timeouts**: The script doesn't handle timeouts well. If the server takes too long to respond, it will simply skip the directory and continue.
- **Rate Limiting**: The script may be blocked by the target server if it's too aggressive or if the server enforces rate limiting.
- **Logging**: The log file can grow large for large wordlists. Make sure to monitor the size if you're scanning large ranges.

## Enhancements
- **Rate Limiting**: Implement rate limiting to avoid overwhelming the target server.
- **Timeout Handling**: Improve timeout management, possibly adding retries for timeouts.
- **Custom HTTP Headers**: Add functionality to specify custom HTTP headers (e.g., User-Agent) for requests.
- **Performance Optimization**: Implement a thread pool or use asynchronous requests for better performance with many directories.
```

