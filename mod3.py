from sympy import *
from sympy.solvers.solveset import linsolve

p = 0.5;
p1 = 0.45;
p2 = 0.35;

np = 1-p;
np1 = 1-p1;
np2 = 1-p2;
P1, P2, P3, P4, P5, P6 = symbols('P1, P2, P3, P4, P5, P6')
A = Matrix(((1, 1, 1, 1, 1, 1, 1),#(p-1, p*np2, 0, 0, 0, 0, 0), 
	(0,  p*p2-1, p*np1, p*np1, 0, 0, 0),
	(np, np*np2, p*p1-1, p*p1*np2, 0, 0, 0),
	(0, np*p2, np*np1, p*p1*p2+np*np1-1, p*np1, np1, 0),
    (0, 0, np*p1, np*p1*np2, p1-1, p1*np2, 0),
	(0, 0, 0, np*p1*p2, np*np1, p1*p2-1, 0)#,
 	))


system_answers = solve_linear_system(A, P1, P2, P3, P4, P5, P6)
print(system_answers)
p000 = system_answers[P1]
p001 = system_answers[P2]
p010 = system_answers[P3]
p011 = system_answers[P4]
p110 = system_answers[P5]
p111 = system_answers[P6]


Po = p011*p2*np1+p110*p1*np+p111*(p2*np1+p1*np);
print(f'Po = {Po}');


Q = 1 - Po;
print(f'Q = {Q}');

A = (p001 + p111 + p011)*np2;
print(f'A = {A}');

Lc = p000+p001+p010+p011+2*(p110+p111)
Wc = Lc/A	
print(f'Wc = {Wc}');

