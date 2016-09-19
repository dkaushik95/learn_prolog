parent(a,b).
parent(a,c).
parent(a,d).
parent(a,e).

parent(b,f).
parent(b,g).

parent(g,l).
parent(g,m).

parent(c,h).

parent(d,i).

parent(e,j).
parent(e,k).

parent(j,h).

assign(1,a).
assign(2,b).
assign(3,c).
assign(4,d).
assign(5,e).
assign(6,f).
assign(7,g).
assign(8,h).
assign(9,i).
assign(10,j).
assign(11,k).
assign(12,l).
assign(13,m).
assign(14,n).

child(X,Y):- parent(Y,X).

bfs(15).

bfs(N) :-
assign(N,X),
write(X),
write(' is found  with value '),write(N),nl,
N1 is N+1,
bfs(N1).

%% dfs(15).
%% dfs(N):-
%% assign(N,X),
%% write(X),
%% write(' '),
%% N1 is child(T,X),
%% dfs(N1).


