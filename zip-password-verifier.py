import zipfile

def verify_zip_password(zip_path, password):
    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(pwd=password.encode())
        return True
    except RuntimeError:
        return False
    except FileNotFoundError:
        print("ZIP file not found.")
        return False

zip_file = input("Enter zip file path: ")
pwd = input("Enter password to verify: ")

if verify_zip_password(zip_file, pwd):
    print("✅ Password is correct.")
else:
    print("❌ Incorrect password.")
