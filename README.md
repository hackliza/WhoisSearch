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
To use this program, first, you have to add words that you want to search in the file **white_list.txt** that is located at **config** folder. Optionally, you can add words that you don’t want to see in the results in the file **black_list.txt** located at **config** folder too.

For example, you can add the following words to the white list:
+ foo
+ bar
+ foobar
+ example

and the following words to the black list:
+ food
+ bart

Then, you run the program with the following command:
```
python ./whoissearch
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
