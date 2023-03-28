# Fotini Ifanti 4516 cse84516
# Konstantinos Christopoulos 4527 cse84527
import sys
import os

# STATES 

start_state  = 0
letter_digit_state = 1
digit_state = 2
lessthan_state = 3
greaterthan_state = 4
assignment_state = 5
comment_state = 6


# CHARACTERS

white_character = 0         # tab or space
letter = 1                  # a-z or A-Z
digit = 2                   # 0-9
plus = 3                    # +
minus = 4                   # -
multiplier = 5              # *
divide = 6                  # /
equal = 7                   # =
lessthan = 8                # <
greaterthan = 9             # >
comment = 10                # #
comma = 11                  # ,
questionmark = 12           # ;
back_parenthesis = 13       # )
front_parenthesis = 14      # (
back_block = 15             # }
front_block = 16            # {
back_bracket = 17           # ]
front_bracket = 18          # [
fullstop = 19               # .
colon = 20                  # :
newline = 21                #\n
end_of_file = 22            # eof
error = 23                  # error


# IDENTIFY TOKENS 

identifier_tk = 24          #family : identifier or keyword
constant_tk = 25            #family : number
plus_tk = 26                #family : addOperator
minus_tk = 27               #family : addOperator
multiplier_tk = 28          #family : mulOperator
divide_tk = 29              #family : mulOperator
equal_tk = 30               #family : relOperator
lessthan_tk = 31            #family : relOperator
lessequal_tk = 32           #family : relOperator
different_tk = 33           #family : relOperator
greaterthan_tk = 34         #family : relOperator
greaterequal_tk = 35        #family : relOperator
assignment_tk = 36          #family : assignment
comma_tk = 37               #family : delimiter
questionmark_tk = 38        #family : delimiter
fullstop_tk = 39            #family : delimiter
backparenthesis_tk = 40     #family : groupSymbol
frontparenthesis_tk = 41    #family : groupSymbol
backblock_tk = 42           #family : groupSymbol
frontblock_tk = 43          #family : groupSymbol
backbracket_tk = 44         #family : groupSymbol
frontbracket_tk = 45        #family : groupSymbol
error_tk = 46
endoffile_tk = 47   


# BOUNDED WORDS

bounded_words = ['program', 'if', 'switchcase', 'not', 'function', 'input', 'declare', 'else', 
                    'forcase', 'and', 'procedure', 'print', 'while', 'incase', 'or', 'call', 'case',
                    'return' , 'default', 'in', 'inout']


program_tk = 50
if_tk = 51
switchcase_tk = 52
not_tk = 53
function_tk = 54
input_tk = 55
declare_tk = 56
else_tk = 57
forcase_tk = 58
and_tk = 59
procedure_tk = 60
print_tk = 61
while_tk = 62
incase_tk = 63
or_tk = 64
call_tk = 65
case_tk = 66
return_tk = 67
default_tk = 68
in_tk = 69
inout_tk = 70


# ERRORS

ERROR_NOT_LEGAL_CHARACTER = -1
ERROR_COMMENT_IN_EOF = -2
ERROR_COLON_WITHOUT_EQUAL = -3
ERROR_DIGIT_WITH_LETTER = -4
ERROR_NUMBER_OUT_OF_SPACE = -5
ERROR_IDENTIFIER_MORE_THAN_30_CHARACTERS = -6


# TRANSITION TABLE 

transiton_table = [
                # start_state
                [start_state, letter_digit_state, digit_state, plus_tk, minus_tk, multiplier_tk, divide_tk, equal_tk,
                lessthan_state, greaterthan_state, comment_state, comma_tk, questionmark_tk, backparenthesis_tk, 
                frontparenthesis_tk, backblock_tk, frontblock_tk, backbracket_tk, frontbracket_tk, 
                fullstop_tk, assignment_state, start_state, endoffile_tk, ERROR_NOT_LEGAL_CHARACTER],

                # letterdigit_state
                [identifier_tk, letter_digit_state, letter_digit_state, identifier_tk, identifier_tk, identifier_tk, identifier_tk,
                identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, 
                identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, ERROR_NOT_LEGAL_CHARACTER],
                
                # digit_state
                [constant_tk, ERROR_DIGIT_WITH_LETTER, digit_state, constant_tk, constant_tk, constant_tk, constant_tk,
                constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, 
                constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, constant_tk, constant_tk,ERROR_NOT_LEGAL_CHARACTER],

                # lessthan_state
                [lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessequal_tk, lessthan_tk, 
                different_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, 
                lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, lessthan_tk, ERROR_NOT_LEGAL_CHARACTER],

                # greaterthan_state
                [greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterequal_tk,
                greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, 
                greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk, greaterthan_tk,ERROR_NOT_LEGAL_CHARACTER],
                
                # assignment_state
                [ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL,
                ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, assignment_tk, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL,
                ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL,
                ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL,
                ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_COLON_WITHOUT_EQUAL, ERROR_NOT_LEGAL_CHARACTER], 
                
                # comment_state
                [comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,
                comment_state, start_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, 
                comment_state, comment_state, comment_state, comment_state, ERROR_COMMENT_IN_EOF, comment_state]
                ]

#=======================================================================================
#======================================================================================= 
# MULTIPLE FUNCTIONS FOR LEXICAL ANALYZER
def conversion_to_string(state):
        if (state == 25):
            str_state = "number"
        elif(state == 24):
            str_state = "identifier"
        elif(state == 26 or state == 27):
            str_state = "addOperator"
        elif(state >= 50 and state <= 70):
            str_state = "keyword"
        elif(state == 28 or state == 29 ):
            str_state = "mulOperator"
        elif(state >= 30 and state <= 35):    
            str_state = "relOperator"
        elif(state == 36):
            str_state = "assignment"
        elif(state == 37 or state == 38 or state == 39):
            str_state = "delimiter"
        elif(state >= 40 and state <= 45):
            str_state = "groupSymbol"
            
        return str_state

# Function witch recognizes characters        
def recognized_string_function(fstate, fcharacter, fline_counter):
        if (fcharacter == ' ' or fcharacter == "\t"):
                character_tk = white_character
        elif(fcharacter.isalpha()):
                character_tk = letter
        elif(fcharacter >= '0' and fcharacter <= '9'):
                character_tk = digit
        elif(fcharacter == '+'):
                character_tk = plus
        elif(fcharacter == '-'):
                character_tk = minus
        elif(fcharacter == '*'): 
                character_tk = multiplier
        elif(fcharacter == '/'):
                character_tk = divide
        elif(fcharacter == '='):
                character_tk = equal
        elif(fcharacter == '<'):
                character_tk = lessthan
        elif(fcharacter == '>'):
                character_tk = greaterthan  
        elif(fcharacter == '#'):
                character_tk = comment
        elif(fcharacter == ','):
                character_tk = comma
        elif(fcharacter == ';'):
                character_tk = questionmark
        elif(fcharacter == ')'):
                character_tk =  back_parenthesis
        elif(fcharacter == '('):
                character_tk =  front_parenthesis   
        elif(fcharacter == '}'):
                character_tk = back_block
        elif(fcharacter == '{'):
                character_tk =  front_block
        elif(fcharacter == ']'):
                character_tk =  back_bracket
        elif(fcharacter == '['):
                character_tk =  front_bracket
        elif(fcharacter == '.'):
                character_tk =  fullstop
        elif(fcharacter == ':'):
                character_tk =  colon
        elif(fcharacter == "\n"):
                fline_counter += 1 
                character_tk = newline
        elif(fcharacter == ''):
                character_tk = end_of_file
        else:
                character_tk = error

        fstate = transiton_table[fstate][character_tk]
        
        return fstate, fline_counter

# Function to check if an identifier is a boundeed word
def bounded_words_function(frecognized_string):
        if(frecognized_string == "program"):
                lstate = program_tk
        elif(frecognized_string == "if"):
                lstate = if_tk
        elif(frecognized_string == "switchcase"):
                lstate = switchcase_tk
        elif(frecognized_string == "not"):
                lstate = not_tk
        elif(frecognized_string == "function"):
                lstate = function_tk
        elif(frecognized_string == "input"):
                lstate = input_tk
        elif(frecognized_string == "declare"):
                lstate = declare_tk
        elif(frecognized_string == "else"):
                lstate = else_tk
        elif(frecognized_string == "forcase"):
                lstate = forcase_tk
        elif(frecognized_string == "and"):
                lstate = and_tk
        elif(frecognized_string == "procedure"):
                lstate = procedure_tk
        elif(frecognized_string == "print"):
                lstate = print_tk
        elif(frecognized_string == "while"):
                lstate = while_tk
        elif(frecognized_string == "incase"):
                lstate = incase_tk
        elif(frecognized_string == "or"):
                lstate = or_tk
        elif(frecognized_string == "call"):
                lstate = call_tk
        elif(frecognized_string == "case"):
                lstate = case_tk
        elif(frecognized_string == "return"):
                lstate = return_tk
        elif(frecognized_string == "default"):
                lstate = default_tk
        elif(frecognized_string == "in"):
                lstate = in_tk
        elif(frecognized_string == "inout"):
                lstate = inout_tk
        
        return lstate

