import os.path
import sys
from config import Config

if len(sys.argv) > 1:
    root_path = sys.argv[1]
else:
    root_path = ""
config_path = os.path.join(root_path, '.config')

print(f"开始配置config: {config_path}")

file = Config(config_path)

integrated_configs = [
    "CONFIG_PACKAGE_block-mount",
    "CONFIG_LUCI_LANG_zh_Hans",
    "CONFIG_PACKAGE_luci-compat",
    "CONFIG_PACKAGE_luci-app-alist",
    "CONFIG_PACKAGE_luci-app-argon-config",
    "CONFIG_PACKAGE_luci-app-cpufreq",
    "CONFIG_PACKAGE_luci-app-ttyd",
    "CONFIG_PACKAGE_openssh-sftp-server",
    "CONFIG_PACKAGE_coremark",
    "CONFIG_PACKAGE_blkid",
    "CONFIG_PACKAGE_cfdisk",
    "CONFIG_PACKAGE_gdisk",
    "CONFIG_PACKAGE_lsblk",
    "CONFIG_IMAGEOPT",
    "CONFIG_TARGET_DEFAULT_LAN_IP_FROM_PREINIT",
    "CONFIG_PREINITOPT",
    "CONFIG_TARGET_PREINIT_SUPPRESS_STDERR",
]

for config in integrated_configs:
    file.set_config(config)

file.set_config("CONFIG_TARGET_PREINIT_IP", '"10.0.0.1"')
file.set_config("CONFIG_TARGET_PREINIT_BROADCAST", '"10.0.0.255"')
file.set_config("CONFIG_VERSION_REPO", '"https://mirrors.nju.edu.cn/immortalwrt/snapshots"')
file.set_config("CONFIG_FEED_nss_packages", 'n')
file.set_config("CONFIG_FEED_sqm_scripts_nss", 'n')
