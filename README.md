# rbnfuzzer

A simple HTTP directory fuzzer written in Python, built to study and explore
Python scripting applied to web application security.

It takes a target URL and a wordlist, sends a request for each path and
reports the HTTP status code of each one, saving the paths that returned
`200 OK` to a JSON file.

## Features

- Directory discovery using custom wordlists
- Configurable connection and read timeouts
- Results exported to JSON
- Error handling for invalid URLs, timeouts and file access

## Requirements

- Python 3.9+
- requests

## Installation

```bash
git clone https://github.com/eltonrbn7/rbnfuzzer.git
cd rbnfuzzer
pip install -r requirements.txt
```

## Usage

```bash
python rbnfuzzer.py -u https://target.com -w path/to/wordlist.txt -o results
```

| Argument                   | Description                           | Required | Default |
| -------------------------- | ------------------------------------- | -------- | ------- |
| `-u`, `--url`          | Target URL                            | Yes      | —      |
| `-w`, `--wordlist`     | Path to the wordlist                  | Yes      | —      |
| `-o`, `--output`       | Output file name (saved as `.json`) | No       | —      |
| `-tc`, `--timeconnect` | Connection timeout in seconds         | No       | 3.0     |
| `-tr`, `--timeread`    | Read timeout in seconds               | No       | 5.0     |

## Example output

```
https://target.com/admin | [ 403 ]
https://target.com/login | [ 200 ]
https://target.com/backup | [ 404 ]
```

`results.json`:

```json
[
  {"path": "https://target.com/login", "status_code": 200}
]
```

## Roadmap

- [ ] Concurrent requests
- [ ] Configurable status code filters
- [ ] Handling of connection errors
- [ ] Automated tests

## Disclaimer

This tool is designed for educational purposes only. Use it only on systems
you own or have explicit permission to test. The author is not responsible
for any misuse.
