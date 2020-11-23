# WhoisSearch

WhoisSearch is a program that search in RIPE, APNIC and AFRINIC a list os user defined words and returns a CSV and JSON with the networks that contain at least one word of the list.

## Prerequisites

This program uses the Requests library and can be installed with one of the following commands:

```
pip install requests
```

or

```
pip install –r requirements.txt
```

## Usage
To use this program, first, you have to create a file with the words that you want to be searched (whitelist). 
Optionally, you can create a file with the words that you want to exclude in the results (blacklist).

For example, you can add the following words to the whitelist:
```
foo
bar
example
```

and the following words to the blacklist:
```
food
bart
```

Then, you run the program with the following command:
```
python ./whoissearch.py -w whitelist.txt -b blacklist.txt
```

Finally, you will got the following result:

![output](images/Output_example.PNG)

## Behavior
1. The program downloads the databases of RIPE, APNIC and AFRINIC from the official FTP servers.
2. Then, parses the IPv4 network blocks.
3. After that, the program classifies block in function of the words os the white and black lists.
4. Finally, write the results in CSV and JSON format.

## TODO
+ Add download, parsing and classifying of ARIN and LACNIC.
+ Search for IPv6 networks.
