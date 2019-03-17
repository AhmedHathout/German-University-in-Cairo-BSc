s(Tree, A, Z):-
  sentence(Tree, A, Z);
  (sentence(STree, A, B), (while(ConjunctionTree, B, C); and(ConjunctionTree, B, C)), s(Inner, C, Z), Tree = s(STree, ConjunctionTree, Inner)).

sentence(s(NPsTree, VPsTree), A, Z):-
  noun_phrases(NPsTree, A, B), verb_phrases(VPsTree, B, Z).

verb_phrases(VPsTree, A, Z):-
  verb_phrase(VPsTree, A, Z);
  (verb_phrase(VPTree, A, B), and(AndTree, B, C), verb_phrases(Inner, C, Z), VPsTree = vps(VPTree, AndTree, Inner)).

verb_phrase(VPTree, A, Z):-
  (adverbed_verb(AdvTree, A, B), prepositional_noun_phrases(PNPTree, B, Z), VPTree = vp(AdvTree, PNPTree));
  (adverbed_verb(AdvTree, A, B), and(AndTree, B, C), verb_phrase(Inner, C, Z), VPTree = vp(AdvTree, AndTree, Inner)).

adverbed_verb(AdvVTree, A, Z):-
  verb(AdvVTree, A, Z);
  (adverb(AdvTree, A, B), verb(VTree, B, Z), AdvVTree = advv(AdvTree, VTree));
  (verb(VTree, A, B), adverb(AdvTree, B, Z), AdvVTree = advv(AdvTree, VTree)).

noun_phrases(NPsTree, A, Z):-
  noun_phrase(NPsTree, A, Z);
  (noun_phrase(NPTree, A, B), and(AndTree, B, C), noun_phrases(InnerNPsTree, C, Z), NPsTree = nps(NPTree, AndTree, InnerNPsTree)).

noun_phrase(NPTree, A, Z):-
  (non_who_noun_phrase(NPTree, A, Z));
  (non_who_noun_phrase(InnerNPTree, A, B), who_phrase(WhoPTree, B, Z), NPTree = np(InnerNPTree, WhoPTree)).

non_who_noun_phrase(NPTree, A, Z):-
  (determiner(DetTree, A, B), adjectives(AdjTree, B, C), noun(NTree, C, Z), NPTree = np(DetTree, AdjTree, NTree));
  (determiner(DetTree, A, B), noun(NTree, B, Z), NPTree = np(DetTree, NTree));
  (adjectives(AdJTree, A, B), plural_noun(NTree, B, Z), NPTree = np(AdJTree, NTree));
  (plural_noun(NTree, A, Z), NPTree = np(NTree)).

prepositional_noun_phrase(PNPTree, A, Z):-
  noun_phrases(PNPTree, A, Z);
  (preposition(PTree, A, B), noun_phrases(NPsTree, B, Z), PNPTree = pnp(PTree, NPsTree));
  (preposition(PTree, A, B), noun(NTree, B, Z), PNPTree = pnp(PTree, NTree)).

prepositional_noun_phrases(PNPsTree, A, Z):-
  prepositional_noun_phrase(PNPsTree, A, Z);
  (prepositional_noun_phrase(PNPTree, A, B), prepositional_noun_phrases(InnerPNPsTree, B, Z), PNPsTree = np(PNPTree, InnerPNPsTree)).

adjectives(AdjTree, A, Z):-
  adjective(AdjTree, A, Z).
adjectives(adjs(AdjTree, InnerAdjsTree), A, Z):-
  adjective(AdjTree, A, B),
  adjectives(InnerAdjsTree, B, Z).

who_phrase(whop(WTree, VPTree), A, Z):-
  who(WTree, A, B), verb_phrases(VPTree, B, Z).

determiner(det(the), [the|X], X).
determiner(det(some), [some|X], X).
determiner(det(any), [any|X], X).
determiner(det(his), [his|X], X).
determiner(det(her), [her|X], X).
determiner(det(their), [their|X], X).
determiner(det(X), [X|A], Z):-
  singular_determiner([X|A], Z);
  plural_determiner([X|A], Z).

singular_determiner([a|X], X).
singular_determiner([every|X], X).
singular_determiner([each|X], X).
plural_determiner([many|X], X).

%-------------------------------------------------------------------------------

adjective(adj(H), [H|A], Z):-
  adjective([H|A], Z).

adjective([young|X], X).
adjective([old|X], X).
adjective([big|X], X).
adjective([large|X], X).
adjective([empty|X], X).
adjective([poor|X], X).
adjective([white|X], X).
adjective([brilliant|X], X).
adjective([talented|X], X).
adjective([bright|X], X).
adjective([beautiful|X], X).
adjective([short|X], X).
adjective([tall|X], X).
adjective([attractive|X], X).
adjective([angry|X], X).
adjective([jealous|X], X).
adjective([mysterious|X], X).
adjective([violent|X], X).
adjective([crooked|X], X).
adjective([small|X], X).

%-------------------------------------------------------------------------------

noun(n(H), [H|A], Z):-
  singular_noun([H|A], Z);
  plural_noun([H|A], Z).

singular_noun([boy|X], X).
singular_noun([box|X], X).
singular_noun([man|X], X).
singular_noun([room|X], X).
singular_noun([school|X], X).
singular_noun([woman|X], X).
singular_noun([envelope|X], X).
singular_noun([shed|X], X).
singular_noun([building|X], X).
singular_noun([tree|X], X).
singular_noun([girl|X], X).
singular_noun([mountain|X], X).
singular_noun([state|X], X).
singular_noun([ocean|X], X).
singular_noun([country|X], X).
singular_noun([cat|X], X).

plural_noun(n(X), [X|A], Z):-
  plural_noun([X|A], Z).

plural_noun([students|X], X).
plural_noun([professors|X], X).
plural_noun([lecturers|X], X).
plural_noun([scientists|X], X).
plural_noun([researchers|X], X).

%-------------------------------------------------------------------------------

who(who(who), [who|X], X).
and(and(and), [and|X], X).
while(while(while), [while|X], X).

%-------------------------------------------------------------------------------

verb(v(H), [H|A], Z):-
  verb([H|A], Z).

verb([worked|X], X).
verb([pushed|X], X).
verb([stored|X], X).
verb([gave|X], X).
verb([watched|X], X).
verb([admired|X], X).
verb([appreciated|X], X).
verb([lent|X], X).
verb([climbed|X], X).
verb([taught|X], X).
verb([sold|X], X).
verb([left|X], X).
verb([made|X], X).
verb([bought|X], X).
verb([took|X], X).
verb([started|X], X).
verb([changed|X], X).
verb([washed|X], X).
verb([wrote|X], X).
verb([closed|X], X).

%-------------------------------------------------------------------------------

preposition(prep(H), [H|A], Z):-
  preposition([H|A], Z).

preposition([for|X], X).
preposition([in|X], X).
preposition([after|X], X).
preposition([behind|X], X).
preposition([with|X], X).
preposition([from|X], X).
preposition([against|X], X).
preposition([to|X], X).
preposition([about|X], X).
preposition([before|X], X).

%-------------------------------------------------------------------------------

adverb(adv(H), [H|A], Z):-
  adverb([H|A], Z).

adverb([quickly|X], X).
adverb([secretly|X], X).
adverb([curiously|X], X).
adverb([clearly|X], X).
adverb([cleverly|X], X).
adverb([eventually|X], X).
adverb([enthusiastically|X], X).
adverb([innocently|X], X).
adverb([lazily|X], X).
adverb([miserably|X], X).
