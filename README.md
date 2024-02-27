# regEx: Regular Expressions interpreter

## Description

This project implements a regular expression interpreter. It allows the user to give a language that is a solution to a particular problem and try to solve it from scratch in an interface where he can send his solutions to the problem and check whether or not a certain word is within the language he has proposed. The user can also get feedback of examples of words that give errors in case his solution is wrong.

## Code execution

To execute this code, it will be necessary to have the grammar `regEx.g4` and the file `regEx.py` in the same folder. In a linux terminal, the following commands will be executed:

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor regEx.g4
streamlit run regEx.py
```
Or you can use the makefile by doing `make` to create the necessary files and `make clear` to clean.

## Usage

Once the necessary files have been generated and the execution has begun, we will have to write the statement of the problem and give the name of the file that contains the solution (it must be in the same folder). At this point, we can start writing our proposal to solve the problem and we can use the tool that allows us to determine whether or not a particular word belongs to the language we are declaring.
Any program must always end with an `output variable` where `variable` will be the variable that will contain the language we want to return as a solution.

## Grammar

To be able to understand how we should write our programs that will be interpreted as regular expressions, we can look at the file `regEx.g4`, which contains the grammar. As expected from a language to declare regular expressions, you can do unions, intersections, concatenations, substitutions, unions with the complement or Kleen star operations.

## Result

When we submit our solutions, we'll be told if it's correct, and if it's not, we'll be told examples of words that aren't there and should be there and/or are accepted and shouldn't be.

## Example

The file named `solution.txt` is an example of a program written to be interpreted as a regular expression.

## Author

Sergio Perez

