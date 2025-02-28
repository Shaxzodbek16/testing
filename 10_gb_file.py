import os

def create_10gb_file(file_path):
    """Creates a 10GB file filled with random data."""
    with open(file_path, 'wb') as f:
        f.write(os.urandom(10 * 1024 * 1024 * 1024))  # 10GB

if __name__ == "__main__":
    create_10gb_file("bigfile.dat")

