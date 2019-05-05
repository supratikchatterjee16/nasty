# NASTY

This is a project for the analysis and summarization of facts and figures from NEWS channels over RSS feeds. 
It is to become astanalone framework for aggregation of multiple sources for the purpose of:

1. Convenience in NEWS distribution
2. Factual checking of information from different sectors.
3. Collection of all facts pertaining to an object
4. Making trend analysis easier

## Sources

There are lots of news channels that are being considered for collection of information, of which a few are, BBC, CNN, Al Jazeera, Times of India, and a few more.

## Progress

The test project has been completed without optimizations and without any finishes provided. There are lots of optimizations and corners to be covered. This will be done if and only if someone is interested in working with this tool any further.

## Installation

To install, run the installer provided by making use of 
```shell
sh ubuntu_installer.sh
```

## Execution

For execution refer to the shell file called 'nasty.sh' for clear procedure of execution. It gives you the exact method for exeuting the program. It is also an automated file that can be executed in a linux environment.

```shell
sh nasty.sh
```

If you want to execute on multiple servers, the commands are:
1. Executing the sourcing module
```shell
python3 ./python/sourcing
```
2. Starting the CoreNLP server, tailored for information extraction
```shell
java -mx8g -cp "./factserver.jar:../corenlp/*" factserver.Driver
```
3. Running the analyzer
```shell
python3 ./python/analysis/analyzer.py
```
4. Make use of MongoDB to check results
5. There exists a mockup of one of the three major use cases of this project at: [NASTY UI](https://github.com/supratikchatterjee16/nastyui)
