import os
import subprocess
import platform
import requests
import zipfile
import tarfile

def is_terraform_installed():
    try:
        subprocess.run(["terraform", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_terraform():
    if is_terraform_installed():
        print("Terraform is already installed.")
        return

    # Terraform URL for downloading
    base_url = "https://releases.hashicorp.com/terraform"

    # Get latest Terraform version (replace this with actual version retrieval)
    version = "1.1.0" # Example version

    # Detect platform and architecture
    os_name = platform.system().lower()
    arch = platform.machine()
    
    if arch == 'x86_64' or arch == 'AMD64':
        arch = 'amd64'
    elif arch == 'aarch64':
        arch = 'arm64'
    else:
        raise Exception(f"Unsupported architecture: {arch}")

    if os_name == 'windows':
        terraform_file = f"terraform_{version}_windows_{arch}.zip"
    elif os_name == 'darwin':
        terraform_file = f"terraform_{version}_darwin_{arch}.zip"
    elif os_name == 'linux':
        terraform_file = f"terraform_{version}_linux_{arch}.zip"
    else:
        raise Exception(f"Unsupported OS: {os_name}")

    # Download Terraform
    url = f"{base_url}/{version}/{terraform_file}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to download Terraform: {url}")

    # Save the file
    with open(terraform_file, 'wb') as file:
        file.write(response.content)

    # Extract the file
    if terraform_file.endswith('.zip'):
        with zipfile.ZipFile(terraform_file, 'r') as zip_ref:
            zip_ref.extractall()
    else:
        with tarfile.open(terraform_file, 'r:gz') as tar_ref:
            tar_ref.extractall()

    # Move the binary to a specific directory (optional)
    if os_name == 'windows':
        os.rename('terraform.exe', 'C:\\Program Files\\terraform\\terraform.exe')
    else:
        os.rename('terraform', '/usr/local/bin/terraform')

    print("Terraform installed successfully.")

# Use the function
install_terraform()
