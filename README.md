# DDoS Simulator 💣📊

**A full-featured DDoS simulation tool with CLI dashboard, Layer 7 support, IP rotation, and real-time metrics.**

---

## 🧠 Overview

This project started as a basic socket-based DoS tester and has evolved into a robust **DDoS simulation tool** for educational and defensive testing purposes. The tool is designed to test and strengthen the resilience of networks, servers, web applications, and mitigation appliances against denial-of-service scenarios.

It includes support for:
- Tor/VPN/Proxy-based IP rotation
- Layer 7 (HTTP flood) mode
- Custom payloads
- Geo-filtering
- CAPTCHA bypass (placeholder)
- Multithreading
- Real-time metrics dashboard
- CPU overload protection
- Configurable threats, connections, and output logs

---

## ⚠️ Disclaimer

> ❗ Use this tool **only in environments where you have explicit permission** to conduct testing.  
> Unauthorized use may violate local, national, or international laws.  
> The author is not responsible for any misuse or damages.

---

## ⚙️ Features

✅ Multi-threaded concurrent attack simulation  
✅ Proxy / VPN / Tor IP rotation  
✅ Tor control port support for `NEWNYM` IP cycling  
✅ Layer 7 HTTP request flood mode  
✅ Optional payload file support (`--payload-file`)  
✅ CAPTCHA bypass stub (custom logic can be added)  
✅ Geo-filter targeting (stubbed, future-ready)  
✅ Output logs and real-time packet statistics  
✅ JSON reports for audit & metrics  
✅ Dashboard-style CLI with live updates  
✅ `--max-mode` for ultra-high threat testing  
✅ Config persistence and dynamic control (coming soon)

---

## 🚀 Usage

### 🔧 Prerequisites

- Python 3.6+
- (Optional) Tor client running on localhost (for IP rotation)

### 📦 Installation

```bash
git clone https://github.com/sadham001/DDoS.git
cd DDoS
```
## ▶️ Run Example

