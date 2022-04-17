# Download youtube videos



try:
    from pytube import YouTube
    from pytube.exceptions import RegexMatchError
    import os
    import argparse
    from colorama import Fore, init
    import time
except AttributeError:
    print(f'[-] Some modules are missing')
    print(f'[-] Please install them using pip install -r requirements.txt')


# Colors
init()

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
GRAY = Fore.LIGHTBLACK_EX

# Dowload youtube videos
def download_url(url):
    try: 
        print(f'{G}[+] Fetching the video...')
        yt = YouTube(url)
        print(f'{G}[+] Downloading...')
        try:
            yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first().download(path)
        except TypeError:
            print(f'{R}[-] Please provide a path.')
    except RegexMatchError:
        print(f"{R}[-] Can't find the video of the given URL.")
        exit()

# Description of the URL
def description(url):
    try:
        yt = YouTube(url)
        # The title of the video.
        print(f'{G}[+] Title: {Y}{yt.title}')
        # The views of the video.
        print(f'{G}[+] Views: {Y}{yt.views}')
        # The description of the video.
        print(f'{G}[+] Description: {Y}\n{yt.description}\n')
        # The uploader of the video.
        print(f'{G}[+] Channel: {Y}{yt.author}')        
        # Checks if age restricted.
        print(f'{G}[+] Age restricted: {Y}{yt.age_restricted}')
        # Checks the size of the file.
        print(f'{G}[+] File size: {Y}{yt.filesize}')
    except AttributeError:
        print(f'{R}[-] Some info cannot be found')
        





# Arguments
parser = argparse.ArgumentParser(description='A CLI YouTube video downloader')
# URL input
parser.add_argument('-l', '--url', required=True, help='The URL of the file (YouTube)')
# The format.
parser.add_argument('-f', '--format', default='mp4', help='The format of the file. Ex. mp4 or mp3. Deafult (mp4)' )
# Show the streams of the video
parser.add_argument('-d', '--choose-stream', help='Show available streams', action='store_true')
# Path argument.
parser.add_argument('-p', '--path', help='The path to save the file. Default (current directory)', default=os.getcwd())

args = parser.parse_args()

url = args.url
path = args.path
extension = args.format



if __name__ == '__main__':
    if args.choose_stream:
        yt = YouTube(url)
        # Show the available streams.
        for stream in yt.streams.all():
            print(f'{GRAY}{stream}')
        print(f'{GRAY}[+] Type back to exit')
        tag = input(f'{G}[+] Choose the stream tag: ')
        stream = yt.streams.get_by_itag(tag)
        # To exit.
        if tag == 'back':
            exit()
        # Else download the video.
        # Download the video provided by the tag.
        else:
            try:
                start = time.perf_counter()
                print(f'{G}[+] Fetching stream...')
                stream.download(path)
                print(f'{G}[+] Downloading...')
                print(f'{G}[+] Download completed!')
                description(url)
                end = time.perf_counter()
                print(f'{G}[+] Downloaded in {end-start} seconds')
                exit()
            except AttributeError:
                print(f'{R}[-] Stream not available')
                exit()
    start = time.perf_counter()
    download_url(url)
    description(url)
    print(f'{G}[+] Download completed!')
    end = time.perf_counter()
    # Show the time it took to download the video.
    print(f'{G}[+] Downloaded in {end-start} seconds')
