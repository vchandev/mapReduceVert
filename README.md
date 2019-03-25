# mapReduceVert

First, make mapper.py and reducer.py into executable files by entering the following in Terminal:

```
$ chmod +x mapper.py
$ chmod +x reducer.py
```

To run the program, enter the following into Terminal:

```
$ cat testfeed.tsv | ./mapper.py | ./reducer.py
```

This basically passes the output from testfeed.tsv to be taken as input for mapper.py, and the same for reducer.py

To print out the results of word count in a text file, use the following command:

```
$ cat testfeed.tsv | ./mapper.py | ./reducer.py > output.txt
```