\`\`\`bash
python ddos.py 192.168.1.100 80 \
  --threads 150 \
  --connections 500 \
  --rotate-ip tor \
  --tor-control \
  --layer7 \
  --payload-file payload.txt \
  --output-log attack.log \
  --report \
  --max-mode
\`\`\`
## ⚙️ Command-Line Options

| Option               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `--threads`          | Number of threads to run simultaneously                                     |
| `--connections`      | Number of connections per thread                                            |
| `--rotate-ip`        | IP rotation method: `proxy`, `vpn`, or `tor`                                |
| `--proxy`            | Proxy server IP or domain                                                   |
| `--proxy-port`       | Proxy server port                                                           |
| `--proxy-username`   | Proxy username (if authentication is needed)                                |
| `--proxy-password`   | Proxy password (if authentication is needed)                                |
| `--tor-control`      | Enable Tor control for identity cycling                                     |
| `--geo-filter`       | Filter targets based on country code (e.g., `--geo-filter US,DE`)           |
| `--layer7`           | Enable Layer 7 HTTP-based attack mode                                       |
| `--payload-file`     | File containing custom payloads to send                                     |
| `--captcha-bypass`   | Simulated CAPTCHA bypass (for testing only)                                 |
| `--output-log`       | Path to log output file                                                     |
| `--report`           | Generate an attack report after execution                                   |
| `--max-mode`         | Use maximum power mode (max connections, threads, and packets)              |
| `--cpu-protect`      | Prevent CPU from hitting 100% usage                                         |
| `--save-config`      | Save current options as a config preset                                     |
| `--help`             | Show help message with all available options                                |
## 📊 Live Metrics & Dashboard

While the tool is running, it provides live, real-time metrics displayed in the terminal. These metrics allow you to monitor the ongoing attack and performance of the system.

### Metrics Displayed:

- **Packets Sent**: The total number of packets sent during the attack.
- **Threads Running**: The number of active threads that are being used to send requests.
- **Active Connections**: The total number of established connections to the target.
- **Attack Status**: Whether the attack is in progress, paused, or completed.
- **Target IP and Port**: Displays the target IP address and port being attacked.
- **Current IP (If rotating)**: Shows the current IP being used if IP rotation is active (via Tor, VPN, or proxy).
- **CPU Usage (%)**: The percentage of CPU usage, especially useful if CPU overload protection (`--cpu-protect`) is enabled.

This real-time dashboard style helps you track attack progress and system performance, providing immediate feedback to help monitor and mitigate issues such as CPU overload or network strain.
## 📑 Reporting

After the simulation completes, the tool can generate a detailed attack report. The report helps in analyzing the performance of the targeted systems and networks during the test.

### Available Reports:

- **Summary Report**: Includes overall stats, attack duration, total packets sent, and system performance (e.g., CPU usage, network utilization).
- **Detailed Attack Logs**: Provides detailed logs of each packet sent, the connections established, and any errors encountered during the simulation.
- **Metrics Breakdown**: A detailed breakdown of metrics such as packets sent per second, threads in operation, and connection success/fail rates.
- **Geo-Analysis**: Displays geo-located IPs involved in the attack, helping to understand the geographic distribution of the attack traffic (if geo-filtering was enabled).

### How to Enable Reporting:

To enable the generation of a report, use the `--report` flag when running the tool.

Example:
```bas
python ddos.py 192.168.1.100 80 --threads 100 --connections 500 --report
```
## 💾 Saving Configuration

The tool allows you to save your current configuration for reuse in future attacks. This is useful for consistent testing or to avoid reconfiguring options each time you run the tool.

### Save Configuration:

To save the current configuration, use the `--save-config` flag. This will save all your current settings to a `.config` file.

Example:
```bash
python ddos.py 192.168.1.100 80 --threads 100 --connections 500 --rotate-ip tor --save-config
```
This will save the configuration to a default file named ddos.config. You can specify a custom file name as well:
```bash
python ddos.py 192.168.1.100 80 --threads 100 --connections 500 --save-config --config my_config.config
```
This will load all the settings stored in my_config.config and apply them to the attack.

This feature helps automate the testing process and ensures you don’t need to manually set options every time you run the tool.
## ⚖️ Legal Disclaimer

This tool is intended for **educational purposes only** and should **only be used in controlled environments** where you have explicit permission to perform testing. Unauthorized use of this tool to attack or disrupt any systems, networks, or websites is **illegal** and may lead to legal consequences.

### By using this tool, you agree to the following:

- You will not use this tool on any systems or networks that you do not have explicit permission to test.
- You understand that DDoS attacks can cause significant disruptions and damage to target systems.
- You take full responsibility for any actions resulting from the use of this tool.

**If you are unsure whether you have permission to test a system, do not use this tool.** Always ensure you have the proper authorization before performing any tests.

### Possible Consequences of Unauthorized Use:

- Legal action from the targeted parties.
- Criminal charges, including potential fines and imprisonment.
- Network and service disruption that may impact users or services.

Always use this tool responsibly and respect the boundaries of ethical hacking and responsible security testing.
## 📝 License

This tool is open-source and distributed under the [GNU General Public License v3.0 (GPL-3.0)](https://www.gnu.org/licenses/gpl-3.0.html).

### GNU General Public License v3.0 (GPL-3.0)

The GPL-3.0 license allows you to freely use, modify, and distribute the software under the following conditions:

- You must provide a copy of the license with any distribution.
- If you modify the software and distribute it, you must release the modified version under the same GPL-3.0 license.
- You may not apply any legal restrictions (such as software patents) that would prevent others from exercising the rights granted by the GPL.

### Disclaimer:

The software is provided "as-is," without any express or implied warranty, including but not limited to warranties of merchantability or fitness for a particular purpose. In no event will the authors be liable for any damages arising from the use of this software.

You can read the full terms of the GNU General Public License v3.0 [here](https://www.gnu.org/licenses/gpl-3.0.html).
