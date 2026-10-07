# 🔐 SQL Injection Patterns
SQL_PATTERNS = [
    r"or\s+1=1",
    r"'\s*or\s*'1'='1",
    r"union\s+select",
    r"select\s+.*\s+from",
    r"insert\s+into",
    r"drop\s+table",
    r"update\s+.*\s+set",
    r"--",
    r";"
]

# ⚠️ XSS Attack Patterns
XSS_PATTERNS = [
    r"<script.*?>.*?</script>",
    r"<script>",
    r"</script>",
    r"javascript:",
    r"onerror\s*=",
    r"onload\s*=",
    r"<img.*?onerror=.*?>"
]