# Bad Words Detection Test Guide

In order to ensure that our system is properly detecting and filtering out bad words, it is important to regularly test our bad word detection functionality. This document outlines the process for adding new test cases to our bad word detection system.

## Adding Test Cases

Adding Test Cases
To add new test cases to the bad word detection system, follow these steps:

1. Open the directory containing the test data files in your file explorer. This directory is typically located at `/test/data` of the Project.
2. Within this directory, you should find a file for each language that you want to test. For example, if you are testing bad words in English, you should look for a file named `en_rude_sentences.txt`.
3. Add each of the sentences that you want to use as test cases to the file, one per line.

## Running the test

Once you have added your test sentences to the file, you can run the bad word detection tests by running:

```sh
pytest
```

## How to fix the failed test

If a test fails, one way to fix it is to add the bad word to the **[badwords.json](../responses/badwords.json)** to improve detection of that word.
