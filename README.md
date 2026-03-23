# Implementation-of-Lexical-Analysis
## Description
For this evidence, the language chosen was all the possible combinations of ab1.<br>
The rules were the following:<br>
- Must have ab1 or 1ba
- Must end with ba.
The **modeling tecnique** used was a Deterministic Finite Automata (DFA) to represents my solutions. DFA was develop because of the predictable and deterministic behavior in its definition presented in (NFA Vs: DFA: Unraveling the Differences in Finite Automaton Models - FasterCapital, 2025)
<br>By the rules required in the lexical analysis, the DFA was implemented to assure that the AUTOMATA fulfilled the necessary processes.

## Model Of the Solution
These is the automata I generated for the language.
![DFA](Automata.png) <br>
I decided to represent my chosen language in a DFA so that the transition to program the Automata in prolog was easier to follow. If I were to use a NFA, the process of implementation would be harder. The analysis between them was followed by the resume given in (GeeksforGeeks, 2025).

## Implementation in prolog

The language chosen was implemented in prolog. The complexity that it follows is of O(n). This is because the DFA process each symbol of the chain one time. Aswell as in the implementation in prolog. The implementation uses tail recursion, which helps with the space complexity by reutilize the same frame only by updating the variables.
Some examples of inputs and outputs are:
- [a,b,1,b,a] > accepted
- [a,b,1,b,b,b,b,a] > accepted
- [1,b,a] > accepted
- [b,a] > rejected
- [a,b,b,1,b] > rejected
- [a,b,1] > rejected

### References 
Peckory, G. (2015, December 1). Why use NFAs over DFAs. Stack Overflow. https://stackoverflow.com/questions/33260936/why-use-nfas-over-dfas <br>
GeeksforGeeks. (2025, July 12). Difference between DFA and NFA. GeeksforGeeks. https://www.geeksforgeeks.org/theory-of-computation/difference-between-dfa-and-nfa/ <br>
NFA vs: DFA: Unraveling the Differences in Finite Automaton Models - FasterCapital. (2025, April 6). FasterCapital. https://fastercapital.com/content/NFA-vs--DFA--Unraveling-the-Differences-in-Finite-Automaton-Models.html
Lists and Recursion - wiki.visual-prolog.com. (n.d.). https://wiki.visual-prolog.com/index.php?title=Lists_and_Recursion#Tail_Recursion


