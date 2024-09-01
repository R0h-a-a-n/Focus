def block_websites(websites):
    with open("C:/Windows/System32/drivers/etc/hosts", "a") as file:
        for website in websites:
            file.write(f"127.0.0.1   {website}\n")
    print("Websites blocked.")

def unblock_websites(websites):
    # Read the current contents of the hosts file
    with open("C:/Windows/System32/drivers/etc/hosts", "r") as file:
        lines = file.readlines()

    # Rewrite the hosts file, excluding the blocked websites
    with open("C:/Windows/System32/drivers/etc/hosts", "w") as file:
        for line in lines:
            if not any(website in line for website in websites):
                file.write(line)
    print("Websites unblocked.")

def get_websites_to_block():
    websites = []
    while True:
        website = input("Enter name of website to block (or type 'done' to finish): ")
        if website.lower() == 'done':
            break
        websites.append(website)
    return websites