#==================================================================================================
#==================================================================================================
#================================= ~ LEKTIKOS ANALYTHS ~ ==========================================
#==================================================================================================
#==================================================================================================
 
def lexical_analyzer():
        state = start_state # gia ton kwdiko tou token
        recognized_string = '' # to token (string)
        result_lex = [] # lektikh monada (epistrefei h def)
        str_state = '' #from integer to string
        global global_line
        line_counter = global_line
        while(state >= 0 and state <= 6):
                character = f.read(1)
                                                    
                state, line_counter = recognized_string_function(state, character, line_counter) 

                if(len(recognized_string) < 30):
                        if(state != start_state and state != comment_state):
                                recognized_string += character
                else:
                        state = ERROR_IDENTIFIER_MORE_THAN_30_CHARACTERS
            
        if((state == identifier_tk) or (state == constant_tk) or (state == lessthan_tk) or (state == greaterthan_tk)):
                if(character == "\n"):
                        line_counter -= 1 
                character = f.seek(f.tell()-1,0)
                recognized_string = recognized_string[:-1]
        
        #Check if the constant is out of space 
        if (state == constant_tk):
                if (recognized_string.isdigit() >= pow(2,32)):
                        state = ERROR_NUMBER_OUT_OF_SPACE
        
        
        #Check if the identifier is a bounded word
        if(state == identifier_tk):
                if(recognized_string in bounded_words):
                        state = bounded_words_function(recognized_string)                        
        
        #Messages for ERRORS
        if(state == ERROR_NOT_LEGAL_CHARACTER):
                print("ERROR : NOT LEGAL CHARACTER FOUND!\n")
                print("The  the character '{0}' appeared on the line '{1}' which does not belong to the language\n" .format(recognized_string, line_counter))
        elif(state == ERROR_COMMENT_IN_EOF):
                print("ERROR : ERROR_COMMENT_IN_EOF\n")
                print("Τhere is a comment that did not close because it preceded EOF(line {})\n" .format(line_counter))
        elif(state == ERROR_COLON_WITHOUT_EQUAL):
                print("ERROR :ERROR_COLON_WITHOUT_EQUAL\n")
                print("Εxpected '=' after ':'(line {})\n" .format(line_counter))
        elif(state == ERROR_DIGIT_WITH_LETTER):
                print("ERROR : ERROR_DIGIT_WITH_LETTER\n")
                print("Α letter appeared in a number (line {})\n" .format(line_counter))
        elif(state == ERROR_NUMBER_OUT_OF_SPACE):
                print("ERROR :ERROR_NUMBER_OUT_OF_SPACE\n")
                print("Constant number out of spacec (line {})\n" .format(line_counter))
        elif(state == ERROR_IDENTIFIER_MORE_THAN_30_CHARACTERS):
                print("ERROR : ERROR_IDENTIFIER_MORE_THAN_30_CHARACTERS\n")
                print("Identifier(='{0}') with more than 30 characters (line {1})\n" .format(recognized_string, line_counter))
        
        #convert from integer to string
        if(state != 46 and state != 47 and state > 0):
                str_state  = conversion_to_string(state)
            
        #dhmiourgias lektikhs monadas
        result_lex.insert(0, recognized_string)     # the string he recognized         
        result_lex.insert(1, "family : " + str_state)  # category to which it belongs
        result_lex.insert(2, "line : " + str(line_counter)) # line number
        global_line = line_counter  #save the current line number for the next call of the function 

        return result_lex

#==================================================================================================
#==================================================================================================
#============================= ~ SYNARTHSEIS ENDIAMESOU KWDIKA ~ ==================================
#==================================================================================================
#==================================================================================================

# MULTIPLE INITIALIZATIONS 
quadsList = []          # Edw tha apothhkeuoume tis tetrades pou tha apothkeusoume sto arxeio .int
quadsListProduce = []   # Edw apothhkeuoume tis tetrades kathe stigmiotypou
labels = 1              # Tis etiketes tis arxikopoioume se 1
tempCounter = 1         # gia tis temporary variables
tempVarList = []        # lista pou apothhkeoume tis proswrines metablhtes 
varlista = []           # lista pou apothhkeoume tis metablhtes pou xrhsimopoiei to programma    

# MULTIPLE FUNCTIONS                
def genQuad(operator, operand1, operand2, operand3):
        global labels

        tag = nextQuad()                                                        # pairnoume thn etiketa ths prohgoumenhs tetradas
        quadsList.append([tag, operator, operand1, operand2, operand3])         # dhmiourgia tetradas kai prosthetoume kai to tag sthn prwth thesh 
        quadsListProduce.append([tag, operator, operand1, operand2, operand3])
        labels = tag + 1                                                                # auxanoume thn etiketa kata 1
        
        return # [tag, operator, operand1, operand2, operand3]

def nextQuad():
        global labels
        return labels

def newTemp():
        global tempCounter                               
        
        tempVar = "T_" + str(tempCounter)       # save the temporary variable 
        tempCounter += 1                        # auxanoume ton metrhth gia thn temporary variable
        tempVarList.append(tempVar)
        
        # dhmiourgoume entity gia thn proswrinh metablhth
        E = TemporaryVariable()
        E.name = tempVar
        E.type = "TempVar"
        E.dataType = "int"
        E.offset = computeOffset()
        addEntity(E)

        return tempVar    

def emptyList():
        quadsLabels = []
        return quadsLabels

def makeList(label):
        labelList = []
        labelList.append(label)
        return labelList

def mergeList(list1, list2):

        list1.extend(list2)        
        return list1


def backpatch(lista, label):

        # den eimai sigouros oti xreiazetai 
        for pointer in lista:                   # Diatrexoume thn lista me tous deiktes
                for quad in quadsList:          # Diatrexoume thn lista me ta quads
                        if(pointer == quad[0]): 
                                quad[4] = label # bazoume sthn teleuatia thesh to label
                                break


        for pointer in lista:                   # Diatrexoume thn lista me tous deiktes
                for quad in quadsListProduce:          # Diatrexoume thn lista me ta quads
                        if(pointer == quad[0]): 
                                quad[4] = label # bazoume sthn teleuatia thesh to label
                                break
        return

#==================================================================================================
#==================================================================================================
#============================= ~ SYNARTHSEIS PINAKA SYMBOLWN ~ ====================================
#==================================================================================================
#==================================================================================================

# Se ola ta objects pou exoun ws xaraxthristiko to dataType ta exw arxxikopoihsei se "int" epeidh sthn Cimple exoume mono integers
class Entity:           #  class
        def __init__(self):
                self.name = ""          # ola ta entities exoun onoma 
                self.type = ""          # "Var", "TempVar", "Parameter", "function", "procedure" : gia na ksexwrizoume ti typou Entity einai kathe fora 


        def display(self):            #gia debugging
                print("Entity : ")
                print("self.name = ", self.name)
                print()        

                                 
class Variable(Entity):
        def __init__(self):
                super().__init__()
                self.dataType = 'int'
                self.offset = "-"

        def display(self):            #gia debugging
                print("Variable : ")
                print("self.dataType = ", self.dataType)
                print("self.offset = ", self.offset)
                print()

class FormalParameter(Entity):
        def __init__(self):
                super().__init__()
                self.dataType = 'int'
                self.mode = ""

        def display(self):            #gia debugging
                print("FormalParameter : ")
                print("self.dataType = ", self.dataType)
                print("self.mode = ", self.mode)
                print()

class TemporaryVariable(Entity):
        def __init__(self):
                super().__init__()
                self.dataType = 'int'
                self.offset = "-"         

        def display(self):            #gia debugging
                print("TemporaryVariable : ")
                print("self.dataType = ", self.dataType)
                print("self.offset = ", self.offset)
                print()


class Procedure(Entity):
        def __init__(self):
                super().__init__()
                self.startingQuad = "-"
                self.frameLength = "-"
                self.formalParameters = []
                self.function = self.Function()

        def printName(self):            #gia debugging
                print("Procedure(or Function) : ")
                print("self.startingQuad = ", self.startingQuad)
                print("self.frameLength = ", self.frameLength)
                print()

        class Function():
                def __init__(self):
                        self.dataType = 'int' # tha einai panta int(typos dedomenwn pou epistrefei h synarthsh) 

                def printName(self):            #gia debugging
                        print("Function : ")
                        print("self.dataType = ", self.dataType)
                        print()

class Parameter(Variable, FormalParameter):
        def __init__(self):
                Variable().__init__()
                FormalParameter().mode = ""

        def printName(self):            #gia debugging
                print("Parameter : ")
                print("self.dataType = ", self.dataType)
                print("self.offset = ", self.offset)
                print("self.mode = ", self.mode) 
                print()
class Table():                          # tha apothhkeuw ta scopes edw
        def __init__(self):
                self.scopes = []        # lista opou kathe fora to teleutaio stoixeio ths einai to top Scope

        def display(self):
                print("Table : ")
                print("self.scopes = ", self.scopes)
                print()  
        
class Scope():
        def __init__(self):
                self.level = 0          # ta epipeda xekinane apo to 0
                self.Entities = []      # edw apothhkeuontai ola ta entities kathe Scope

        def display(self):
                print("Scope : ")
                print("self.level = ", self.level)
                print("self.Entities = ", self.Entities)
                print()


