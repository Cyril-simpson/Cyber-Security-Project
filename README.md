🔐 Cybersecurity Internship Projects

GlowLogics Cybersecurity Internship

This repository contains four cybersecurity projects developed as part of my online cybersecurity internship at GlowLogics.

The projects demonstrate fundamental concepts of cybersecurity, including password security, cryptography, phishing awareness, and network security.

📌 Projects

No.                    Project                              Technology

1               Password Strength Analyzer                    Python

2          Data Encryption and Decryption Tool          Python, Cryptography

3          Phishing Email Awareness Simulator                  Python

4          Simple Vulnerability / Port Scanner             Python, Socket

🔑 1. Password Strength Analyzer

📖 Description

The Password Strength Analyzer is a Python-based cybersecurity tool that checks the strength of a password using different security criteria.

The program analyzes the password and provides a strength score along with suggestions for improvement.

🎯 Objectives

Check password length

Check uppercase letters

Check lowercase letters

Check numbers

Check special characters

Calculate password strength

Provide security recommendations

⚙️ Features

Password validation

Character type checking

Strength calculation

Security suggestions

Simple command-line interface

🛠️ Technologies Used

Python

Regular Expressions

▶️ How to Run

python password_analyzer.py

📊 Example


     PASSWORD STRENGTH ANALYZER

Enter your password: MyPassword@123

Password Strength: Strong
Score: 5 / 5

Excellent! Your password satisfies all basic checks.

🎓 Learning Outcome

This project provides an understanding of password security, input validation, and basic cybersecurity practices.

⚠️ For demonstration purposes, use only fictional/test passwords. Never enter real passwords.

🔐 2. Data Encryption and Decryption Tool

📖 Description

The Data Encryption and Decryption Tool is a Python application that demonstrates how data can be protected using encryption algorithms.

The project demonstrates both AES symmetric encryption and RSA asymmetric encryption.

🎯 Objectives

Understand encryption and decryption

Implement AES encryption

Implement RSA encryption

Understand symmetric encryption

Understand asymmetric encryption

Demonstrate data confidentiality

⚙️ Features

AES-256 encryption

AES decryption

RSA-2048 encryption

RSA decryption

Automatic key generation

Base64 encoded encrypted output

🛠️ Technologies Used

Python

Cryptography Library

AES

RSA

OAEP

SHA-256

📦 Installation

Install the required library:

pip install cryptography

Or:

pip install -r requirements.txt

▶️ How to Run

python encryption_tool.py

The program provides two options:

1. AES
2. RSA

The user can select an algorithm and enter a test message.

🔄 AES Encryption

AES is a symmetric encryption algorithm.

The same secret key is used for encryption and decryption.

Original Message
       ↓
    AES Key
       ↓
   Encryption
       ↓
Encrypted Message
       ↓
    AES Key
       ↓
   Decryption
       ↓
Original Message

🔄 RSA Encryption

RSA is an asymmetric encryption algorithm.

It uses two keys:

Public Key

Private Key

Original Message
       ↓
   Public Key
       ↓
   Encryption
       ↓
Encrypted Message
       ↓
  Private Key
       ↓
   Decryption
       ↓
Original Message

🎓 Learning Outcome

This project provides an understanding of cryptography, encryption keys, symmetric encryption, asymmetric encryption, and data confidentiality.

⚠️ This project is an educational demonstration and should not be considered a replacement for professionally designed cryptographic systems.

🎣 3. Phishing Email Awareness Simulator

📖 Description

The Phishing Email Awareness Simulator is an educational cybersecurity project that helps users identify common signs of phishing emails.

The program displays fictional email scenarios and asks the user to identify whether an email is phishing or safe.

🎯 Objectives

Understand phishing attacks

Identify suspicious email characteristics

Understand social engineering

Improve phishing awareness

Provide immediate feedback

⚙️ Features

Fictional email examples

Phishing identification

Safe email identification

Warning-sign explanations

Score calculation

Cybersecurity awareness feedback

🛠️ Technologies Used

Python

Random Module

▶️ How to Run

python phishing_simulator.py

The program displays an email and provides two options:

1. Phishing
2. Safe

The user selects an answer and receives an explanation.

📊 Example


EMAIL


From: security@example.invalid

Subject: URGENT: Your account will be closed!

Is this email:
1. Phishing
2. Safe

Your answer: 1

Correct!

Why?

- Uses urgent language.
- Requests immediate action.
- Uses a fictional sender domain.

🚨 Common Phishing Warning Signs

The project teaches users to identify:

Urgent or threatening messages

Unexpected requests

Requests for sensitive information

Suspicious sender addresses

Unexpected prizes or offers

Pressure to act immediately

🎓 Learning Outcome

This project helps users understand phishing, social engineering, suspicious email patterns, and cybersecurity awareness.

🛡️ Safety

This project is an educational simulation.

It does not:

Send real phishing emails

Collect passwords

Collect credentials

Target real users

Use malicious links

🔎 4. Simple Vulnerability / Port Scanner

📖 Description

The Simple Port Scanner is a beginner-level cybersecurity tool developed using Python.

It checks common TCP ports on the local computer and identifies whether they are open or closed.

🎯 Objectives

Understand TCP ports

Identify open ports

Identify closed ports

Understand basic network scanning

Learn socket programming

Generate a basic security report

⚙️ Features

Scans common TCP ports

Detects open ports

Detects closed ports

Identifies common services

Uses connection timeouts

Generates a scan report

🛠️ Technologies Used

Python

Socket Programming

Socket Module

▶️ How to Run

python port_scanner.py

The program scans the local computer:

127.0.0.1

📋 Common Ports

Port          Service

21              FTP

22              SSH

23              Telnet

25              SMTP

53              DNS

80              HTTP

110             POP3

143             IMAP

443             HTTPS

445             SMB

3306            MySQL

3389            RDP

📊 Example Output

             SIMPLE PORT SCANNER

Target: 127.0.0.1

Scanning common ports...

[CLOSED] Port 21    - FTP
[CLOSED] Port 22    - SSH
[OPEN]   Port 80    - HTTP
[CLOSED] Port 443   - HTTPS


                 SCAN REPORT


Target: 127.0.0.1
Open ports: 1

Open ports detected:
- Port 80: HTTP

The actual results depend on the services running on the computer.

🎓 Learning Outcome

This project provides an understanding of TCP ports, network services, socket programming, client-server communication, and basic network security.

🛡️ Safety

The provided project is designed to scan the local computer only.

Do not scan computers, servers, or networks that you do not own or have explicit permission to test.
