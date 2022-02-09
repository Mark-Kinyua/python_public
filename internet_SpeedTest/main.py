import speedtest

# Lets test Zuku.

test = speedtest.Speedtest()
print("Loading server list...")

test.get_servers() # Get list of servers
print("Getting best server...")

best = test.get_best_server()

print(f"Found: {best['host']} located in : {best['country']}")

print("Performing download test..")
download_result = test.download()

print("Performing upload test..")
upload_result = test.upload()
print("Getting ping")
ping_result = test.results.ping

# Print all information.
print(f"Download speed: {download_result / 1024 / 1024:.2f} mb/s ") # Changing bits to mbs
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} mb/s ")
print(f"Ping: {ping_result:.2f} ms")