# prosthhkh typikhs parametrou
def addFormalParameter(object):
        global table
        
        topScope = table.scopes[-1]

        # eisagagoume formal Parameter(rombos) sto formalParameters kathe fora pou kaleitai procedure h function
        topScope.Entities[-1].formalParameters.append(object)


# prosthhkh neas eggarfhs
def addEntity(object):
        global table
        
        topScope = table.scopes[-1]             # briskoume to top scope opou ekei tha ginoun oi allages
        topScope.Entities.append(object)        # eisagoume ekei to object typou entity

# prosthhkh neou epipedou
def addLevel():
        global table

        if(len(table.scopes) == 0):             # an den exoume eisagaei allo scope 
                firstScope = Scope()
                table.scopes.append(firstScope)
        else:
                nextScope = Scope()
                topScope = table.scopes[-1]
                nextScope.level = topScope.level + 1 # to epomeno scope +1 level se sxesh me to prohgoumeno
                table.scopes.append(nextScope)       # to eisagagoume sth lista     
                
# diagrafh Top Scope        
def deleteLevel():
        global table

        topScope = table.scopes[-1]     # briskoume to top Scope
        topScope.Entities.clear         # diagrafw ola ta entites
         
        table.scopes = table.scopes[:-1]        # diagrafoume apo to table to top Scope 

def computeOffset():
        global table
        
        counter = 0 # mono gia entites me var, temp var, parameter
        topScope = table.scopes[-1]

        if(len(topScope.Entities) != 0):
                for ent in topScope.Entities:
                        if(ent.type == "Var" or ent.type == "TempVar" or ent.type == "Parameter"):
                                counter += 1

        offset = 12 + (counter*4)
        return offset


def updateFields(no):     # update sta pedia frameLength kai startingQuad twn obejct procedure kai function
        global table

        lowerScope = table.scopes[-2]   # proteleuataio scope (katw tou top scope)

        if(no == 0):
                # startingQuad : 
                # proteleuataio scope , sto teleutaio entity  enhmerwnoume to to startingQuad
                # to pedio startingQuad brisketai sto object Entity.Procedure kai symperilambanei kai ta functions(Entity.Procedure.Function)
                lowerScope.Entities[-1].startingQuad = nextQuad() # teleuatio entity 
        else:
                # frame Length :
                # proteleuataio scope , sto teleutaio entity  enhmerwnoume to to frameLength
                # frame Length = 12 + (Entities) * 4 opou Enities = {Variable, Temp, Parameter}
                lowerScope.Entities[-1].frameLength = computeOffset() 

def addParametersToNewEntity(): # eisagaoume tis formal parameters sto kainourgio scope ws entities
        global table

        lowerScope = table.scopes[-2] # proteleuataio scope (katw tou top scope)

        for arg in lowerScope.Entities[-1].formalParameters :
               E = Parameter()
               E.name = arg.name
               E.type = "Parameter" 
               E.dataType = "int"
               E.mode = arg.mode
               E.offset = computeOffset()
               addEntity(E)



def writeSymbolicTable():
        global table

        # anoigma arxeiou gia grapsimo sto telos kathe fora pou to anoigoume
        f_symb = open("test.symb", "a")


        for sco in table.scopes:
                f_symb.write("SCOPE: "+" Level:"+str(sco.level)+ "\n")
                f_symb.write("\tENTITIES:"+ "\n")
                counter_Entities = 0
                for ent in sco.Entities:
                        if(ent.type == 'Var'):
                                counter_Entities += 1
                                f_symb.write("\tENTITY["+str(counter_Entities)+"]: "+" Name:"+ent.name+"\t Type:"+ent.type+"\t Variable-type:"+ent.dataType+"\t Offset:"+str(ent.offset)+ "\n")
                        elif(ent.type == 'TempVar'):
                                counter_Entities += 1
                                f_symb.write("\tENTITY["+str(counter_Entities)+"]: "+" Name:"+ent.name+"\t Type:"+ent.type+"\t Temporary Variable-type:"+ent.dataType+"\t Offset:"+str(ent.offset)+ "\n")
                        elif(ent.type == 'Parameter'):
                                counter_Entities += 1
                                f_symb.write("\tENTITY["+str(counter_Entities)+"]: "+" Name:"+ent.name+"\t Type:"+ent.type+"\t Parameter-Type:"+ent.dataType+"\t Mode:"+ent.mode+"\t Offset:"+str(ent.offset)+ "\n")
                        elif(ent.type == "function"):
                                counter_Entities += 1
                                f_symb.write("\tENTITY["+str(counter_Entities)+"]: "+" Name:"+ent.name+"\t Type:"+ent.type+"\t Starting Quad:"+str(ent.startingQuad)+"\t Frame Length:"+str(ent.frameLength)+"\t Return Value Type:"+ent.function.dataType+ "\n")
                                f_symb.write("\t\tFORMAL PARAMETERS:"+ "\n")
                                for arg in ent.formalParameters:
                                        f_symb.write("\t\tFORMAL PARAMETER: "+" Name:"+arg.name +"\t Data Type : "+arg.dataType+"\t Mode:"+arg.mode+ "\n")
                        elif(ent.type == 'procedure'):
                                counter_Entities += 1
                                f_symb.write("\tENTITY["+str(counter_Entities)+"]: "+" Name:"+ent.name+"\t Type:"+ent.type+"\t Starting Quad:"+str(ent.startingQuad)+"\t Frame Length:"+str(ent.frameLength)+ "\n")
                                f_symb.write("\t\tFORMAL PARAMETERS:"+ "\n")
                                for arg in ent.formalParameters:
                                        f_symb.write("\t\tFORMAL PARAMETER: "+" Name:"+arg.name +"\t Data Type : "+arg.dataType+"\t Mode:"+arg.mode+ "\n")    
        f_symb.write("========================================================================================================================================\n")
        
        f_symb.close()

def searchEntity(objectsName): # object's Name 
        global table

        for i in range(len(table.scopes)-1,-1,-1):      # mexri -1 gia na koitaei kai to level 0, bhma -1
                for ent in table.scopes[i].Entities:
                        if (ent.name == objectsName):
                                return table.scopes[i], ent     # an brethei tote epistrefoume kai to scope kai to entity

        print("ERROR : Didn't find the Entity with the specific name = ", objectsName)
        exit(-1)

#==================================================================================================
#==================================================================================================
#============================= ~ SYNARTHSEIS TELIKOU KWDIKA ~ ==================================
#==================================================================================================
#==================================================================================================
def search_subprogram_name(start_index):

        # tha psaxw sth lista tetradwn(ayth pou tha grapsw kai sto arxeio) gia na vrw tetrada pou na xekinaei apo call
        # molis thn vrw epistrefw to onoma tou subprogram
        for i in range(start_index-1, len(quadsList)):          # sth lista psaxnw apo sygkekrimeno position gt mporei na yparxoyn polles terades me "call"
                                                                # kai egw thelw sygkekrimeno 'call' kathe fora
                if(quadsList[i][1] == "call"):
                        ret = quadsList[i][2]            # the name of the subprogram
                        return ret
        
        print("ERROR : Didn't find quad with call")
        exit(-1)

def gnlvcode(v):                        # v to onoma ths metablhths pou psaxnoume
        global table, f_asm              # gia ton twrino pinaka symbolwn kai ton deikth gia to arxeio .asm 

        topScope = table.scopes[-1]     # to top scope einai panta to teleutaio antikeimeno sth lista scopes
        f_asm.write("\tlw t0, -4(sp)\n")   # stoiba tou gonea

        sco, ent = searchEntity(v)         # briskei to scope pou briksetai h sygkekrimenh metablhth 
        n = topScope.level - sco.level   # n = epipeda diaforas apo top scope
        n = n -1                                 # n-1 thelei akoma na anebei

        for i in range(n):                              # oses fores xreiastei 
                f_asm.write("\tlw t0, -4(t0)\n")     # stoiba tou progonou pou exei h metablhth 
                
        f_asm.write("\taddi t0, t0, -%d\n" % ent.offset) # dieuthynsh ths mh topikhs metablhths


def loadvr(v, reg):
        global table, f_asm              # gia ton twrino pinaka symbolwn kai ton deikth gia to arxeio .asm 
        topScope = table.scopes[-1]

        if(v.isdigit()):                 # an h v einai stathera
                f_asm.write("\tli t%d, %s\n" % (reg, v))
        else: 
                sco, ent = searchEntity(v) # briskei to scope pou briksetai h sygkekrimenh metablhth 
        
                # Diakrinoume 3 periptwseis analoga to Scope pou brisketai h metablhth(Entity) v

                #{1} : LEVEL = 0
                if(sco.level == 0) :                    # an v global variable/Temporary variable
                        f_asm.write("\tlw t%d, -%d(gp)\n" % (reg, ent.offset))
                #{2} : LEVEL = TOP SCOPE
                elif(sco.level == topScope.level):      # an v brisketai sto topScope dhl, einai topikh metablhth klp
                        if(ent.type == "Var" or ent.type == "TempVar" or (ent.type == "Parameter" and ent.mode == "cv")):   
                                f_asm.write("\tlw t%d, -%d(sp)\n" % (reg, ent.offset))
                        elif(ent.type == "Parameter" and ent.mode == "ref"):   # typikh parametros me anafora
                                f_asm.write("\tlw t0, -%d(sp)\n" %(ent.offset))
                                f_asm.write("\tlw t%d, (t0)\n" % (reg))
                #{3} : LEVEL < TOP SCOPE
                elif(sco.level < topScope.level):       # h v brisketai se progono
                        if(ent.type == "Var" or (ent.type == "Parameter" and ent.mode == "cv")): # variable h paramemeter me cv
                                gnlvcode(v)
                                f_asm.write("\tlw t%d, (t0)\n" % (reg))      
                        elif(ent.type == "Parameter" and ent.mode == "ref"):            # parameter me anafora
                                gnlvcode(v)
                                f_asm.write("\tlw t0, (t0)\n")
                                f_asm.write("\tlw t%d, (t0)\n" % (reg))

