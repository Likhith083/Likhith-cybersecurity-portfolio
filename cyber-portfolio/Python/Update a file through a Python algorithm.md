### **Project description**

In an organization, access to restricted content is controlled with an allow list of IP addresses. The "allow\_list.txt" file identifies these IP addresses. A separate remove list identifies IP addresses that should no longer have access to this content. I created a robust Python module, update\_allow\_list.py, to automate updating the "allow\_list.txt" file. Unlike a simple script, this program includes safety features like "dry runs" to preview changes without applying them, creates backups of the original data, and utilizes a suite of unit tests to ensure accuracy.

### **Import modules and define file paths**

For the first part of the algorithm, I needed to set up the environment to handle file system paths and command-line arguments. Instead of using simple strings for file names, I imported the Path class from the pathlib library:

Python

from pathlib import Path  
import update\_allow\_list

In my algorithm, pathlib provides an object-oriented way to handle filesystem paths, making the code more readable and compatible across different operating systems. This allowed me to easily define the locations of the "allow.txt" and "remove.txt" files and pass them into my main function. I also structured the code as a reusable module, allowing me to import it into a testing file.

### **Read and parse the file contents**

In order to read the file contents effectively, I created a utility function named read\_list. This function goes beyond standard reading; it cleans the data as it imports it.

When reading the files, I needed to ignore blank lines and comments (lines starting with \#) to prevent errors. The read\_list function opens the file using the .read\_text() method provided by pathlib. It then converts the text into a list and filters out any unwanted data. This ensures that the variable ip\_addresses only contains valid IP addresses that act as the data source for my algorithm.

### **Iterate through the remove list**

A key part of my algorithm involves iterating through the IP addresses that are elements in the remove list. To do this, I incorporated a for loop within the update\_allow\_list function:

The for loop in Python repeats code for a specified sequence. The overall purpose of the loop in this algorithm is to apply specific logic to every IP address found in the remove\_list. The loop iterates through the sequence of IPs identified for removal, assigning each value to the loop variable element one by one.

### **Remove IP addresses and track changes**

My algorithm requires removing any IP address from the allow list that is also contained in the remove list. To make the script informative, I tracked exactly which IPs were removed.

Python

if element in allow\_list:  
    allow\_list.remove(element)  
    removed.append(element)

First, within my for loop, I created a conditional that evaluated whether the loop variable element was found in the allow\_list. If it was, I applied .remove() to eliminate it. I also appended this IP to a separate list called removed. This allows the program to report back exactly which addresses were deleted and which remaining addresses were kept, providing clear feedback to the user.

### **Update the file with safety checks (Dry Run & Backup)**

As a final step in the modification process, I needed to update the allow list file. However, before writing any data, I implemented a safety check using a dry\_run parameter.

Python

if not dry\_run:  
    if backup:  
        \# Logic to create a timestamped backup  
    allow\_path.write\_text("\\n".join(allow\_list))

The dry\_run argument is a boolean (True/False). If set to True, the algorithm skips the writing step entirely, allowing me to verify what *would* happen without risking data loss. If dry\_run is False, 1the algorithm proceeds. Before overwriting the file, it checks the backup parameter; if true, it creates a timestamped copy of the original file. Finally, it uses the .write\_text() method to write the updated list of IPs back to the file, ensuring restricted content is secured.

### **Verify the algorithm with Unit Tests**

To guarantee the algorithm works as expected, I wrote a test suite using the pytest framework.

Python

def test\_remove\_ips(tmp\_path):  
    \# ... setup temporary files ...  
    assert removed \== \["5.6.7.8"\]  
    assert allow.read\_text().strip().splitlines() \== \["1.2.3.4"\]

I used the tmp\_path fixture to create temporary files in a strictly controlled environment. I wrote assertions—statements that check if a condition is true—to verify that the correct IPs were removed and that the file on the disk was updated correctly. I also created a separate test, test\_dry\_run\_no\_change, to assert that the file remains untouched when the dry run mode is active.

### **Summary**

I created a sophisticated Python module that removes IP addresses identified in a remove list from an "allow\_list.txt" file. This algorithm involved using pathlib for robust file handling and creating a custom read\_list function to parse data while ignoring comments. I iterated through the remove list, eliminating matches from the allow list while tracking exactly what was removed. Uniquely, this implementation prioritized safety by including a dry\_run feature to preview changes and a backup system to preserve data. Finally, I validated the entire process with unit tests to ensure the code performs accurately under various conditions.

