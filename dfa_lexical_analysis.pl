% DFA

final_state(q5).
final_state(q8).

delta(q0, a, q1).
delta(q0, b, q0).
delta(q0, 1, q6).
delta(q1, a, q1).
delta(q1, b, q2).
delta(q1, 1, q6).
delta(q2, a, q1).
delta(q2, b, q0).
delta(q2, 1, q3).
delta(q3, a, q3).
delta(q3, b, q4).
delta(q3, 1, q3).
delta(q4, a, q5).
delta(q4, b, q4).
delta(q4, 1, q3).
delta(q5, a, q3).
delta(q5, b, q4).
delta(q5, 1, q3).
delta(q6, a, q1).
delta(q6, b, q7).
delta(q6, 1, q6).
delta(q7, a, q8).
delta(q7, b, q0).
delta(q7, 1, q6).
delta(q8, a, q3).
delta(q8, b, q4).
delta(q8, 1, q3).

%  Recursive

process(State, []) :-
    final_state(State).

process(State, [Symbol|Rest]) :-
    delta(State, Symbol, Next),
    process(Next, Rest).

%  accepts/1 - checks if string is accepted
accepts(String) :-
    process(q0, String).

% ============================================================
%  evaluate/1 - prints result
% ============================================================

evaluate(String) :-
    write('String : '), write(String), nl,
    result(String).

result(String) :-
    accepts(String),
    write('Result : ACCEPTED'), nl, nl.

result(String) :-
    \+ accepts(String),
    write('Result : REJECTED'), nl.

%  Interactive menu
menu :-
    nl,
    write('============================================'), nl,
    write('   DFA Language 50'), nl,
    write('   Alphabet: {a, b, 1}'), nl,
    write('============================================'), nl,
    nl,
    write('  Options:'), nl,
    write('    1. Enter a string'), nl,
    write('    2. View examples'), nl,
    write('    3. Exit'), nl,
    nl,
    write('  Choose an option (1/2/3): '),
    read(Option), nl,
    handle_option(Option).

handle_option(1) :-
    write('  Enter your string, example: [a,b,1,b,a].'), nl,
    write('  String: '),
    read(String), nl,
    evaluate(String),
    write('  Evaluate another string? (yes/no): '),
    read(Resp), nl,
    (Resp = yes , handle_option(1) ; menu).

handle_option(2) :-
    write('--------------------------------------------'), nl,
    write('  -- Must be ACCEPTED --'), nl, nl,
    evaluate([a,b,1,b,a]),
    evaluate([1,b,a]),
    write('  -- Must be REJECTED --'), nl, nl,
    evaluate([a,b,1]),
    evaluate([b,a]),
    evaluate([]),
    write('  Type "menu." to go back: '),
    read(_), menu.

handle_option(3) :-
    write('  Goodbye!'), nl, nl.

handle_option(_) :-
    write('  Invalid option. Try again.'), nl, menu.

:- initialization(menu).
