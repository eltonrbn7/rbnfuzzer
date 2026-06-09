import argparse
import requests

def get_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog='Fuzzer',
                                                            description='Fuzzing for directories list',
                                                            epilog='Help you',
                                                            usage='Example: python rbnfuzzer.py -u https://target.com -w path/wordlist')

    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-w', '--wordlist', required=True)

    args: argparse.Namespace = parser.parse_args()

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


def probe(url: str, wdl: str) -> None:

    url = url.rstrip('/')
    paths = [url + "/" + word for word in wdl]


    for path in paths:
        try:
            req = requests.get(path)
            status_code = req.status_code
            print(f'Route: {path}  -  Status Code: {status_code}')

        except requests.exceptions.MissingSchema:
            print(f'Invalid URL {path}: No scheme supplied. Perhaps you meant https://{path}')


if __name__ == "__main__":
    args = get_args()
    words = read_wordlist(path=args.wordlist)
    probehttp = probe(url=args.url, wdl=words)