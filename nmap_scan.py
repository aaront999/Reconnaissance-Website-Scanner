import subprocess

def nmap_scan(options, ip):
    # creates and stores the user command options and ip address into "commands" variable
    commands = ["nmap"] + options.split() + [ip]
    
    # runs the commands and captures the output into results variable
    # "universal_newlines=True" This argument ensures that the output is returned as a string rather than bytes
    try:
        results =  subprocess.check_output(commands, universal_newlines=True)
        return results
    # This line catches any exceptions that are of type CalledProcessError, which occurs if the command executed by subprocess.check_output
    # Stores the error into "e" variable
    except subprocess.CalledProcessError as e: 
        return f"Error: {e.output}"

# test cases
print(nmap_scan('-F', '137.74.187.103'))