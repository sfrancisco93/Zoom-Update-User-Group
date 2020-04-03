# Sample Update Zoom User Group Script
This tool is designed to update your Zoom User Groups. This feature is currently unavailable through Zoom's Import User tool.


# Installation
Please ensure you have installed the following packages:
[Requests](https://requests.readthedocs.io/en/master/)

```bash
pip install requests
```

# Instructions
1. Add a CSV file containing two columns: Email, Group. Please see file "sampleTemplate.csv" for an example. 
2. In the file 'main.py', edit Line 5 to point the script to your CSV file created in Step 1. 
3. In the files 'Group.py' and 'User.py' please add your Zoom account's JWT token in Line 5.
4. In your terminal, run:

```bash
python main.py
```

# Additional Notes
Please use this at your own risk. Note that this is only sample code and has been tested in small batches. I am not responsible for any data loss or unexpected results due to the execution of this script. Bug fixes will be added periodically.
