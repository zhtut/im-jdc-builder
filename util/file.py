class File:
    def __init__(self, path: str):
        self.path = path

    def check_has_line(self, line: str) -> bool:
        with open(self.path, "r") as f:
            for l in f.readlines():
                if line in l:
                    return True
        return False

    def replace_line(self, key: str, new_line: str, not_found_add_to_end: bool = False):
        if not new_line.endswith("\n"):
            new_line = new_line + "\n"
        with open(self.path, "r") as f:
            new_lines = []
            is_find = False
            for line in f.readlines():
                if key in line:
                    print(f"已找到：{key}")
                    new_lines.append(new_line)
                    is_find = True
                else:
                    new_lines.append(line)
            if not is_find and not_found_add_to_end:
                new_lines.append(new_line)
            with open(self.path, 'w') as w:
                w.writelines(new_lines)

            print("检查是否包含")
            contain = self.check_has_line(new_line)
            if contain:
                print(f"已包含：{new_line}")
            else:
                print(f"未包含：{new_line}")