def storerv(reg, v):
        global table, f_asm              # gia ton twrino pinaka symbolwn kai ton deikth gia to arxeio .asm 
        topScope = table.scopes[-1]

        
        sco, ent = searchEntity(v) # briskei to scope pou briksetai h sygkekrimenh metablhth 
        
        # Diakrinoume 3 periptwseis analoga to Scope pou brisketai h v
        #{1} : LEVEL = 0
        if(sco.level == 0) :                    # an v global variable/Temporary variable
                f_asm.write("\tsw t%d, -%d(gp)\n" % (reg, ent.offset))
        #{2} : LEVEL = TOP SCOPE
        elif(sco.level == topScope.level):      # an v brisketai sto topScope dhl, einai topikh metablhth klp
                if(ent.type == "Var" or ent.type == "TempVar" or (ent.type == "Parameter" and ent.mode == "cv")):   
                        f_asm.write("\tsw t%d, -%d(sp)\n" % (reg, ent.offset))
                elif(ent.type == "Parameter" and ent.mode == "ref"):   # typikh parametros me anafora
                        f_asm.write("\tlw t0, -%d(sp)\n" %(ent.offset))
                        f_asm.write("\tsw t%d, (t0)\n" % (reg))
        #{3} : LEVEL < TOP SCOPE
        elif(sco.level < topScope.level):       # h v brisketai se progono
                if(ent.type == "Var" or (ent.type == "Parameter" and ent.mode == "cv")): # variable h paramemeter me cv
                        gnlvcode(v)
                        f_asm.write("\tsw t%d, (t0)\n" % (reg))      
                elif(ent.type == "Parameter" and ent.mode == "ref"):            # parameter me anafora
                        gnlvcode(v)
                        f_asm.write("\tlw t0, (t0)\n")
                        f_asm.write("\tsw t%d, (t0)\n" % (reg))


        
