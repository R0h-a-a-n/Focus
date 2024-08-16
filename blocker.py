host1=input("Enter name of website to block:")
file = open("C:\Windows\System32\drivers\etc\hosts","a")
file.write(f"127.0.0.1   {host1}")
file.close()