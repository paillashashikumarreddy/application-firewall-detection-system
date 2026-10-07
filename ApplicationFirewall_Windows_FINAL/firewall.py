import re, time
from flask import request, abort
from rules import SQL_PATTERNS, XSS_PATTERNS
from datetime import datetime
from urllib.parse import unquote   # 🔥 IMPORTANT FIX

# 🔥 Dashboard logs
logs = []

RATE = {}
MAX_REQ = 10
WINDOW = 60


def log_attack(ip, attack, url):
    log_entry = f"{datetime.now()} | {attack} BLOCKED | IP: {ip} | URL: {url}"
    
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_entry + "\n")
    
    logs.append(log_entry)


def log_allowed(ip, url):
    log_entry = f"{datetime.now()} | ALLOWED | IP: {ip} | URL: {url}"
    logs.append(log_entry)


def detect(patterns, payload):
    for p in patterns:
        if re.search(p, payload):
            return True
    return False


def rate_limit(ip):
    now = time.time()
    RATE.setdefault(ip, [])
    RATE[ip] = [t for t in RATE[ip] if now - t < WINDOW]
    RATE[ip].append(now)
    return len(RATE[ip]) > MAX_REQ


def firewall():
    ip = request.remote_addr
    url = request.url.lower()

    # 🔥 FINAL FIX: decode URL properly
    payload = unquote(request.full_path).lower()

    # 🚨 Rate limiting
    if rate_limit(ip):
        log_attack(ip, "Rate Limit Exceeded", url)
        abort(429)

    # 🚨 SQL Injection
    if detect(SQL_PATTERNS, payload):
        log_attack(ip, "SQL Injection", url)
        abort(403)

    # 🚨 XSS Attack
    if detect(XSS_PATTERNS, payload):
        log_attack(ip, "XSS Attack", url)
        abort(403)

    # ✅ Normal request
    log_allowed(ip, url)