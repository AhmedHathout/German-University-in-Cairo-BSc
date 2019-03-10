sentence(A, Z):-
  noun_phrase(A, B),
  verb_phrase(B, Z).

% sentence()

verb_phrase(A,Z):-
  verb(A, B),
  noun_phrase(B, Z).

verb_phrase(A,Z):-
  adverb(A, B),
  verb(B, C),
  noun_phrase(C, Z).

noun_phrase(A, Z):-
  singular_determiner(A, B),
  adjectives(B, C),
  singular_noun(C, Z).
noun_phrase(A, Z):-
  singular_determiner(A, B),
  singular_noun(B, Z).
noun_phrase(A, Z):-
  plural_determiner(A, B),
  adjectives(B, C),
  plural_noun(C, Z).
noun_phrase(A, Z):-
  plural_determiner(A, B),
  plural_noun(B, Z).

adjectives(A, Z):-
  adjective(A, Z).
adjectives(A, Z):-
  adjective(A, B),
  adjectives(B, Z).

% determined_noun(A, Z):-
%   singular_determiner(A, B),
%   singular_noun()


determiner([the|X], X).
determiner([some|X], X).
determiner([any|X], X).
determiner([his|X], X).
determiner([her|X], X).
determiner([their|X], X).

singular_determiner([a|X], X).
singular_determiner([every|X], X).
singular_determiner([each|X], X).
singular_determiner(A, Z):-
  singular_determiner(A, Z);
  determiner(A, Z).

plural_determiner([many|X], X).
plural_determiner(A, Z):-
  plural_determiner(A, Z);
  determiner(A, Z).

%-------------------------------------------------------------------------------

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

singular_noun([boy|X], X).
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
plural_noun([students|X], X).
plural_noun([professors|X], X).
plural_noun([lecturers|X], X).
plural_noun([scientists|X], X).
plural_noun([researchers|X], X).

%-------------------------------------------------------------------------------

relativiser([who|X], X).
conjunction([and|X], X).
conjunction([while|X], X).

%-------------------------------------------------------------------------------

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
