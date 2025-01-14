import os
import sys
import socket
import zlib
import time

ARCHIVE_DIR = 'archive'

# Ensure the archive directory exists
if not os.path.exists(ARCHIVE_DIR):
    os.makedirs(ARCHIVE_DIR)

# Function to execute a list of commands on the target system
def execute_commands(commands, target_ip):
    """Execute a list of commands on the target system via remote connection."""
    output = ""
    for cmd in commands:
        try:
            print(f"Executing: {cmd}")
            cmd_output = send_command_to_target(target_ip, cmd)
            output += f"$ {cmd}\n{cmd_output}\n{'='*40}\n"
        except Exception as e:
            output += f"Error executing command {cmd}: {str(e)}\n"
    return output

# Function to send commands to the target system
def send_command_to_target(target_ip, cmd):
    """Send command to the target system and retrieve the output."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, 9999))  # Target's IP and port
            s.sendall(cmd.encode('utf-8'))
            response = s.recv(4096).decode('utf-8')
        return response
    except socket.error as e:
        return f"Connection error: {str(e)}"
    except Exception as e:
        return f"Failed to execute command: {str(e)}"

# Function to save output to a file
def save_output(filename, data):
    """Save output to a file."""
    try:
        with open(f"{ARCHIVE_DIR}/{filename}", "w") as f:
            f.write(data)
        print(f"Output saved to {ARCHIVE_DIR}/{filename}")
    except Exception as e:
        print(f"Error saving output: {str(e)}")

# Function to handle the exec command
def handle_exec(argv, target_ip):
    """Handle the exec command input and execute it on the remote target."""
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(f"Usage: {sys.argv[0]} <command1> [<command2> ...] [-o <filename>]")
        return

    write_file = None
    if '-o' in argv:
        write_index = argv.index('-o')
        if len(argv) > write_index + 1:
            write_file = argv[write_index + 1]
        else:
            print("Error: No filename specified for output.")
            return
        argv = argv[:write_index]

    commands = ' '.join(argv[1:])
    output = execute_commands(commands.split(), target_ip)

    if write_file:
        save_output(write_file, output)
    else:
        print(output)

# Function to compress data for improved efficiency in transmission
def compress_data(data):
    """Compress data using zlib for efficient transmission."""
    return zlib.compress(data.encode('utf-8'))

# Function to decompress the data upon receipt
def decompress_data(data):
    """Decompress data received from the target."""
    return zlib.decompress(data).decode('utf-8')

# Command line execution entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: exec.py <command1> [<command2> ...] [-o <filename>]")
        sys.exit(1)

    # Example target IP (replace with the real target IP)
    target_ip = "192.168.1.10"  # Example IP, change as needed

    handle_exec(sys.argv, target_ip)