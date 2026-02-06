# CamPhish

**CamPhish** is a lightweight and effective phishing tool designed to capture photos and videos from a target's front and back cameras using a generated link. It utilizes PHP for the web server and ngrok for tunneling to make the phishing page accessible over the internet.

> **⚠️ DISCLAIMER:**  
> This tool is for **EDUCATIONAL PURPOSES ONLY**.  
> The author and contributors are not responsible for any misuse of this tool.  
> Do not use this tool on systems or devices you do not have permission to test.  
> Hacking without permission is illegal.

---

## 🚀 Features

- 📸 **Take Photos**: Captures images from both Front and Back cameras.
- 📹 **Record Video**: Records short video clips from Front and Back cameras.
- 🌐 **Tunneling**: Auto-generates a public URL using **ngrok**.
- ⚙️ **Customizable**: Modify recording duration and photo counts via `main.py` or interactive prompts.
- 📂 **Auto-Save**: Saves captured media directly to the `uploads/` directory.

---

## 📋 Prerequisites

Before running the tool, ensure you have the following installed:

1.  **Python 3**
2.  **PHP**
3.  **Ngrok** (with a valid authtoken)
4.  **Git**

### 📦 Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/c2-tlhah/CamPhish.git
cd CamPhish
```

#### 2. Install Dependencies
**Linux / Termux / macOS**:
```bash
pip3 install -r requirements.txt
# If requirements.txt is missing, install manually:
pip3 install watchdog colorama
```
*Note: On some Linux distributions, you may need to use `pip3 install --break-system-packages ...` if you are not in a virtual environment.*

#### 3. Install System Packages

**Debian/Ubuntu/Kali Linux**:
```bash
sudo apt update
sudo apt install php python3 python3-pip git -y
sudo snap install ngrok  # Or download from ngrok.com
```

**Termux**:
```bash
pkg update
pkg install php python git -y
```

**Windows**:
- Download and install [Python](https://www.python.org/downloads/)
- Download and install [PHP](https://www.php.net/downloads.php) (Add to PATH)
- Download [Ngrok](https://ngrok.com/download)

---

## 🔧 Configuration (Important!)

You need an **Ngrok Authtoken** to use the tunneling feature.

1.  Go to [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) and copy your authtoken.
2.  Add it to the tool:
    ```bash
    ngrok config add-authtoken <YOUR_TOKEN_HERE>
    ```
    *Alternatively, the script will ask for it on first run.*

---

## 🎮 Usage

Run the script using Python:

```bash
python3 main.py
```

### Steps:
1.  The tool will launch and ask if you want to configure `index.html` settings (Photo count, video duration).
2.  It will start a local PHP server.
3.  It will start an Ngrok tunnel and display a **Public URL** (e.g., `https://abcd-1234.ngrok-free.app`).
4.  **Send this URL to the target.**
5.  When the target opens the link and allows camera permissions, photos/videos will be captured.
6.  Captured files will appear in the `uploads/` folder and you will be notified in the terminal.

---

## ❓ Troubleshooting

- **"No ngrok URL found"**:
    - Ensure your Ngrok token is valid.
    - Check your internet connection.
    - If you are in a restricted region, use a VPN.
- **"php: command not found"**:
    - Ensure PHP is installed and added to your system PATH.
- **"ModuleNotFoundError"**:
    - Run `pip3 install watchdog colorama`.

---

## 📜 Credits
- Developed by **c2-tlhah**
