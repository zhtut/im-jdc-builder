import os.path
import sys

if len(sys.argv) > 1:
    root_path = sys.argv[1]
else:
    root_path = ""
config_path = os.path.join(root_path, '.config')

print(f"开始配置config: {config_path}")

with open(config_path, 'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if line.__contains__('luci-app-'):
            if line.startswith("#"):
                lib_name = line.split(' ')[1]
                new_line = f'{lib_name}=m'
                print(f"发现一个luci-app，修改后：{new_line}")
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    with open(config_path, 'w') as w:
        w.writelines(new_lines)
