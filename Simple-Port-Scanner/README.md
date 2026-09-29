# Simple Vulnerability / Port Scanner

## Project Description

This project is a beginner-level cybersecurity tool developed
using Python.

The scanner checks common TCP ports on the local computer and
identifies whether they are open or closed.

## Objective

- Identify open TCP ports
- Identify commonly associated services
- Generate a basic security report
- Understand basic network scanning concepts

## Technologies Used

- Python
- Socket programming

## Features

- Scans common TCP ports
- Displays open and closed ports
- Identifies common services
- Generates a simple scan report
- Uses connection timeouts

## How to Run

Run:

python port_scanner.py

The program scans the local computer
(127.0.0.1).

## Example Ports

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |

## Learning Outcomes

- Understand TCP ports
- Understand client-server connections
- Learn basic socket programming
- Understand basic port scanning
- Interpret basic scan results

## Safety

This project is intended for educational purposes.

The provided version scans only the local computer.
Do not scan systems or networks without explicit authorization.