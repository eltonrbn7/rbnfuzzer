import argparse
import requests
import sys
import json

def banner() -> None:
    print(r"""
          _            __                        
     _ __| |__  _ __  / _|_   _ ___________ _ __ 
    | '__| '_ \| '_ \| |_| | | |_  /_  / _ \ '__|
    | |  | |_) | | | |  _| |_| |/ / / /  __/ |   
    |_|  |_.__/|_| |_|_|  \__,_/___/___\___|_|   
    
    rbnfuzzer v0.1  |  by elton ribeiro
    HTTP directory fuzzer
    """)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='Fuzzer',
                                    description='Fuzzing for directories list',
                                    epilog='Help you',
                                    usage='Example: python rbnfuzzer.py -u https://target.com -w path/wordlist')

    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-w', '--wordlist', required=True)
    parser.add_argument('-o', '--output', required=False)
    parser.add_argument('-tc', '--timeconnect', required=False, type=float, default=3.0)
    parser.add_argument('-tr', '--timeread', required=False, type=float, default=5.0)

    args: argparse.Namespace = parser.parse_args()
    if args.timeconnect <= 0 or args.timeread <= 0:
        print('Timeout values must be greater than 0')
        sys.exit(1)

    return args


def read_wordlist(path: str) -> list[str]:
    words=[]
    
    try:
        with open(path,"r") as file:
            for line in file:
                words.append(line.strip('\n'))
        return words

    except FileNotFoundError:
        print('Cannot find this file, try again')
    except PermissionError:
        print('You dont have permission to read this file')

    return words


def probe(url: str, wdl: list[str], timeout: tuple) -> list[dict]:

    url = url.rstrip('/')
    paths = [url + "/" + word for word in wdl]

    results = [] 

    for path in paths:

        try:
            req = requests.get(path, timeout=timeout)
            status_code = req.status_code
            print(f'{path}  |  [ {status_code} ]')
            if status_code == 200:
                results.append(
                    {
                        'path': path,
                        'status_code': status_code
                    }
                )

        except requests.exceptions.MissingSchema:
            print(f'Invalid URL {path}: No scheme supplied. Perhaps you meant https://{path}')
        except requests.exceptions.ConnectTimeout:
            print(f'Connect Timeout Error: {path}')
        except requests.exceptions.ReadTimeout:
            print(f'Read Timeout Error: {path}')

    return results


def save_output(results: list[dict], output: str) -> None:
    if output:
        with open(output+".json", 'w') as o_file:
                json.dump(results, o_file)


if __name__ == "__main__":
    banner()
    args = get_args()
    words = read_wordlist(path=args.wordlist)
    results = probe(url=args.url, wdl=words, timeout=(args.timeconnect, args.timeread))
    save_output(results, args.output)
