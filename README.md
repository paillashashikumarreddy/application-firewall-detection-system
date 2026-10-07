# 🔐 Application Firewall Detection System

An **Application-Level Firewall Detection System** designed to identify and block potentially malicious web requests, with a focus on detecting common application-layer attacks such as **Cross-Site Scripting (XSS)** and **SQL Injection**.

The system maintains application firewall logs containing timestamps, attack types, source IP information, and the URLs associated with blocked requests. The recorded logs demonstrate successful detection and blocking of multiple malicious request patterns.

---

## 📌 Project Overview

Web applications are frequently targeted by application-layer attacks such as SQL Injection and Cross-Site Scripting. These attacks can manipulate application inputs and potentially compromise the security or integrity of web applications.

This project focuses on detecting suspicious request patterns and recording blocked attacks through an application firewall logging mechanism.

The system's logs provide evidence of detected attacks, including:

* XSS attacks
* SQL Injection attempts
* Source IP information
* Requested URLs
* Date and time of detected activity
* Blocked request status

---

## 🎯 Objectives

The main objectives of this project are:

* Detect suspicious application-level requests.
* Identify common attack patterns such as XSS and SQL Injection.
* Block detected malicious requests.
* Record security events for monitoring and analysis.
* Maintain logs containing attack details and timestamps.
* Provide a foundation for improving web application security.

---

## 🛡️ Attacks Detected

### 1. Cross-Site Scripting (XSS)

The system identifies requests containing XSS-related input patterns.

Example recorded event:

```text
XSS Attack BLOCKED
IP: 127.0.0.1
URL: http://127.0.0.1:5000/login?user=<script>alert(1)</script>
```

The project logs contain multiple XSS detection events showing that such requests were successfully marked as **BLOCKED**.

### 2. SQL Injection

The system also records SQL Injection attempts containing suspicious SQL input patterns.

Example:

```text
SQL Injection BLOCKED
IP: 127.0.0.1
URL: http://127.0.0.1:5000/login?user='%20or%201=1
```

The logs contain multiple SQL Injection events that were identified and recorded as **BLOCKED**.

---

## ⚙️ Key Features

* 🔍 **Attack Detection** – Identifies suspicious application-level request patterns.
* 🚫 **Attack Blocking** – Detected malicious requests are recorded with a blocked status.
* 📝 **Security Logging** – Maintains logs of detected security events.
* ⏱️ **Timestamp Recording** – Each event includes the date and time of detection.
* 🌐 **URL Tracking** – Records the URL associated with the suspicious request.
* 🖥️ **IP Tracking** – Records available source IP information.
* 🛡️ **XSS Detection** – Detects and blocks recorded XSS patterns.
* 💉 **SQL Injection Detection** – Detects and blocks recorded SQL Injection patterns.

---

## 📊 Project Results

The provided firewall log demonstrates that the system detected and blocked repeated attempts involving **XSS and SQL Injection**.

The recorded events include activity against local application endpoints such as:

```text
http://127.0.0.1:5000/login
http://localhost/login
http://localhost:5000/test
```

The logs show repeated blocked XSS and SQL Injection attempts across multiple dates.

A particularly useful test case recorded in the logs is:

```text
SQL Injection BLOCKED
IP: 127.0.0.1
URL: http://localhost:5000/test?id=1'%20or%20'1'='1
```

This demonstrates that the system was tested against an SQL Injection pattern on a local test endpoint.

---

## 📋 Sample Firewall Log

The project generates security records in a format similar to:

```text
DATE/TIME | ATTACK TYPE | IP | URL
```

Example:

```text
2026-03-30 06:13:58 | SQL Injection BLOCKED | IP: 127.0.0.1 |
URL: http://127.0.0.1:5000/login?user='%20or%201=1

2026-03-30 06:14:10 | XSS Attack BLOCKED | IP: 127.0.0.1 |
URL: http://127.0.0.1:5000/login?user=<script>alert(1)</script>
```

These examples are taken from the project's actual firewall logs.

---

## 🏗️ System Workflow

```text
        Incoming Web Request
                │
                ▼
       ┌───────────────────┐
       │ Request Inspection│
       └─────────┬─────────┘
                 │
                 ▼
       ┌───────────────────┐
       │ Pattern Detection │
       └─────────┬─────────┘
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
     Suspicious       Normal
       Request         Request
          │             │
          ▼             ▼
       BLOCKED         Allow
          │
          ▼
   Security Event Log
          │
          ▼
  Timestamp / IP / URL /
     Attack Type
```

---

## 🔎 Logging and Monitoring

The firewall log records security events using information such as:

| Information | Description                           |
| ----------- | ------------------------------------- |
| Timestamp   | Date and time of the event            |
| Attack Type | Type of detected attack               |
| IP Address  | Source IP when available              |
| URL         | Requested application URL             |
| Status      | Indicates that the attack was blocked |

The supplied logs contain both `127.0.0.1` and `None` for IP information, so IP availability depends on the particular test request.

---

## 🧪 Testing

The system was tested using application requests containing patterns associated with:

* Cross-Site Scripting
* SQL Injection

The recorded results show that these requests were classified as **BLOCKED**.

Examples of repeated blocked events can be seen throughout the firewall log.

---

## 📁 Suggested Repository Structure

```text
application-firewall-detection-system/
│
├── README.md
│
├── src/
│   └── application_firewall/
│
├── logs/
│   └── firewall.log
│
├── screenshots/
│
├── documentation/
│
├── requirements.txt
│
└── .gitignore
```

> Update the folder names above to match your actual project files.

---

## 💻 Technologies

Based on the available project evidence, the system was tested using local web application endpoints such as `localhost` and `127.0.0.1`.

If your implementation uses additional technologies such as **Python, Flask, HTML, CSS, JavaScript, or SQLite**, add only the technologies that are actually present in your source code.

---

## 🚀 Future Enhancements

Potential improvements for a future version include:

* Add a web-based security monitoring dashboard.
* Provide attack statistics and visualizations.
* Add additional application attack detection rules.
* Improve IP and request tracking.
* Add configurable detection rules.
* Implement alert notifications for critical events.
* Add automated security reports.
* Improve log management and filtering.

---

## ⚠️ Disclaimer

This project is intended for **educational and authorized security testing purposes only**.

Testing should be performed only against applications and systems for which you have permission.

---

## 👨‍💻 Author

**Pailla Shashi Kumar Reddy**

Computer Science & Engineering Student
Hyderabad, India

### Areas of Interest

* Software Development
* Cybersecurity
* Web Development
* Python
* Network Security
* Application Security

---

## ⭐ Project Highlights

* Application-level security monitoring
* XSS detection and blocking
* SQL Injection detection and blocking
* Security event logging
* Timestamp and URL tracking
* Local web application security testing

---

## 📌 Project Status

**Academic Project — Completed Prototype**

The current project demonstrates application-level detection and logging of selected malicious request patterns, including XSS and SQL Injection, using local test endpoints.
