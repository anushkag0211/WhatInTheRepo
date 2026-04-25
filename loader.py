import os

def load_files(path):
    files_data = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        files_data.append({
                            "file": file_path,
                            "text": f.read()
                        })
                except:
                    pass

    return files_data
