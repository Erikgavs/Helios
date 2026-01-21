# ✨ Elendil
> The one who loves the stars

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Elendil** is a server monitoring bot that sends detailed email reports about your system's health, including CPU usage, memory, disk space, temperature, active Docker containers, and network connectivity. Perfect for system administrators who need to keep track of their servers' status.

---

## 📖 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Report Details](#report-details)
- [Automation](#automation)
- [n8n Integration](#n8n-integration)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Author](#author)

---

## ✨ Features

- 📊 **System Monitoring**: CPU, RAM, and disk usage tracking
- 🌡️ **Temperature Monitoring**: Real-time temperature sensors data
- 🐳 **Docker Integration**: Active containers monitoring
- 🌐 **Network Information**: Private and public IP detection
- 📡 **Connectivity Check**: Ping monitoring to custom servers
- 📧 **Email Reports**: Automatic HTML-formatted email reports
- 🤖 **n8n Compatible**: Easy integration with n8n workflows
- 🔌 **REST API**: Simple HTTP endpoint for triggering reports
- ⚡ **Lightweight**: Minimal resource consumption
- 🔧 **Extensible**: Easy to add custom features

---

## 📋 Prerequisites

Before installing Elendil, make sure you have:

- **Python 3.8+** installed
- **Docker** (optional, only if you want Docker monitoring)
- **Gmail account** with App Password enabled
- **Linux/Unix system** (for full functionality)
- **pip** package manager
- **Root/sudo access** (for some system metrics)

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Erikgavs/Elendil.git
cd Elendil

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env with your credentials

# 5. Run the server
python3 main.py

# 6. Trigger a report
curl http://localhost:5000/helios
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Erikgavs/Elendil.git
cd Elendil
```

### 2. Create Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The following packages will be installed:
- `Flask` - Web framework for the API endpoint
- `psutil` - System and process utilities
- `python-dotenv` - Environment variables management
- Other dependencies (see requirements.txt)

---

## 🔐 Configuration

### Setting up the .env File

Create a `.env` file in the project root directory:

```env
REMITENTE=your-email@gmail.com
DESTINATARIO=recipient@gmail.com
PASSWORD=your-google-app-password
```

**Parameters:**
- `REMITENTE`: The Gmail account that will send the reports
- `DESTINATARIO`: The email address that will receive the reports
- `PASSWORD`: Google App Password (NOT your regular Gmail password)

### 🔑 How to Get a Google App Password

1. Go to your Google Account: https://myaccount.google.com/
2. Select **Security** from the left menu
3. Under "Signing in to Google," select **2-Step Verification** (you must enable this first)
4. At the bottom, select **App passwords**
5. Select **Mail** and **Other (Custom name)**
6. Name it "Elendil" or any name you prefer
7. Click **Generate**
8. Copy the 16-character password and paste it in your `.env` file

**Important:** This password is shown only once. Keep it secure!

---

## 📖 Usage

### Starting the Server

#### Foreground Mode (for testing)

```bash
python3 main.py
```

The server will start on `http://0.0.0.0:5000`

#### Background Mode (for production)

```bash
nohup python3 main.py &
```

This runs the server in the background and keeps it running even after closing the terminal.

### Triggering a Report

#### Via HTTP Request

```bash
curl http://localhost:5000/helios
```

#### Via Browser

Simply visit: `http://your-server-ip:5000/helios`

#### Response

```json
{
  "status": "ok",
  "resultado": null
}
```

---

## 📊 Report Details

Each report includes the following information:

### System Metrics
- **CPU Usage**: Current CPU utilization percentage
- **Memory Usage**: RAM consumption in MB
- **Disk Usage**: Disk space used in MB

### Temperature Monitoring
- **Current Temperature**: Real-time sensor reading
- **Maximum Recommended**: Safe operating temperature
- **Critical Temperature**: Threshold for critical warnings

### Network Information
- **Private IP**: Local network IP address (/24 subnet)
- **Public IP**: External IP address (via ifconfig.me)
- **Ping Test**: Connectivity check to `192.168.5.200` (customizable in code)

### Docker Containers
- **Active Containers**: List of running Docker containers
- **Container Details**: Names, status, and ports

---

## 🔄 Automation

### Using Cron (Linux/Unix)

To schedule automatic reports, add a cron job:

```bash
# Edit crontab
crontab -e

# Add these lines for reports at 10:00 and 19:00
0 10 * * * curl http://localhost:5000/helios
0 19 * * * curl http://localhost:5000/helios
```

**Cron Syntax:**
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday = 0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

**Examples:**
```bash
# Every day at 8:00 AM
0 8 * * * curl http://localhost:5000/helios

# Every 6 hours
0 */6 * * * curl http://localhost:5000/helios

# Every Monday at 9:00 AM
0 9 * * 1 curl http://localhost:5000/helios
```

### Using systemd Service (Recommended)

Create a service file `/etc/systemd/system/elendil.service`:

```ini
[Unit]
Description=Elendil Server Monitor
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/Elendil
Environment="PATH=/path/to/Elendil/venv/bin"
ExecStart=/path/to/Elendil/venv/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable elendil
sudo systemctl start elendil
sudo systemctl status elendil
```

---

## 🤖 n8n Integration

Elendil is fully compatible with n8n workflows.

### Setting up n8n Workflow

1. Create a new workflow in n8n
2. Add a **Cron** node for scheduling
3. Add an **HTTP Request** node with these settings:
   - **Method**: GET
   - **URL**: `http://your-server-ip:5000/helios`
4. Activate the workflow

### Example n8n Configuration

```json
{
  "nodes": [
    {
      "name": "Schedule",
      "type": "n8n-nodes-base.cron",
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 10,
              "minute": 0
            },
            {
              "hour": 19,
              "minute": 0
            }
          ]
        }
      }
    },
    {
      "name": "Trigger Elendil",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "http://localhost:5000/helios"
      }
    }
  ]
}
```

---

## 🐛 Troubleshooting

### Email Not Sending

**Error:** `Authentication failed` or `SMTP error`

**Solutions:**
- Verify your Google App Password is correct
- Ensure 2-Step Verification is enabled on your Google account
- Check if "Less secure app access" is disabled (should be disabled, use App Password)
- Verify your `.env` file is in the correct location

### Docker Information Not Showing

**Error:** `docker: command not found`

**Solutions:**
- Install Docker: `sudo apt-get install docker.io`
- Add your user to the docker group: `sudo usermod -aG docker $USER`
- Restart your terminal session
- If Docker is not needed, the script will continue without Docker info

### Temperature Not Available

**Error:** Temperature shows "No disponible"

**Solutions:**
- Install `lm-sensors`: `sudo apt-get install lm-sensors`
- Detect sensors: `sudo sensors-detect`
- Verify sensors are working: `sensors`
- Some virtual machines don't have temperature sensors (this is normal)

### Port Already in Use

**Error:** `Address already in use`

**Solutions:**
```bash
# Find process using port 5000
sudo lsof -i :5000

# Kill the process
sudo kill -9 <PID>

# Or change the port in main.py
app.run(host="0.0.0.0", port=5001)
```

### Permission Denied Errors

**Error:** `Permission denied` when accessing system info

**Solutions:**
- Run with sudo: `sudo python3 main.py`
- Or add specific permissions for psutil access

---

## 🔐 Security

### Best Practices

1. **Never commit your `.env` file** to version control
2. **Add `.env` to `.gitignore`**:
   ```bash
   echo ".env" >> .gitignore
   ```
3. **Use strong Google App Passwords** (16 characters)
4. **Regularly rotate credentials**
5. **Restrict Flask to localhost** if not using n8n:
   ```python
   app.run(host="127.0.0.1", port=5000)
   ```
6. **Use a firewall** to protect port 5000
7. **Consider using HTTPS** for production environments
8. **Keep dependencies updated**:
   ```bash
   pip list --outdated
   pip install --upgrade -r requirements.txt
   ```

### Network Security

If exposing the endpoint to the internet, consider:
- Using a reverse proxy (nginx, Apache)
- Implementing authentication (API keys, OAuth)
- Setting up rate limiting
- Using VPN or IP whitelisting

---

## 🛠️ Customization

### Changing the Ping Target

Edit `reporter.py` line 25:

```python
ping_server = subprocess.run(["ping", "-c", "1", "YOUR-IP-HERE"], text=True, capture_output=True)
```

### Changing Report Schedule

Modify the cron job or n8n workflow to match your preferred schedule.

### Adding Custom Metrics

Add your custom commands in `reporter.py`:

```python
# Example: Check if a service is running
service_status = subprocess.run(["systemctl", "status", "nginx"], text=True, capture_output=True)

# Add to the info string
info = f"""
...
Service Status
{service_status.stdout}
"""
```

### Changing Email Subject

Edit `reporter.py` line 75:

```python
mensaje["Subject"] = "Your Custom Subject Here"
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🧙‍♂️ Author

**Erik Gavs**
- GitHub: [@Erikgavs](https://github.com/Erikgavs)
- Project Link: [https://github.com/Erikgavs/Elendil](https://github.com/Erikgavs/Elendil)

---

## 🌟 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- System monitoring via [psutil](https://github.com/giampaolo/psutil)
- Inspired by Tolkien's legendarium

---

## 📝 Changelog

### Version 1.0.0 (Current)
- Initial release
- Basic system monitoring
- Email reporting
- Docker integration
- n8n compatibility

---

**Made with ❤️ for system administrators**
