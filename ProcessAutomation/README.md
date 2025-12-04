# Process Automation Tool – Automated Running Process Logger with Email Alerts



This Python automation tool periodically scans all system processes, records important process information (such as PID, name, username, and memory usage), generates a timestamped log file, and automatically sends the log file to a registered email address.  
The tool uses a scheduler to run automatically every few seconds.

---

## ✨ Features

- 🧠 Process Scanning using the `psutil` module  
- 📋 Logs details: PID, Process Name, Username, Memory Usage  
- ⏱️ Automatically runs every 1 second using the `schedule` module  
- 📝 Creates timestamped log files  
- 📧 Sends the log file as an email attachment  
- 💻 Works on Windows, Linux, and macOS  

---

## 🛠️ How the Script Works

### 1️⃣ ProcessScan()
Collects details of every running process and returns a list of dictionaries.

### 2️⃣ CreateLog(FolderName)
Creates folder (if not present), generates timestamped log file, writes process details, then emails the log.

### 3️⃣ SendMail(logFile)
Sends the generated log file via Gmail SMTP using an App Password.

### 4️⃣ main()
Handles arguments, shows help/usage, and schedules the log creation task.

---

## 🚀 Usage

```bash
python ProcessAutomation.py <FolderName>
```

Example:
```bash
python ProcessAutomation.py Logs
```

Help:
```bash
python ProcessAutomation.py --h
```

Usage:
```bash
python ProcessAutomation.py --u
```

---

## 🧩 Email Setup

Update inside SendMail():

```
SenderMail = "yourmail@gmail.com"
SenderPass = "your-app-password"
reciverMail = "targetmail@gmail.com"
```

---

## 📦 Requirements

```
pip install psutil schedule
```

---

## 📂 Example Log File

```
================================================================================
    Marvellous InfoSystem Process log
    Log File is Created at : Tue_Jun_15_12_30_55_2025
================================================================================

{'pid': 1200, 'name': 'python3', 'username': 'mangesh', 'vms': 12.5}

{'pid': 800, 'name': 'chrome', 'username': 'mangesh', 'vms': 230.7}

================================================================================
```


---

## 👨‍💻 Author

**Mangesh Ashok Bedre**  

