class Config:
    def __init__(self, path: str):
        self.path = path

    def set_config(self, key: str, value: str = 'y'):
        new_line = f"{key}={value}\n"
        with open(self.path, "r") as f:
            new_lines = []
            is_find = False
            for line in f.readlines():
                if line.__contains__(key) and line != new_line:
                    new_lines.append(new_line)
                    is_find = True
                else:
                    new_lines.append(line)

            if not is_find:
                return

            with open(self.path, 'w') as w:
                w.writelines(new_lines)
            if is_find:
                with open(self.path, "r") as f:
                    for l in f.readlines():
                        if key in l:
                            print(f"已修改: {l}")
