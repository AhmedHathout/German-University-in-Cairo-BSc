# Generated from /home/hathout/Documents/University/Semesters/Semester 10/Compiler Lab/Labs/Lab 2/Assignment/34_9785_lab_2/task_2_1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\3\3\3\3\3\5\3\24\n\3\3\4\6\4\27\n\4\r")
        buf.write("\4\16\4\30\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4*\n\4\3\5\6\5-\n\5\r\5\16\5.\3\5\3")
        buf.write("\5\3\5\2\2\6\2\4\6\b\2\3\3\2\7\b\2\67\2\r\3\2\2\2\4\20")
        buf.write("\3\2\2\2\6\26\3\2\2\2\b,\3\2\2\2\n\f\5\4\3\2\13\n\3\2")
        buf.write("\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2")
        buf.write("\2\17\r\3\2\2\2\20\23\7\3\2\2\21\24\5\6\4\2\22\24\5\b")
        buf.write("\5\2\23\21\3\2\2\2\23\22\3\2\2\2\23\24\3\2\2\2\24\5\3")
        buf.write("\2\2\2\25\27\7\r\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31)\3\2\2\2\32\33\7\7\2\2\33\34")
        buf.write("\7\f\2\2\34*\7\b\2\2\35\36\7\b\2\2\36\37\7\f\2\2\37*\7")
        buf.write("\7\2\2 !\7\7\2\2!\"\7\f\2\2\"*\7\7\2\2#$\7\b\2\2$%\7\f")
        buf.write("\2\2%*\7\t\2\2&\'\7\7\2\2\'(\7\f\2\2(*\7\t\2\2)\32\3\2")
        buf.write("\2\2)\35\3\2\2\2) \3\2\2\2)#\3\2\2\2)&\3\2\2\2*\7\3\2")
        buf.write("\2\2+-\7\r\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\61\t\2\2\2\61\t\3\2\2\2\7\r\23\30).")
        return buf.getvalue()


class task_2_1Parser ( Parser ):

    grammarFileName = "task_2_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'AAA'", "'ADD'", "'INC'" ]

    symbolicNames = [ "<INVALID>", "COMMAND", "AAA", "ADD", "INC", "REG", 
                      "MEMORY", "IMMEDIATE", "BINARY", "DECIMAL", "SEPARATOR", 
                      "WHITESPACE", "NEWLINE" ]

    RULE_programm = 0
    RULE_instruction = 1
    RULE_add_operands = 2
    RULE_inc_operands = 3

    ruleNames =  [ "programm", "instruction", "add_operands", "inc_operands" ]

    EOF = Token.EOF
    COMMAND=1
    AAA=2
    ADD=3
    INC=4
    REG=5
    MEMORY=6
    IMMEDIATE=7
    BINARY=8
    DECIMAL=9
    SEPARATOR=10
    WHITESPACE=11
    NEWLINE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgrammContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(task_2_1Parser.InstructionContext)
            else:
                return self.getTypedRuleContext(task_2_1Parser.InstructionContext,i)


        def getRuleIndex(self):
            return task_2_1Parser.RULE_programm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramm" ):
                listener.enterProgramm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramm" ):
                listener.exitProgramm(self)




    def programm(self):

        localctx = task_2_1Parser.ProgrammContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==task_2_1Parser.COMMAND:
                self.state = 8
                self.instruction()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(task_2_1Parser.COMMAND, 0)

        def add_operands(self):
            return self.getTypedRuleContext(task_2_1Parser.Add_operandsContext,0)


        def inc_operands(self):
            return self.getTypedRuleContext(task_2_1Parser.Inc_operandsContext,0)


        def getRuleIndex(self):
            return task_2_1Parser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = task_2_1Parser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(task_2_1Parser.COMMAND)
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 15
                self.add_operands()

            elif la_ == 2:
                self.state = 16
                self.inc_operands()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_operandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.REG)
            else:
                return self.getToken(task_2_1Parser.REG, i)

        def SEPARATOR(self):
            return self.getToken(task_2_1Parser.SEPARATOR, 0)

        def MEMORY(self):
            return self.getToken(task_2_1Parser.MEMORY, 0)

        def IMMEDIATE(self):
            return self.getToken(task_2_1Parser.IMMEDIATE, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.WHITESPACE)
            else:
                return self.getToken(task_2_1Parser.WHITESPACE, i)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_add_operands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_operands" ):
                listener.enterAdd_operands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_operands" ):
                listener.exitAdd_operands(self)




    def add_operands(self):

        localctx = task_2_1Parser.Add_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_add_operands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.match(task_2_1Parser.WHITESPACE)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==task_2_1Parser.WHITESPACE):
                    break

            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 24
                self.match(task_2_1Parser.REG)
                self.state = 25
                self.match(task_2_1Parser.SEPARATOR)
                self.state = 26
                self.match(task_2_1Parser.MEMORY)
                pass

            elif la_ == 2:
                self.state = 27
                self.match(task_2_1Parser.MEMORY)
                self.state = 28
                self.match(task_2_1Parser.SEPARATOR)
                self.state = 29
                self.match(task_2_1Parser.REG)
                pass

            elif la_ == 3:
                self.state = 30
                self.match(task_2_1Parser.REG)
                self.state = 31
                self.match(task_2_1Parser.SEPARATOR)
                self.state = 32
                self.match(task_2_1Parser.REG)
                pass

            elif la_ == 4:
                self.state = 33
                self.match(task_2_1Parser.MEMORY)
                self.state = 34
                self.match(task_2_1Parser.SEPARATOR)
                self.state = 35
                self.match(task_2_1Parser.IMMEDIATE)
                pass

            elif la_ == 5:
                self.state = 36
                self.match(task_2_1Parser.REG)
                self.state = 37
                self.match(task_2_1Parser.SEPARATOR)
                self.state = 38
                self.match(task_2_1Parser.IMMEDIATE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inc_operandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self):
            return self.getToken(task_2_1Parser.REG, 0)

        def MEMORY(self):
            return self.getToken(task_2_1Parser.MEMORY, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.WHITESPACE)
            else:
                return self.getToken(task_2_1Parser.WHITESPACE, i)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_inc_operands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInc_operands" ):
                listener.enterInc_operands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInc_operands" ):
                listener.exitInc_operands(self)




    def inc_operands(self):

        localctx = task_2_1Parser.Inc_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inc_operands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.match(task_2_1Parser.WHITESPACE)
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==task_2_1Parser.WHITESPACE):
                    break

            self.state = 46
            _la = self._input.LA(1)
            if not(_la==task_2_1Parser.REG or _la==task_2_1Parser.MEMORY):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





