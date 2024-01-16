import mmap
import os

# Define the file name and the size of the file
file_name = "sample_mmap.dat"
file_size = 1024  # Size in bytes

# Create and open the file for reading and writing
with open(file_name, "wb") as file:
    # Expand the file to the desired size
    file.seek(file_size - 1)
    file.write(b"\x00")

# Open the file for reading and writing
with open(file_name, "r+b") as file:
    # Memory-map the file
    mmapped_file = mmap.mmap(file.fileno(), file_size, access=mmap.ACCESS_WRITE)

    # Write some data to the memory-mapped file
    message = "Hello from memory-mapped file!"
    mmapped_file[:len(message)] = message.encode()

    # Read data from memory-mapped file
    mmapped_file.seek(0)
    print("Data read from memory-mapped file:", mmapped_file.read(len(message)).decode())

    # Close the memory-mapped file
    mmapped_file.close()

# Clean up: Delete the file after use
os.remove(file_name)
