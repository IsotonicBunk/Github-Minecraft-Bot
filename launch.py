import os
import subprocess
import zipfile




# === НАСТРОЙКИ ===
MC_DIR = "./minecraft"  # путь к папке Minecraft
VERSION = "1.16.5"
FABRIC_VERSION = "0.14.0"
JDK_DIR = "java"  # системная java
USERNAME = "isobunsMCGithubBot"

# === СОБИРАЕМ CLASSPATH ===
libs = []

for root, dirs, files in os.walk(os.path.join(MC_DIR, "libraries")):
    for file in files:
        if file.endswith(".jar"):
            libs.append(os.path.join(root, file))

# Добавляем основной Minecraft jar
libs.append(os.path.join(MC_DIR, "versions", VERSION, f"{VERSION}.jar"))

# classpath для Linux / Ubuntu
cp = ":".join(libs)

# === NATIVES ===
natives_path = os.path.join(MC_DIR, "natives")

os.makedirs(natives_path, exist_ok=True)

for root, dirs, files in os.walk(os.path.join(MC_DIR, "libraries")):
    for file in files:
        if "natives-linux" in file and file.endswith(".jar"):
            jar_path = os.path.join(root, file)

            with zipfile.ZipFile(jar_path, 'r') as jar:
                jar.extractall(natives_path)

print("Natives extracted!")


# === КОМАНДА ===
cmd = [
    JDK_DIR,
    "-Xmx2G",
    f"-Djava.library.path={natives_path}",
    "-cp", cp,

    # Главный класс Fabric
    "net.fabricmc.loader.impl.launch.knot.KnotClient",

    "--username", USERNAME,
    "--version", f"fabric-loader-{FABRIC_VERSION}-{VERSION}",
    f"-Dorg.lwjgl.librarypath={natives_path}",
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