import os.path
from file import File
import sys

args = sys.argv
if len(args) < 2:
    print("参数不对，需要传入 1: openwr根目录，2：内核id")
    exit(-1)

openwrt_path = args[1]
kernel_md5 = args[2]

print(f"开始给{openwrt_path}，把内核id，修改为：{kernel_md5}")

print("首先在根目录生成vermagic文件")
vermagic_path = os.path.join(openwrt_path, "vermagic")
with open(vermagic_path, 'w') as f:
    f.write(kernel_md5)

with open(vermagic_path, "r") as f:
    content = f.read()
    if content == kernel_md5:
        print(f"生成成功，内容：{content}")
    else:
        print(f"写入失败：文件内容{content}不一致，退出")
        exit(-1)

print("开始修改include/kernel-defaults.mk")

mk_file = "include/kernel-defaults.mk"
mk_file_path = os.path.join(openwrt_path, mk_file)
mk_file_obj = File(mk_file_path)
mk_file_obj.replace_line(
    "md5",
    '	cp $(TOPDIR)/vermagic $(LINUX_DIR)/.vermagic')

print("开始修改package/kernel/linux/Makefile")
make_file = "package/kernel/linux/Makefile"
make_file_path = os.path.join(openwrt_path, make_file)
make_file_obj = File(make_file_path)
make_file_obj.replace_line(
    "md5",
    '  STAMP_BUILT:=$(STAMP_BUILT)_$(shell cat $(LINUX_DIR)/.vermagic)')

print("修改完成")
