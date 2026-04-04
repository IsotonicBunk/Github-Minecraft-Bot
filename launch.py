import os
import subprocess

# === НАСТРОЙКИ ===
MC_DIR = ".\\minecraft"
VERSION = "1.16.5"
FABRIC_VERSION = "0.14.0"
#JDK_DIR = ".\\jdk\\jdk-21.0.10.7-hotspot\\bin\\java.exe"
JDK_DIR = "java"
USERNAME = "isobunsMCGithubBot"

# === СОБИРАЕМ CLASSPATH ===
libs = []

for root, dirs, files in os.walk(os.path.join(MC_DIR, "libraries")):
    for file in files:
        if file.endswith(".jar"):
            libs.append(os.path.join(root, file))

# Minecraft jar
libs.append(os.path.join(MC_DIR, "versions", VERSION, f"{VERSION}.jar"))

# classpath
cp = ";".join(libs)

# === NATIVES ===
natives_path = os.path.join(MC_DIR, "natives")

# === КОМАНДА ===
cmd = [
    JDK_DIR ,
    "-Xmx2G",
    f"-Djava.library.path={natives_path}",
    "-cp", cp,

    # Главный класс Fabric
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

# === ЗАПУСК ===
print("Запуск Minecraft с Fabric...")
subprocess.run(cmd)