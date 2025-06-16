#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    module_path = "/tmp/hidden_4.pyc"

    # Modulun spesifik yolunu və adını təyin edirik
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Modulda olan bütün adları götürürük
    names = dir(hidden_4)

    # __ ilə başlayanları filterləyirik
    filtered_names = [name for name in names if not name.startswith("__")]

    # əlifba sırası ilə sırala
    filtered_names.sort()

    # çap et
    for name in filtered_names:
        print(name)
