import time
def shutdown(message, delay, force=False): 
    print("Shutdown message: ",message) 
    time.sleep(delay)
    if force:
        print("Force shutdown initiated!")
    else:
        print("Shutdown in progress...")
    print("System shutting down... Goodbye!")
shutdown("System is going down for maintenance.", 10, force=True)