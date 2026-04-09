import os
import subprocess
import urllib.request
import zipfile


# === Автоскачивание linux natives для LWJGL 3.2.2 ===
print("Скачиваем Linux natives для LWJGL...")

LWJGL_VERSION = "3.2.2"
BASE_URL = f"https://build.lwjgl.org/release/{LWJGL_VERSION}/bin"

natives = [
    "lwjgl",
    "lwjgl-glfw",
    "lwjgl-openal",
    "lwjgl-opengl",
    "lwjgl-stb",
    "lwjgl-tinyfd"
]

libs_dir = "./minecraft/libraries"

for lib in natives:
    jar_name = f"{lib}-natives-linux.jar"
    url = f"{BASE_URL}/{lib}/{jar_name}"
    dest_path = os.path.join(libs_dir, f"org/lwjgl/{lib.replace('lwjgl-', '')}/{LWJGL_VERSION}/{jar_name}")
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    if not os.path.exists(dest_path):
        print(f"Скачиваем {jar_name}...")
        urllib.request.urlretrieve(url, dest_path)
    else:
        print(f"{jar_name} уже есть")

print("Linux natives готовы!")




# === НАСТРОЙКИ ===
MC_DIR = "./minecraft"
VERSION = "1.16.5"
FABRIC_VERSION = "0.14.0"        # ← убедись, что это правильная версия твоего fabric loader
USERNAME = "isobunMCBot"

# === Собираем classpath (теперь есть и linux natives) ===
libs = []
for root, dirs, files in os.walk(os.path.join(MC_DIR, "libraries")):
    for file in files:
        if file.endswith(".jar"):
            libs.append(os.path.join(root, file))

libs.append(os.path.join(MC_DIR, "versions", VERSION, f"{VERSION}.jar"))

cp = ":".join(libs)

cmd = [
    "java",
    "-Xmx2G",
    "-Dfabric.renderer=0",
    "-Dorg.lwjgl.util.Debug=true",
    "-Dorg.lwjgl.util.DebugLoader=true",
    
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

print("Запуск Minecraft...")
result = subprocess.run(cmd)
print(f"Код завершения: {result.returncode}")