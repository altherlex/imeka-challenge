# IMEKA-CHALLENGE

## How to run:

```bash
$ git clone https://github.com/altherlex/imeka-challenge.git
$ cd imeka-challenge
$ python fizz_buzz.py
$ python reverse_words.py

$ open todo-list/index.html

$ python
>>> from reverse_words import reverse_words_to_file
>>> reverse_words_to_file('hello world!')
```

## General code - Q1

```
Goal: The goal of this exercise is to assess your coding strategies on various short, classical
problems.
Language: you can use the language of your choice. If needed, please provide instructions on
compilation and execution. If compilation is needed, please ensure that you provide an easy to
use solution that works on Linux. You can use libraries if required, but not a library that would
handle the problem (for example, do not use a Prime number testing library for Problem 4).
Problem 1: Code an algorithm that will output the Fizz Buzz sequence
(https://en.wikipedia.org/wiki/Fizz_buzz) to the terminal, with the following modified rules:
- Output each number as its value number
- Except if divisible by 3, output “Fizz”
- Except if divisible by 5, output “Buzz”
- If divisible by both 3 and 5, output “Fizz-Buzz”
- If the number contains the digit “6”, output “Buzz-Fizz” instead.
Problem 2: Write a function that will take a given string and reverse the order of the words. The
string should be taken as an input, and the result should be output to a text file.
Deliverables
- Your code for each problem in a separate file.
- Instructions on how to setup and use your code.
```

## Code assessment workflow - Q2

```
We would like to understand your workflow and thought process when assessing new code,
especially in a language you haven’t used.
Imeka has developed the trk-io project as an open-source library to help working with the
TrackVis file format. This specific data structure in the trk-io repository contains a data structure
that is used to store streamlines information, which represent tracts of the white matter that are
reconstructed from diffusion MRI.
1. Please summarize your thought process and workflow to understand the data structure,
to answer the questions below and how you found the information when you were not
familiar with some concepts.
2. From lines 8-12, what’s the purpose of the “derive” line? What could be a reason to
create an “ArraySequence” structure in a project like “trk-io”?
```

## Front end development - Q3

```
We would like you to create a minimal To-Do List web component with the following features:
- A text input and an “Add” button
- When the user adds a task:
- It appears in a list below
- Each task has a “Delete” button to remove it
- Basic styling (CSS or inline styles)
- The list persists while the page is open (no need for saving to localStorage)
You may use basic HTML, JS and CSS, or use a framework. If using a framework, make sure to
include any instruction that might be needed to deploy.
Deliverables:
- Archive of the code that can be used to test the product.
- Any instructions, if applicable.
```