# Malware Detection Tool

This is a simple malware detection tool with a graphical interface, designed to scan script files (e.g., `.py`, `.sh`) for **suspicious keywords**.

It performs **static analysis** by searching for potentially dangerous functions or patterns that are commonly used in malware, such as:

- File system manipulation
- Remote access and sockets
- System command execution
- Encoding and obfuscation

---

## Features

- GUI built with Tkinter (Python)
- Browse and scan any file
- Highlights suspicious keywords with associated risk levels
- Generates a detailed report (`scan_report.txt`)

---

## What is Malware?

**Malware** is short for *Malicious Software*. It refers to any program or code intentionally designed to cause harm to a device, data, or users.

### Common types:
- **Virus**: Infects and replicates inside files
- **Worm**: Spreads through network connections
- **Trojan Horse**: Disguises as a normal program
- **Spyware**: Collects user data secretly
- **Ransomware**: Locks your files and demands payment

---

## Files Included

- `main.py`: Main GUI application
- `scan_report.txt`: Auto-generated after each scan
- `suspicious_keywords.txt`: List of keywords considered risky

---

## Note

This tool is for **educational purposes** and **basic analysis** only. It is not a replacement for antivirus software.
