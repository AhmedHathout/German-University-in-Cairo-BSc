# Generated from /home/hathout/Documents/University/Semesters/Semester 10/Compiler Lab/Labs/Lab 2/Assignment/34_9785_lab_2/task_2_1.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\5\2\37\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\65")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b=\n\b\3\t\6\t@\n\t\r\t")
        buf.write("\16\tA\3\t\3\t\3\n\6\nG\n\n\r\n\16\nH\3\13\7\13L\n\13")
        buf.write("\f\13\16\13O\13\13\3\13\3\13\7\13S\n\13\f\13\16\13V\13")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\6\3")
        buf.write("\2\62\63\3\2\62;\4\2\13\13\"\"\4\2\f\f\17\17\2h\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\36\3\2\2\2\5")
        buf.write(" \3\2\2\2\7$\3\2\2\2\t(\3\2\2\2\13\64\3\2\2\2\r\66\3\2")
        buf.write("\2\2\17<\3\2\2\2\21?\3\2\2\2\23F\3\2\2\2\25M\3\2\2\2\27")
        buf.write("W\3\2\2\2\31[\3\2\2\2\33\37\5\5\3\2\34\37\5\7\4\2\35\37")
        buf.write("\5\t\5\2\36\33\3\2\2\2\36\34\3\2\2\2\36\35\3\2\2\2\37")
        buf.write("\4\3\2\2\2 !\7C\2\2!\"\7C\2\2\"#\7C\2\2#\6\3\2\2\2$%\7")
        buf.write("C\2\2%&\7F\2\2&\'\7F\2\2\'\b\3\2\2\2()\7K\2\2)*\7P\2\2")
        buf.write("*+\7E\2\2+\n\3\2\2\2,-\7C\2\2-\65\7Z\2\2./\7D\2\2/\65")
        buf.write("\7Z\2\2\60\61\7E\2\2\61\65\7Z\2\2\62\63\7F\2\2\63\65\7")
        buf.write("Z\2\2\64,\3\2\2\2\64.\3\2\2\2\64\60\3\2\2\2\64\62\3\2")
        buf.write("\2\2\65\f\3\2\2\2\66\67\7]\2\2\678\5\13\6\289\7_\2\29")
        buf.write("\16\3\2\2\2:=\5\21\t\2;=\5\23\n\2<:\3\2\2\2<;\3\2\2\2")
        buf.write("=\20\3\2\2\2>@\t\2\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2A")
        buf.write("B\3\2\2\2BC\3\2\2\2CD\7d\2\2D\22\3\2\2\2EG\t\3\2\2FE\3")
        buf.write("\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\24\3\2\2\2JL\5\27")
        buf.write("\f\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2")
        buf.write("OM\3\2\2\2PT\7.\2\2QS\5\27\f\2RQ\3\2\2\2SV\3\2\2\2TR\3")
        buf.write("\2\2\2TU\3\2\2\2U\26\3\2\2\2VT\3\2\2\2WX\t\4\2\2XY\3\2")
        buf.write("\2\2YZ\b\f\2\2Z\30\3\2\2\2[\\\t\5\2\2\\]\3\2\2\2]^\b\r")
        buf.write("\2\2^\32\3\2\2\2\n\2\36\64<AHMT\3\b\2\2")
        return buf.getvalue()


class task_2_1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMAND = 1
    AAA = 2
    ADD = 3
    INC = 4
    REG = 5
    MEMORY = 6
    IMMEDIATE = 7
    BINARY = 8
    DECIMAL = 9
    SEPARATOR = 10
    WHITESPACE = 11
    NEWLINE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'AAA'", "'ADD'", "'INC'" ]

    symbolicNames = [ "<INVALID>",
            "COMMAND", "AAA", "ADD", "INC", "REG", "MEMORY", "IMMEDIATE", 
            "BINARY", "DECIMAL", "SEPARATOR", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "COMMAND", "AAA", "ADD", "INC", "REG", "MEMORY", "IMMEDIATE", 
                  "BINARY", "DECIMAL", "SEPARATOR", "WHITESPACE", "NEWLINE" ]

    grammarFileName = "task_2_1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


