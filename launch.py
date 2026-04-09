import os
import subprocess

# === НАСТРОЙКИ ===
MC_DIR = "./minecraft"
VERSION = "1.16.5"
FABRIC_VERSION = "0.14.0"        # ← убедись, что это правильная версия твоего fabric loader
USERNAME = "isobunsMCGithubBot"

# Собираем classpath — ВАЖНО: добавляем ВСЕ jar, включая windows natives (они не помешают)
libs = []
for root, dirs, files in os.walk(os.path.join(MC_DIR, "libraries")):
    for file in files:
        if file.endswith(".jar"):
            libs.append(os.path.join(root, file))

# Добавляем сам клиент
libs.append(os.path.join(MC_DIR, "versions", VERSION, f"{VERSION}.jar"))

cp = ":".join(libs)

# Команда запуска
cmd = [
    "java",
    "-Xmx2G",
    
    "-cp", cp,
    "net.fabricmc.loader.impl.launch.knot.KnotClient",

    "--username", USERNAME,
    "--version", f"fabric-loader-{FABRIC_VERSION}-{VERSION}",
    "--gameDir", MC_DIR,
    "--assetsDir", os.path.join(MC_DIR, "assets"),
    "--assetIndex", "1.16",
    "--uuid", "1234567890abcdef1234567890abcdef",
    "--accessToken", "0",
    "--userType", "legacy"
]

print("Запуск Minecraft 1.16.5 Fabric на Linux...")
result = subprocess.run(cmd, env=os.environ.copy())

print(f"Процесс завершился с кодом: {result.returncode}")