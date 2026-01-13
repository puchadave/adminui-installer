import os
import shutil
from flask import current_app

def backup_tenant_data(tenant_id):
    tenant_storage_path = os.path.join(current_app.config['TENANT_STORAGE'], tenant_id)
    backup_path = os.path.join(current_app.config['BACKUP_STORAGE'], tenant_id)

    if not os.path.exists(tenant_storage_path):
        raise FileNotFoundError(f"Tenant data for {tenant_id} not found.")

    if os.path.exists(backup_path):
        shutil.rmtree(backup_path)

    shutil.copytree(tenant_storage_path, backup_path)
    return f"Backup for tenant {tenant_id} created successfully."

def backup_all_tenants():
    tenants = os.listdir(current_app.config['TENANT_STORAGE'])
    for tenant_id in tenants:
        backup_tenant_data(tenant_id)
    return "All tenant data backed up successfully."

if __name__ == "__main__":
    print("This module is intended to be imported, not run directly.")