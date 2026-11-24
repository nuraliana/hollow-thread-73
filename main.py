import os


ENTRY = "Approved. The comment thread is empty because the code is perfect, or because everyone else is already gone."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
