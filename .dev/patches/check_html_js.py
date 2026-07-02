import re, subprocess, sys, tempfile, os
html = open('index.html', encoding='utf-8').read()
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
if not scripts:
    print("Kein <script>-Block gefunden"); sys.exit(1)
js = "\n".join(scripts)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
    f.write(js)
    tmp = f.name
r = subprocess.run(['node', '--check', tmp])
os.unlink(tmp)
sys.exit(r.returncode)