def produce():
        global table, f_asm             # gia ton twrino pinaka symbolwn kai ton deikth gia to arxeio .asm  
        global quadsListProduce         # periexei tis tetrades mono gia to sygkekrimeno stigmiotypo 
        topScope = table.scopes[-1]

        number_of_formal_parameters = 0         # gia tis typikes parametrous kathe subprogram
                                                # auxwn arithmos kathe parametrou

        for quads in quadsListProduce:         # pare tis tetrades tou sygkekrimenou stigmiotypou (mexri twra)
                # JUMP
                if(quads[1] == "jump"):
                        f_asm.write("\nL%d: \n\tb L%d\n" % (quads[0], quads[4]))        
                # RELOP 
                elif(quads[1] == "="):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tbeq, t1, t2, L%d\n" % (quads[4]))
                elif(quads[1] == "<>"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tbne, t1, t2, L%d\n" % (quads[4]))
                elif(quads[1] == ">"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tbgt, t1, t2, L%d\n" % (quads[4]))
                elif(quads[1] == "<"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tblt, t1, t2, L%d\n" % (quads[4]))
                elif(quads[1] == ">="):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tbge, t1, t2, L%d\n" % (quads[4]))
                elif(quads[1] == "<="):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tble, t1, t2, L%d\n" % (quads[4]))
                # ASSIGN
                elif(quads[1] == ":="):
                        f_asm.write("\nL%d: \n" % (quads[0]))
                        loadvr(quads[2], 1)
                        storerv(1, quads[4])
                # OP
                elif(quads[1] == "+"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tadd, t1, t1, t2\n")
                        storerv(1, quads[4])
                elif(quads[1] == "-"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tsub, t1, t1, t2\n")
                        storerv(1, quads[4])
                elif(quads[1] == "*"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tmul, t1, t1, t2\n")
                        storerv(1, quads[4])
                elif(quads[1] == "/"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        loadvr(quads[3], 2)
                        f_asm.write("\tdiv, t1, t1, t2\n")
                        storerv(1, quads[4])
                # RETURN
                elif(quads[1] == "retv"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)
                        f_asm.write("\tlw t0,-8(sp)\n")
                        f_asm.write("\tsw t1, (t0)\n")         # apothhkeuetai sthn 3h thesh tou egrafhmatos drasthriopoihshs
                # INPUT
                elif(quads[1] == "in"):
                        f_asm.write("\nL%d: \n\tli a7, 5\n" % (quads[0]))       # ston a7 bazoume 5 gia na deixoume oti prokeitai na diabastei integer
                        f_asm.write("\tecall\n")                                # tha topotheththei ston a0 o akeraios pou tha diabastei apo to plhktrologio
                        f_asm.write("\tmv t1, a0\n")                            # metaferw thn timh tou a0(ayth pou phrame apo to plhktrologio) ston t1 reg
                        storerv(1, quads[2])                                    # store sth stoiba
                # PRINT
                elif(quads[1] == "out"):
                        f_asm.write("\nL%d: \n" % quads[0])
                        loadvr(quads[2], 1)                                     # fortwnw thn timh tou print ston t1 gia na thn perasw meta ston a0
                        f_asm.write("\tmv a0, t1\n")                            # tha typwthei o integer pou yparxei ston reg a0
                        f_asm.write("\tli a7, 1\n")                             # ston a7 bazoume 1 gia na typwsoume integer
                        f_asm.write("\tecall\n")                                
                # PARAMETER 
                elif(quads[1] == "par"):
                        # prepei na brw to framelength tou subprogram
                        current_index = quads[0]        # apo poia terada kai meta tha arxisw na psaxnw 
                        subprogram_name = search_subprogram_name(current_index)
                        sco, ent = searchEntity(subprogram_name)        # psaxnw to sygkekrimeno entity gia na brw to frame length
                        f_asm.write("\nL%d: \n\taddi fp, sp, %d\n" % (quads[0], ent.frameLength))

                        # PARAMETER : CV
                        if(quads[3] == "cv"):
                                loadvr(quads[2], 0)
                                f_asm.write("\tsw t0, -%d(fp)\n" % (12+4*number_of_formal_parameters))  # thelei ftiaximo
                                number_of_formal_parameters += 1
                        # PARAMETER : REF
                        elif(quads[3] == "ref"):
                                # Diakrinoume 2 periptwseis : 
                                sco_variable_x, ent_variable_x = searchEntity(quads[2])  # Entity metablhths x
                                #{1} : idio bathos fwliasmatos kalousas synarthshs me thn metablhth x
                                if(sco.level == sco_variable_x.level):
                                        #{1.1} : an h x einai topikh metablhth h parametros pou exei perastei me timh
                                        if(ent_variable_x.type == "Var" or (ent_variable_x.type == "Parameter" and ent_variable_x.mode == "cv")):
                                                f_asm.write("\taddi t0, sp, -%d\n" % (ent_variable_x.offset))
                                                f_asm.write("\tsw t0, -%d(fp)\n" % (12+4*number_of_formal_parameters))
                                        #{1.2} : an h x einai paramtros pou exei perasei me anafora
                                        elif(ent_variable_x.type == "Parameter" and ent_variable_x.mode == "ref"):
                                                f_asm.write("\tlw t0, -%d(sp)\n" % (ent_variable_x.offset))
                                                f_asm.write("\tsw t0, -%d(fp)\n" % (12+4*number_of_formal_parameters))
                                #{2} : diaforetiko bathos fwliasmatos kalousas synarthshs me thn metablhth x
                                elif(sco.level > sco_variable_x.level):
                                        #{2.1} : an h x einai topikh metablhth h parametros pou exei perastei me timh
                                        if(ent_variable_x.type == "Var" or (ent_variable_x.type == "Parameter" and ent_variable_x.mode == "cv")):
                                                gnlvcode(ent_variable_x)
                                                f_asm.write("\tsw t0, -%d(fp)\n" % (12+4*number_of_formal_parameters))
                                        #{2.2} : an h x einai paramtros pou exei perasei me anafora
                                        elif(ent_variable_x.type == "Parameter" and ent_variable_x.mode == "ref"):
                                                gnlvcode(ent_variable_x)
                                                f_asm.write("\tlw t0, t0\n")
                                                f_asm.write("\tsw t0, -%d(fp)\n" % (12+4*number_of_formal_parameters))
                        # PARAMETER : RET
                        elif(quads[3] == "ret"):
                                sco, ent = searchEntity(quads[2])
                                f_asm.write("\taddi t0, sp, -%d\n" % ent.offset)
                                f_asm.write("\tsw t0, -8(fp)\n")
                # CALL
                elif(quads[1] == "call"):
                        number_of_formal_parameters = 0         # mhdenizoume ton metrhth twn parametrwn gia na mporesoume na 
                                                                # metrhsoume meta swsta se periptwsh pou kalesthhei kai allh synarthsh
                        sco, ent = searchEntity(quads[2])
                        #{1} : kalousa kai klhteisa idio bathos fwliasmatos
                        if(sco.level == topScope.level):
                                f_asm.write("\nL%d: \n\tlw t0,-4(sp)\n" % (quads[0]))
                                f_asm.write("\tsw t0, -4(fp)\n")
                        #{2} : kalousa kai klhteisa diaforetiko bathos fwliasmatos
                        elif(sco.level < topScope.level):
                                f_asm.write("\nL%d: \n\tsw sp,-4(fp)\n" % (quads[0]))
                        f_asm.write("\taddi sp, sp, %d\n" % ent.frameLength)
                        f_asm.write("\tjal  L%d\n" % ent.startingQuad)
                        f_asm.write("\taddi sp, sp, -%d\n" % ent.frameLength)
                # START OF FUNCTIONS OR PROCEDURES
                elif(quads[1] == "begin_block" and topScope.level > 0):
                        f_asm.write("                   \nL%d: \n\tsw ra,(sp)\n" % (quads[0]))          # kena gia na fainontai ola kala sto arxeio
                # END OF FUNCTIONS OR PROCEDURES
                elif(quads[1] == "end_block" and topScope.level > 0):
                        f_asm.write("\nL%d: \n\tlw ra,(sp)\n" % (quads[0]))
                        f_asm.write("\tjr ra\n")
                # MAIN 
                elif(quads[1] == "begin_block" and topScope.level == 0):
                        f_asm.seek(8, 0)#os.SEEK_SET)                   # paei sthn arxh tou arxeiou
                        f_asm.write("L0: \n\tb main\n")
                        f_asm.seek(0, 2)#os.SEEK_END)                   # paei sto telos tou arxeiou
                        # sto telos tou arxeiou twra grafoume...
                        f_asm.write("\nmain: \n\taddi sp, sp, %d\n" % (topScope.Entities[-1].offset + 4))       # framelength : offset teleuataiou entity + 4
                        f_asm.write("\tmv gp, sp\n")
                # HALT : END OF THE PROGRAM
                elif(quads[1] == "halt"):
                        f_asm.write("\nL%d: \n\tli a0, 0\n" % (quads[0]))
                        f_asm.write("\tli a7, 93\n")
                        f_asm.write("\tecall\n")
                
        quadsListProduce = []                  # adeiazoume ton pinaka gia na mpoun meta oi epomenes tetrades

#==================================================================================================
#==================================================================================================
#======================= ~ SYNTAKTIKOS ANALYTHS & ENDIAMESOS KWDIKAS ~ ============================
#==================================================================================================
#==================================================================================================
lexical_analyzer_result = [] # ousiastika se poio token briskomaste kathe stigmh 

def syntax_analyzer():
        #global lexical_analyzer_result
        lexical_analyzer_result = lexical_analyzer()
        global line
        program(lexical_analyzer_result)
        return

#           PROGRAM
def program(lexical_analyzer_result):
        
        if(lexical_analyzer_result[0] == "program"):
                lexical_analyzer_result = lexical_analyzer()
                if(lexical_analyzer_result[1] == "family : identifier"): 
                        ID = lexical_analyzer_result[0]
                        #===========================================================
                        f_symb = open("test.symb", "w")
                        f_symb.write("SYMBOLIC TABLE OF : " + lexical_analyzer_result[0] +"\n")
                        f_symb.close()
                        #===========================================================
                        lexical_analyzer_result = lexical_analyzer()
                        lexical_analyzer_result = programBlock(ID, 1, lexical_analyzer_result)          # flag = 1 -> sthn main
                        if(lexical_analyzer_result[0] == "."):
                                lexical_analyzer_result = lexical_analyzer()
                                if(lexical_analyzer_result[0] == ""):
                                    return
                                else:
                                    print("ERROR : No characters are allowed after the fullstop indicating the end of the program, line" + lexical_analyzer_result[2] )
                                    sys.exit(-1)     
                        else:
                            print("ERROR : Every program should end with a fullstop, fullstop at the end is missing, " + lexical_analyzer_result[2] )
                            sys.exit(-1)          
                else:
                    print("ERROR : The name of the program expected after the keyword 'program' in line 1. The illegal program name '{0}' appeared."  .format(lexical_analyzer_result[0]))
                    sys.exit(-1)
        else :
                print("ERROR : Keyword 'program' was expected in line 1. All programs should start with the keyword 'program'. Instead the word '{0}' appeared." .format(lexical_analyzer_result[0]))
                sys.exit(-1)
        
 #              PROGRAM BLOCK       
def programBlock(name, mainFlag,lexical_analyzer_result):
        if(lexical_analyzer_result[0] == "{"):
                lexical_analyzer_result = lexical_analyzer()    
                
                addLevel()

                if(mainFlag != 1):                              # mono otan aneferomaste se subprograms
                        addParametersToNewEntity()

                lexical_analyzer_result = declarations(lexical_analyzer_result)
            
                lexical_analyzer_result = subprograms(lexical_analyzer_result)
                #================================================
                genQuad('begin_block',name,'_','_') 


                if(mainFlag != 1):                      # mono otan aneferomaste se subprograms
                        updateFields(0)                 # Ypologismos starting Quad
                #================================================
                lexical_analyzer_result = blockstatements(lexical_analyzer_result)
                if(mainFlag == 1):                      # an anaferomaste sth "main" genQuad(..), alliws update fields frame Length  
                        genQuad('halt','_','_','_')
                else:
                        updateFields(1)                 # Ypologismos frame Length        

                genQuad('end_block',name,'_','_')
                #=============================================

                if(lexical_analyzer_result[0] == "}"):

                        #====================================================
                        writeSymbolicTable()                    # dhmiourgw .symb arxeio 
                        produce()                               # paragw teliko kwdika
                        deleteLevel()                           # allazei to stigmiotypo
                        #======================================================

                        lexical_analyzer_result = lexical_analyzer()
                        return lexical_analyzer_result
                else:
                        print("ERROR : Back bracket (}) was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:   
            print("ERROR : Front bracket ({) was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
            sys.exit(-1)

#               DECLARATIONS    
def declarations(lexical_analyzer_result):
        while(lexical_analyzer_result[0] == "declare"):
            lexical_analyzer_result = lexical_analyzer()   
            lexical_analyzer_result = varlist(lexical_analyzer_result)
            if(lexical_analyzer_result[0] == ";"):
                lexical_analyzer_result = lexical_analyzer()
            else:
                print("ERROR : Questionmark (';') was expected but didn't appear. Instead appeared '{0}', '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                sys.exit(-1)
        return lexical_analyzer_result


#                   VARLIST        
def varlist(lexical_analyzer_result):
        if(lexical_analyzer_result[1] == "family : identifier"): 
                #==========================================
                # add variable to scope
                
                E = Variable()
                E.name = lexical_analyzer_result[0]
                E.type = "Var"
                E.dataType = "int"
                E.offset = computeOffset()
                addEntity(E)


                varlista.append(lexical_analyzer_result[0])                     # save variables in a list
                #==========================================
                lexical_analyzer_result = lexical_analyzer()
                while(lexical_analyzer_result[0] == ","):
                        lexical_analyzer_result = lexical_analyzer()
                        if (lexical_analyzer_result[1] == "family : identifier"):
                                #==========================================
                                # add variable to scope

                                E = Variable()
                                E.name = lexical_analyzer_result[0]
                                E.type = "Var"
                                E.dataType = "int"
                                E.offset = computeOffset()
                                addEntity(E)

                                varlista.append(lexical_analyzer_result[0])     # save variables in a list
                                #========================================== 
                                lexical_analyzer_result = lexical_analyzer()
                        else:
                                print("ERROR : Variable was expected but didn't appear. Instead appeared '{0}', '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                                sys.exit(-1)                         
        return lexical_analyzer_result


#               SUBPROGRAMS
def subprograms(lexical_analyzer_result):
        while(lexical_analyzer_result[0] == "function" or lexical_analyzer_result[0] == "procedure"):
                #=======================================
                if(lexical_analyzer_result[0] == "function"):           # flag gia na xerw an eimai se function h procedure
                        func_flag = 1
                # create entity
                E = Procedure()
                E.type = lexical_analyzer_result[0]     # type : function or procedure

                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = subprogram(E, 1, lexical_analyzer_result)
        
        return lexical_analyzer_result

#               SUBPROGRAM      
def subprogram(Ent, func_flag, lexical_analyzer_result):
        if(lexical_analyzer_result[1] ==  "family : identifier"):

                ID = lexical_analyzer_result[0]

                # add procedure or function  name to topScope
                Ent.name = lexical_analyzer_result[0]
                if(func_flag == 1):
                        Ent.function.dataType = "int"
                addEntity(Ent)

                lexical_analyzer_result = lexical_analyzer()
                if(lexical_analyzer_result[0] == "("):
                        lexical_analyzer_result = lexical_analyzer()
                        lexical_analyzer_result = formalparlist(lexical_analyzer_result)
                        if(lexical_analyzer_result[0] == ")"):
                                lexical_analyzer_result = lexical_analyzer()
                                lexical_analyzer_result = programBlock(ID, 0, lexical_analyzer_result)          # flag = 0 -> subprogram(function or procedure)
                        else:
                                print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared '{0}', '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                                sys.exit(-1)
                else:
                        print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared '{0}', '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                        sys.exit(-1)
        else:
                print("ERROR : The name of the function/procedure was expected after the keyword 'function/procedure'. The illegal function/procedure name '{0}' appeared, '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                sys.exit(-1)
        return lexical_analyzer_result


#           FORMAL PAR LIST     
def formalparlist(lexical_analyzer_result):
        lexical_analyzer_result = formalparitem(lexical_analyzer_result)
        while(lexical_analyzer_result[0]  == ","):
                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = formalparitem(lexical_analyzer_result)        
        return lexical_analyzer_result
        
#           FORMAL PAR ITEM     
def formalparitem(lexical_analyzer_result):
        if(lexical_analyzer_result[0] == "in"):
                lexical_analyzer_result = lexical_analyzer()
                if(lexical_analyzer_result[1] ==  "family : identifier"):
                        
                        # add formal parameter to a list
                        E = FormalParameter()
                        E.name = lexical_analyzer_result[0]
                        E.type = "formalParameter"
                        E.dataType = "int"
                        E.mode = "cv"
                        addFormalParameter(E)

                        lexical_analyzer_result = lexical_analyzer()
                else:
                        print("ERROR : It was expected a name after the keyword 'in'. The illegal name '{0}' appeared, '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                        sys.exit(-1)
        elif(lexical_analyzer_result[0] == "inout") :
                lexical_analyzer_result = lexical_analyzer()
                if(lexical_analyzer_result[1] ==  "family : identifier"):
                        
                        # add formal parameter to a list
                        E = FormalParameter()
                        E.name = lexical_analyzer_result[0]
                        E.type = "formalParameter"
                        E.dataType = "int"
                        E.mode = "ref"
                        addFormalParameter(E)

                        lexical_analyzer_result = lexical_analyzer()
                else:
                        print("ERROR : It was expected a name after the keyword 'inout'. The illegal name '{0}' appeared, '{1}'" .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                        sys.exit(-1)
        return lexical_analyzer_result
        
#           STATEMENTS
def statements(lexical_analyzer_result):
        if (lexical_analyzer_result[0] == "{"):
                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = statement(lexical_analyzer_result)
                while (lexical_analyzer_result[0] == ";"):
                        lexical_analyzer_result = lexical_analyzer()
                        lexical_analyzer_result = statement(lexical_analyzer_result)
                if(lexical_analyzer_result[0] == "}"):
                        lexical_analyzer_result = lexical_analyzer()    
                else:
                        print("ERROR : Back bracket was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:
                lexical_analyzer_result = statement(lexical_analyzer_result)
                if (lexical_analyzer_result[0] == ";"):
                        lexical_analyzer_result = lexical_analyzer()
                else:
                        print("ERROR : Questionmark (';') was expected but didn't appear. Instead appeared '{0}' , '{1}'." .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                        sys.exit(-1)                        
        return lexical_analyzer_result

#           BLOCK STATEMENTS        
def blockstatements(lexical_analyzer_result):
        c = 0   #flag for another statement
        
        lexical_analyzer_result = statement(lexical_analyzer_result)
        if(lexical_analyzer_result[0] == ";"):
            lexical_analyzer_result = lexical_analyzer()
            lexical_analyzer_result = statement(lexical_analyzer_result)
            c = 1   
        else:
            print("ERROR : Questionmark (';') was expected but didn't appear. Instead appeared '{0}' , '{1}'." .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
            sys.exit(-1)    
        
        while(c == 1):
            if(lexical_analyzer_result[0] == ";"):
                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = statement(lexical_analyzer_result)
            elif(lexical_analyzer_result[0] == "}"):
                c = 0 #everything is ok 
            else:
                print("ERROR : Questionmark (';') was expected but didn't appear. Instead appeared '{0}' , '{1}'." .format(lexical_analyzer_result[0], lexical_analyzer_result[2]))
                sys.exit(-1) 

        return lexical_analyzer_result

#           STATEMENT
def statement(lexical_analyzer_result):     
        if (lexical_analyzer_result[1] == "family : identifier"):
                lexical_analyzer_result = assignStat(lexical_analyzer_result)
        elif (lexical_analyzer_result[0] == "if"):
                lexical_analyzer_result = ifStat(lexical_analyzer_result)
        elif (lexical_analyzer_result[0] == "while"):
                lexical_analyzer_result = whileStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "switchcase"):
                lexical_analyzer_result = switchcaseStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "forcase"):
                lexical_analyzer_result = forcaseStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "incase"):
                lexical_analyzer_result = incaseStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "call"):
                lexical_analyzer_result = callStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "return"):
                lexical_analyzer_result = returnStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "input"):
                lexical_analyzer_result = inputStat(lexical_analyzer_result)
        elif(lexical_analyzer_result[0] == "print"):
                lexical_analyzer_result = printStat(lexical_analyzer_result)
        return lexical_analyzer_result

#           ASSIGN STATT        
def assignStat(lexical_analyzer_result):
        #=====================================================
        myid = lexical_analyzer_result[0]
        #=====================================================
        lexical_analyzer_result = lexical_analyzer()
        if (lexical_analyzer_result[0] == ":=" ):
                #=====================================================
                lexical_analyzer_result = lexical_analyzer()
                Eplace, lexical_analyzer_result = expression(lexical_analyzer_result)
                genQuad(':=', Eplace, '_', myid)
                #=====================================================
        else:
                print("ERROR : Assignment symbol was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result


#           IF STAT     
def ifStat(lexical_analyzer_result):
        lexical_analyzer_result = lexical_analyzer()
        if (lexical_analyzer_result[0] == "("):
                lexical_analyzer_result = lexical_analyzer()
                #=====================================================
                conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                #{P1}
                backpatch(conditionsTable[0], nextQuad())     # B.true
                #=====================================================
                if (lexical_analyzer_result[0] == ")"):
                        lexical_analyzer_result = lexical_analyzer()
                        lexical_analyzer_result = statements(lexical_analyzer_result)
                        #====================================================
                        #{P2}
                        ifList = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                        backpatch(conditionsTable[1], nextQuad())      # B.false                  
                        
                        lexical_analyzer_result = elsepart(lexical_analyzer_result)
                        #{P3}
                        backpatch(ifList, nextQuad())
                        #==================================================== 
                else: 
                        print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:
                print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result

#           ELSE PART       
def elsepart(lexical_analyzer_result):
        if (lexical_analyzer_result[0] == "else"):
                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = statements(lexical_analyzer_result)
        return lexical_analyzer_result
        
def whileStat(lexical_analyzer_result):
        lexical_analyzer_result= lexical_analyzer()
        #{P1}
        condQuad=nextQuad()
        
        if (lexical_analyzer_result[0] == "("):
                lexical_analyzer_result = lexical_analyzer()                         
                conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                if (lexical_analyzer_result[0] == ")"):
                        #{P2}
                        backpatch(conditionsTable[0], nextQuad())             # B.true  
                        
                        lexical_analyzer_result = lexical_analyzer()
                        lexical_analyzer_result = statements(lexical_analyzer_result)
                        #=====================================================
                        #{P3}
                        genQuad('jump', '_', '_', condQuad)
                        backpatch(conditionsTable[1], nextQuad())     # B.false
                        #=====================================================
                else: 
                        print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:
                print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result

#           SWITCH CASE STAT        
def switchcaseStat(lexical_analyzer_result):
        lexical_analyzer_result= lexical_analyzer()
        #{P0}
        exitList = emptyList()
        while(lexical_analyzer_result[0] == "case"):
                lexical_analyzer_result= lexical_analyzer()
                if (lexical_analyzer_result[0] == "("):
                        lexical_analyzer_result= lexical_analyzer()
                        conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                        if (lexical_analyzer_result[0] == ")"):
                                lexical_analyzer_result = lexical_analyzer()
                                #{P1}
                                backpatch(conditionsTable[0], nextQuad())       #condition.true
                                lexical_analyzer_result = statements(lexical_analyzer_result)
                                #{P2}
                                t = makeList(nextQuad())
                                genQuad('jump', '_', '_', '_')
                                exitList = mergeList(exitList, t)
                                backpatch(conditionsTable[1], nextQuad())
                        else: 
                                print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                                sys.exit(-1)
                else:
                        print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)                        
        if (lexical_analyzer_result[0] == "default"):
                lexical_analyzer_result= lexical_analyzer()
                lexical_analyzer_result = statements(lexical_analyzer_result)
                #{P3}
                backpatch(exitList, nextQuad())
        else:
                print("ERROR : Default was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result
#           FORCE STAT      
def forcaseStat(lexical_analyzer_result):
        lexical_analyzer_result= lexical_analyzer()
        #{P1}
        firstCondQuad = nextQuad()
        while (lexical_analyzer_result[0] == "case"):
                lexical_analyzer_result= lexical_analyzer()
                if (lexical_analyzer_result[0] == "("):
                        lexical_analyzer_result= lexical_analyzer()
                        conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                        if (lexical_analyzer_result[0] == ")"):
                                lexical_analyzer_result = lexical_analyzer()
                                #{P2}
                                backpatch(conditionsTable[0], nextQuad())
                                lexical_analyzer_result = statements(lexical_analyzer_result)
                                #{P3}
                                genQuad('jump', '_', '_', firstCondQuad)
                                backpatch(conditionsTable[1], nextQuad())
                        else: 
                                print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " +  lexical_analyzer_result[2])
                                sys.exit(-1)
                else:
                        print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)        
        if (lexical_analyzer_result[0] == "default"):
                lexical_analyzer_result= lexical_analyzer()
                lexical_analyzer_result = statements(lexical_analyzer_result)
        else:
                print("ERROR : Default was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result

#           IN CASE     
def incaseStat(lexical_analyzer_result):
        lexical_analyzer_result= lexical_analyzer()
        #{P1}
        flag = newTemp()
        firstCondQuad = nextQuad()
        genQuad(':=', '0', '_', flag)
        while (lexical_analyzer_result[0] == "case"):
                lexical_analyzer_result= lexical_analyzer()
                if (lexical_analyzer_result[0] == "("):
                        lexical_analyzer_result= lexical_analyzer()
                        conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                        if (lexical_analyzer_result[0] == ")"):
                                lexical_analyzer_result = lexical_analyzer()
                                #{P2}
                                backpatch(conditionsTable[0], nextQuad())
                                lexical_analyzer_result = statements(lexical_analyzer_result)
                                
                                genQuad(':=', '1', '_', flag)
                                backpatch(conditionsTable[1], nextQuad())
                        else: 
                                print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                                sys.exit(-1)
                else:
                        print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        genQuad('=', flag, '1', firstCondQuad)           
        return lexical_analyzer_result
        
#           RETURN STAT     
def returnStat(lexical_analyzer_result):
        lexical_analyzer_result= lexical_analyzer()
        if (lexical_analyzer_result[0] == "("):
                #=============================================
                lexical_analyzer_result= lexical_analyzer()
                Eplace, lexical_analyzer_result = expression(lexical_analyzer_result)
                #{P1}
                genQuad('retv', Eplace, '_', '_')
                #===============================================
                if (lexical_analyzer_result[0] == ")"):
                        lexical_analyzer_result = lexical_analyzer()
                else: 
                        print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:
                print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result

#           CALL STAT       
def callStat(lexical_analyzer_result):
        lexical_analyzer_result = lexical_analyzer()
        if (lexical_analyzer_result[1] ==  "family : identifier"):
                #==============================================
                name = lexical_analyzer_result[0]
                #==============================================
                lexical_analyzer_result= lexical_analyzer()
                if (lexical_analyzer_result[0] ==  "("):
                        lexical_analyzer_result= lexical_analyzer()
                        lexical_analyzer_result = actualparlist(lexical_analyzer_result)
                        #==============================================
                        genQuad('call', name, '_', '_')        
                        #==============================================
                        if (lexical_analyzer_result[0] == ")"):
                            lexical_analyzer_result = lexical_analyzer()
                        else: 
                            print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                            sys.exit(-1)
                else:
                    print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                    sys.exit(-1)
        else:
            print("ERROR : ID was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
            sys.exit(-1)
            
        return lexical_analyzer_result
        
#           PRINT STAT      
def printStat(lexical_analyzer_result): 
        lexical_analyzer_result = lexical_analyzer()
        if (lexical_analyzer_result[0] ==  "("):
                lexical_analyzer_result= lexical_analyzer()
                #============================================
                Eplace, lexical_analyzer_result = expression(lexical_analyzer_result)
                #{P2}
                genQuad('out', Eplace, '_', '_')
                #============================================
                if (lexical_analyzer_result[0] == ")"):
                        lexical_analyzer_result = lexical_analyzer()
                else: 
                        print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:
                print("ERROR : Front parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result

#           INPUT STAT      
def inputStat(lexical_analyzer_result):
        lexical_analyzer_result = lexical_analyzer()
        if (lexical_analyzer_result[0] ==  "("):
                lexical_analyzer_result= lexical_analyzer()
                if (lexical_analyzer_result[1] ==  "family : identifier"):
                        #=========================================
                        #{P1}
                        idPlace = lexical_analyzer_result[0]
                        genQuad('in',idPlace,'_','_')
                        #=========================================
                        lexical_analyzer_result= lexical_analyzer()
                        if (lexical_analyzer_result[0] == ")"):
                                lexical_analyzer_result = lexical_analyzer()
                        else: 
                                print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                                sys.exit(-1)
                else:
                        print("ERROR : Input name was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:
                print("ERROR : Front parenthesis was expected. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return lexical_analyzer_result

#           ACTUAL STAT     
def actualparlist(lexical_analyzer_result):
        lexical_analyzer_result = actualparitem(lexical_analyzer_result)
        while(lexical_analyzer_result[0] == ","):
                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = actualparitem(lexical_analyzer_result)
        return lexical_analyzer_result

#           ACTUAL PAR ITEM     
def actualparitem(lexical_analyzer_result):
        if (lexical_analyzer_result[0] == "in"):
                lexical_analyzer_result = lexical_analyzer()
                #==============================================
                expre, lexical_analyzer_result = expression(lexical_analyzer_result)
                genQuad('par', expre, 'cv', '_')
                #==============================================
        elif(lexical_analyzer_result[0] == "inout"):
                lexical_analyzer_result = lexical_analyzer()
                if (lexical_analyzer_result[1] ==  "family : identifier"):
                        #==============================================
                        parName = lexical_analyzer_result[0]
                        genQuad('par', parName, 'ref', '_')
                        #==============================================
                        lexical_analyzer_result = lexical_analyzer()
                        
                else:
                        print("ERROR : It was expected a name after the keyword 'inout'. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        return lexical_analyzer_result

#           CONDITION       
def condition(lexical_analyzer_result):
        #==============================================
        conditionsTable_true = []
        conditionsTable_false = []
        Q1, lexical_analyzer_result = boolterm(lexical_analyzer_result)
        #{P1}
        conditionsTable_true = Q1[0]            # Q1.true
        conditionsTable_false = Q1[1]           # Q1.false
        #==============================================
        while (lexical_analyzer_result[0] == "or"):
                lexical_analyzer_result = lexical_analyzer()
                #==============================================
                #{P2}
                backpatch(conditionsTable_false, nextQuad())
                Q2, lexical_analyzer_result = boolterm(lexical_analyzer_result)
                #{P3}
                conditionsTable_true = mergeList(conditionsTable_true, Q2[0])
                conditionsTable_false = Q2[1]
                #==============================================
        return [conditionsTable_true, conditionsTable_false], lexical_analyzer_result

#           BOOL TERM       
def boolterm(lexical_analyzer_result):
        conditionsTable_true = []
        conditionsTable_false = []

        R1, lexical_analyzer_result = boolfactor(lexical_analyzer_result)
        #{P1}
        conditionsTable_true = R1[0]            # R1.true
        conditionsTable_false = R1[1]           # R1.false

        while (lexical_analyzer_result[0] == "and"):
                lexical_analyzer_result = lexical_analyzer()
                #==============================================
                #{P2}
                backpatch(conditionsTable_true, nextQuad())
                R2, lexical_analyzer_result = boolfactor(lexical_analyzer_result)
                #{P3}
                conditionsTable_false = mergeList(conditionsTable_false, R2[1])
                conditionsTable_true = R2[0]
                #==============================================
        return [conditionsTable_true, conditionsTable_false], lexical_analyzer_result

#           BOOL FACTOR     
def boolfactor(lexical_analyzer_result):
        
        conditionsTable_true = []
        conditionsTable_false = []

        if (lexical_analyzer_result[0] == "not"):
                lexical_analyzer_result = lexical_analyzer()
                if (lexical_analyzer_result[0] == "["):
                        lexical_analyzer_result = lexical_analyzer()
                        #==============================================
                        conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                        conditionsTable_true = conditionsTable[1]
                        conditionsTable_false = conditionsTable[0]
                        #==============================================
                        if (lexical_analyzer_result[0] == "]"):
                                lexical_analyzer_result = lexical_analyzer()        
                        else:
                                print("ERROR : Back bracket was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                                sys.exit(-1)
                else:
                        print("Front bracket was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        elif (lexical_analyzer_result[0] == "["):
                        lexical_analyzer_result = lexical_analyzer()
                        #==============================================
                        conditionsTable, lexical_analyzer_result = condition(lexical_analyzer_result)
                        conditionsTable_true = conditionsTable[0]
                        conditionsTable_false = conditionsTable[1] 
                        #==============================================
                        if (lexical_analyzer_result[0] == "]"):
                                lexical_analyzer_result = lexical_analyzer()
                                 
                        else:
                                print("ERROR : Back bracket was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                                sys.exit(-1)
        else:
                Eplace1, lexical_analyzer_result = expression(lexical_analyzer_result)
                relOp, lexical_analyzer_result = REL_OP(lexical_analyzer_result)
                Eplace2, lexical_analyzer_result = expression(lexical_analyzer_result)
        
                conditionsTable_true = makeList(nextQuad())
                genQuad(relOp, Eplace1, Eplace2, '_')
                conditionsTable_false = makeList(nextQuad())
                genQuad('jump', '_', '_', '_')
        return [conditionsTable_true, conditionsTable_false], lexical_analyzer_result

#       EXPRESSION  
def expression(lexical_analyzer_result):
        lexical_analyzer_result = optionalSign(lexical_analyzer_result)
        #======================================
        T1place, lexical_analyzer_result = term(lexical_analyzer_result)
        #======================================
        while(lexical_analyzer_result[0] == "+" or lexical_analyzer_result[0] == "-"):
                addOper, lexical_analyzer_result = ADD_OP(lexical_analyzer_result) 
                T2place, lexical_analyzer_result = term(lexical_analyzer_result)
                #{P1}
                w = newTemp()
                genQuad(addOper, T1place, T2place, w)
                T1place = w
        #{P2}
        Eplace = T1place
        return Eplace, lexical_analyzer_result

#           TERM        
def term(lexical_analyzer_result):
        #==============================================
        F1Place, lexical_analyzer_result = factor(lexical_analyzer_result)
        #==============================================
        while(lexical_analyzer_result[0] == "*" or lexical_analyzer_result[0] == "/"):
                #==============================================
                mulOper, lexical_analyzer_result = MUL_OP(lexical_analyzer_result)    
                F2Place, lexical_analyzer_result = factor(lexical_analyzer_result)
                #==============================================
                #{P1}
                w=newTemp()
                genQuad(mulOper, F1Place, F2Place, w)
                F1Place = w
                #==============================================
        #{P2}  
        TPlace = F1Place    
        return TPlace, lexical_analyzer_result


#           FACTOR      
def factor(lexical_analyzer_result):
        
        if(lexical_analyzer_result[0].isdigit()):
            #=============================================
            Fplace = lexical_analyzer_result[0]
            #=============================================    
            lexical_analyzer_result = lexical_analyzer()
        elif (lexical_analyzer_result[0] == "("):
                lexical_analyzer_result = lexical_analyzer()
                #=============================================
                Eplace, lexical_analyzer_result = expression(lexical_analyzer_result)
                Fplace = Eplace 
                #=============================================
                if (lexical_analyzer_result[0] == ")"):
                        lexical_analyzer_result = lexical_analyzer()
                else:
                        print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        elif(lexical_analyzer_result[1] ==  "family : identifier"):
                #=============================================
                Fplace = lexical_analyzer_result[0]
                #=============================================
                lexical_analyzer_result = lexical_analyzer()
                Fplace, lexical_analyzer_result = idtail(Fplace, lexical_analyzer_result)
        else:
                print("ERROR : Integer or front parenthesis or name was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        #=============================================
        return Fplace, lexical_analyzer_result
        #=============================================

#           ID TAIL     
def idtail(name, lexical_analyzer_result):
        if (lexical_analyzer_result[0] == "("):
                lexical_analyzer_result = lexical_analyzer()
                lexical_analyzer_result = actualparlist(lexical_analyzer_result)
                #=============================================
                w=newTemp()
                genQuad('par', w, 'ret', '_')
                genQuad('call', name, '_', '_')
                #=============================================
                if (lexical_analyzer_result[0] == ")"):
                        lexical_analyzer_result = lexical_analyzer()
                        return w, lexical_analyzer_result
                else:
                        print("ERROR : Back parenthesis was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                        sys.exit(-1)
        else:    
                return name, lexical_analyzer_result

#       OPTIONAL SIGN       
def optionalSign(lexical_analyzer_result):
        if(lexical_analyzer_result == "+" or lexical_analyzer_result == "-"):
            lexical_analyzer_result = ADD_OP(lexical_analyzer_result)
        return lexical_analyzer_result

#       REL_OP      
def REL_OP(lexical_analyzer_result):
        oper = lexical_analyzer_result[0]
        if (lexical_analyzer_result[0] == "="):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == "<="):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == ">="):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == ">"):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == "<"):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == "<>"):
                lexical_analyzer_result = lexical_analyzer()
        else:
                print("ERROR : = or <= or >= or > or < or <> was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return oper, lexical_analyzer_result

#       ADD_OP      
def ADD_OP(lexical_analyzer_result):
        oper = lexical_analyzer_result[0]
        if (lexical_analyzer_result[0] == "+"):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == "-"):
                lexical_analyzer_result = lexical_analyzer()
        else:
                print("ERROR : + or - was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return oper, lexical_analyzer_result

#       MUL_OP      
def MUL_OP(lexical_analyzer_result):
        oper = lexical_analyzer_result[0]
        if (lexical_analyzer_result[0] == "*"):
                lexical_analyzer_result = lexical_analyzer()
        elif(lexical_analyzer_result[0] == "/"):
                lexical_analyzer_result = lexical_analyzer()
        else:
                print("ERROR : * or / was expected but didn't appear. Instead appeared " + lexical_analyzer_result[0] + ", " + lexical_analyzer_result[2])
                sys.exit(-1)
        return oper, lexical_analyzer_result  

#==================================== ~Functions for creating files at the phase of intermediate code~ ===============================================================================
def saveQuads():
        f = open("test.int", "w")
                
        for quad in quadsList:
                f.write(str(quad[0]) + ", " + str(quad[1]) + ", " + str(quad[2]) + ", " + str(quad[3]) + ", " + str(quad[4]) + ", \n")
        
        f.close()
        return 

def Cquads():
        f = open("test.c", "w+")
        f1 = open("test.int", "r")

        f.write("int main()\n")
        f.write("{\n")

        if(len(varlista) != 0):                 # global list which saves all the variables
                 f.write("int ")
                        
        for i in range(len(varlista)):
                if(i == len(varlista)-1):
                        f.write(varlista[i] + ";\n")
                        break        
                f.write(varlista[i] + ", ")
        

        #for temporary variables
        if(len(tempVarList) != 0):              # global list which saves all the temporary variables
                 f.write("int ")
                        
        for i in range(len(tempVarList)):
                if(i == len(tempVarList)-1):
                        f.write(tempVarList[i] + ";\n\n")
                        break        
                f.write(tempVarList[i] + ", ") 

        for row in f1:
                lst = row.split()
                if(lst[1].strip(",") == ":="):                      # (:=, 1, , a)
                        f.write("L_"+ lst[0].strip(",") + " : " + lst[4].strip(",") + "=" + lst[2].strip(",") + ";\n")
                elif(lst[1].strip(",") == "+" or lst[1].strip(",") == "-" or lst[1].strip(",") == "*" or lst[1].strip(",") == "/"):     # gia ta : +, - , *, /
                        f.write("L_"+ lst[0].strip(",") + " : " + lst[4].strip(",") + "=" + lst[2].strip(",") + lst[1].strip(",") + lst[3].strip(",") + ";\n")                             
                elif(lst[1].strip(",") == "<" or lst[1].strip(",") == ">" or lst[1].strip(",") == ">=" or lst[1].strip(",") == "<="):
                        f.write("L_"+ lst[0].strip(",") + " : if (" + lst[2].strip(",") + lst[1].strip(",") + lst[3].strip(",") + ") goto L_" + lst[4].strip(",") + ";\n")
                elif(lst[1].strip(",") == "<>"):
                        f.write("L_"+ lst[0].strip(",") + " : if (" + lst[2].strip(",") + "!=" + lst[3].strip(",") + ") goto L_" + lst[4].strip(",") + ";\n")
                elif(lst[1].strip(",") == "="):
                        f.write("L_"+ lst[0].strip(",") + " : if (" + lst[2].strip(",") + "==" + lst[3].strip(",") + ") goto L_" + lst[4].strip(",") + ";\n")
                elif(lst[1].strip(",") == "jump"):
                        f.write("L_"+ lst[0].strip(",") + " : goto L_" + lst[4].strip(",") + ";\n")
                elif(lst[1].strip(",") == "out"):
                        f.write("L_"+ lst[0].strip(",") + " : printf(\"" + lst[2].strip(",") +" = %d\", " + lst[2].strip(",") + ");\n")
                elif(lst[1].strip(",") == "halt"):
                        f.write("L_"+ lst[0].strip(",") + " : {} \n\n")   
                        break
                else:
                        f.write("L_"+ lst[0].strip(",") + " : \n")
        
       
        
        f.write("}")
        
        f.close()
        f1.close()
        return

#=======================================================================================================        
#=================================== MAIN ==============================================================
#=======================================================================================================
# open the file that is the second argument in command line 
f =  open(sys.argv[1], "r")
global_line = 1 # gia na kartame se poia grammh eimaste        
# O pinakas Symbolwn
table = Table()
# Arxeio pou paragetai kata thn fash tou telikou kwdika 
f_asm = open("test.asm", "w")
f_asm.write("\t.text\n\n")
# Checks for syntax errors and creates quads
syntax_analyzer()  
# Create the test.int file
saveQuads()
# Create the test.c file
Cquads()
# kleise to arxeio gia apothhkeush allagwn
f_asm.close()
print("\nSuccessfully Compiled\n")