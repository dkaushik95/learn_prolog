%% parent(X,Y).
%% male(X).
%% female(X).
%% grandparent(X,Y).
%% wife(X,Y).
%% husband(X,Y).
%% son(X,Y).
%% daughter(X,Y).
%% sister(X,Y).
%% brother(X,Y).
%% uncle(X,Y).



male(abraham).
female(mona).
parent(abraham,herb).
parent(abraham,homer).
parent(mona,herb).
parent(mona,homer).
male(herb).
male(homer).

male(clancy).
female(jackie).
parent(clancy,marge).
parent(clancy,patty).
parent(clancy,selma).
parent(jackie,marge).
parent(jackie,patty).
parent(jackie,selma).
female(marge).
female(patty).
female(selma).

parent(homer,bart).
parent(homer,lisa).
parent(homer,maggie).
parent(marge,bart).
parent(marge,lisa).
parent(marge,maggie).
male(bart).
female(lisa).
female(maggie).





father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).

son(X,Y):- parent(Y,X),male(X).
daughter(X,Y):- parent(Y,X),female(X).

offspring(X,Y):- parent(Y,X).

grandparent(X,Y):-parent(Z,X),parent(Y,Z).

grandfather(X,Y):-parent(Z,X),parent(Y,Z),male(Y).
grandmother(X,Y):-parent(Z,X),parent(Y,Z),female(Y).

sister(X,Y) :-parent(Z,X),parent(Z,Y),female(X),not(X=Y).
brother(X,Y) :-parent(Z,X),parent(Z,Y),male(X),not(X=Y).
uncle(X,Y) :-parent(Z,Y),brother(X,Z).                        
aunt(X,Y) :-parent(Z,Y),sister(X,Z).
