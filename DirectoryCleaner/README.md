# Directory Cleaner – Automated Duplicate File Remover with Email Alerts

This Python automation tool scans a directory, identifies duplicate files using **MD5 checksums**, deletes duplicates, generates a **detailed log file**, and automatically **emails the log file** to a registered email address.  
The script also supports **automatic scheduling** and runs every **1 minute**.

## ✨ Features
- Detects duplicate files using MD5 checksum  
- Automatically deletes duplicates (keeps one original copy)  
- Creates timestamped log files  
- Emails log file as an attachment  
- Fully automated using `schedule`  
- Works on Windows, Linux, macOS  

## 🛠️ How It Works

### 1. CalculateChksum()
Computes MD5 checksum.

### 2. FindDuplicate()
Scans directory and groups duplicates.

### 3. DeleteDuplicate()
Deletes duplicates and logs results.

### 4. SendMail()
Emails log file.

### 5. Scheduler
Runs every 1 minute.

## 🚀 Usage
```bash
python DirectoryCleaner.py <DirectoryPath>
```

Help:
```bash
python DirectoryCleaner.py --h
```

Usage:
```bash
python DirectoryCleaner.py --u
```

## 📨 Email Configuration
Update inside `SendMail()`:
```
SenderMail = "yourmail@gmail.com"
SenderPass = "your-app-password"
reciverMail = "targetmail@gmail.com"
MailServer = "smtp.gmail.com"
```

## 📝 Log File Example
```
------------------------------------------------------
This is the log file of Marvellous Automation Script
This is Directory Cleaner Script
------------------------------------------------------

Deleted File : /home/user/Downloads/file_copy.png
Deleted File : /home/user/Downloads/file_duplicate.docx

Total Deleted file : 2

------------------------------------------------------
This is created at
Tue Nov 18 13:50:33 2025
------------------------------------------------------

```

## 📦 Requirements
```
pip install schedule
```

## 👨‍💻 Author
**Mangesh Ashok Bedre**
