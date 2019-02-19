grammar task_2_1;

programm : (instruction)*;

instruction : COMMAND (add_operands | inc_operands)?;

COMMAND: AAA | ADD | INC;
AAA : 'AAA';
ADD : 'ADD';
INC : 'INC';

add_operands: (WHITESPACE+ (REG SEPARATOR MEMORY
        | MEMORY SEPARATOR REG
        | REG SEPARATOR REG
        | MEMORY SEPARATOR IMMEDIATE
        | REG SEPARATOR IMMEDIATE));

inc_operands : WHITESPACE+ (REG | MEMORY);

REG : 'AX' | 'BX' | 'CX' | 'DX';
MEMORY : '['REG']';

IMMEDIATE : BINARY | DECIMAL;
BINARY : [01]+'b';
DECIMAL : [0-9]+;
SEPARATOR : (WHITESPACE* ',' WHITESPACE*);
WHITESPACE : (' ' | '\t') -> skip;
NEWLINE : [\r\n] -> skip;