import subprocess
import time

def get_apps_to_block():
    apps = []
    while True:
        app_name = input("Enter the name of the application to block (or type 'done' to finish): ")
        if app_name.lower() == 'done':
            break
        apps.append(app_name)
    return apps

def block_applications(app_names):
    while True:
        for app_name in app_names:
            tasks = subprocess.check_output('tasklist', shell=True).decode()
            if app_name in tasks:
                subprocess.call(f'taskkill /F /IM {app_name}', shell=True)
                print(f"{app_name} has been blocked and terminated.")
        
        time.sleep(3)  

def unblock_applications(app_names):
    print("Unblocking applications...")

if __name__ == "__main__":
    apps_to_block = get_apps_to_block()  
    if apps_to_block:
        try:
            block_applications(apps_to_block)
        except KeyboardInterrupt:
            unblock_applications(apps_to_block)
    else:
        print("No applications to block.")
