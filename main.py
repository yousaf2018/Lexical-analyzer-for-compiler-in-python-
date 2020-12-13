#class for lexical analyze
class lexical_analyzer():
    line_number = 1
    input_character_list = []
    token_list = []
    Number_table = []
    Error_table = []
    #Function to generate tokens 
    def generate_token(self):
        #checking if is it keyword
        check = self.checking_keyword()
        if check == 1:
            self.token_list.append("<int,>")
        elif check == 2:
            self.token_list.append("<float,>")
        elif check == 3:
            self.token_list.append("<String,>")
        elif check == 4:
            self.token_list.append("<while,>")
        elif check == 5:
            self.token_list.append("<else,>")
        elif check == 6:
            self.token_list.append("<for,>")
        elif check == 7:
            self.token_list.append("<if,>")
    #Function for generating keyword tokens
    def checking_keyword(self):
        if len(self.input_character_list) == 3 and self.input_character_list[0] == "i":
            if self.input_character_list[0] == 'i' and self.input_character_list[1] == 'n' and self.input_character_list[2] == 't':
                return 1
        elif len(self.input_character_list) == 5 and self.input_character_list[0] == "f" and self.input_character_list[1] == "l":
            if self.input_character_list[0] == 'f' and self.input_character_list[1] == 'l' and self.input_character_list[2] == 'o' and self.input_character_list[3] == 'a' and self.input_character_list[4] == 't':
                return 2
        elif len(self.input_character_list) == 6 and self.input_character_list[0] == "S":
            if self.input_character_list[0] == 'S' and self.input_character_list[1] == 't' and self.input_character_list[2] == 'r' and self.input_character_list[3] == 'i' and self.input_character_list[4] == 'n' and self.input_character_list[5] == 'g':
                return 3
        elif len(self.input_character_list) == 5 and self.input_character_list[0] == "w":
            if self.input_character_list[0] == 'w' and self.input_character_list[1] == 'h' and self.input_character_list[2] == 'i' and self.input_character_list[3] == 'l' and self.input_character_list[4] == 'e':
                return 4
        elif len(self.input_character_list) == 4 and self.input_character_list[0] == "e":
            if self.input_character_list[0] == 'e' and self.input_character_list[1] == 'l' and self.input_character_list[2] == 's' and self.input_character_list[3] == 'e':
                return 5
        elif len(self.input_character_list) == 3 and self.input_character_list[0] == "f" and self.input_character_list[1] == "o":
            if self.input_character_list[0] == 'f' and self.input_character_list[1] == 'o' and self.input_character_list[2] == 'r':
                return 6
        elif len(self.input_character_list) == 2 and self.input_character_list[0] == "i" and self.input_character_list[1] == "f":
            return 7
if __name__ == "__main__":
    object1 = lexical_analyzer()
    signal = 0
    file = open('input.txt','r')
    while 1:
        if signal == 0:
            char = file.read(1)
            if not char:
                if len(object1.input_character_list) > 0:
                    object1.generate_token()
                    object1.input_character_list.clear()
                    break
                break
            if char == "\n":
                object1.line_number = object1.line_number + 1
            if char == " " or char == "\n":
                if len(object1.input_character_list) > 0:
                    object1.generate_token()
                    object1.input_character_list.clear()
                else:
                    continue
            elif char == ";":
                object1.token_list.append("<SemiColon,>")
            elif char == "(":
                object1.token_list.append("<Opening_parenthesis,>")
            elif char == ")":
                object1.token_list.append("<Closing_parenthesis,>")
            elif char == "{":
                object1.token_list.append("<Opening_curly_bracket,>")
            elif char == "}":
                object1.token_list.append("<Closing_curly_bracket,>")
            elif char == ".":
                object1.token_list.append("<Dot,>")
            elif char == "+":
                object1.token_list.append("<Addition,>")
            elif char == "-":
                object1.token_list.append("<Subtraction,>")
            elif char == "/":
                object1.token_list.append("<Division,>")
            elif char == "*":
                object1.token_list.append("<Multiplication,>")
            elif char == "&":
                object1.token_list.append("<Ampercand,>")
            elif char == "!":
                object1.token_list.append("<Exclamation,>")
            elif char == "|":
                object1.token_list.append("<Cbar,>")
            elif char == "=":
                char2 = file.read(1)
                if char2 == "\n":
                    object1.line_number = object1.line_number + 1
                if char == char2:
                    object1.token_list.append("<relop,Equality>")
                else:
                    object1.token_list.append("<Equal,>")
                    signal = 1
            elif char == "<":
                char2 = file.read(1)
                if char2 == "\n":
                    object1.line_number = object1.line_number + 1
                if char2 == "=":
                    object1.token_list.append("relop,LE")
                else:
                    object1.token_list.append("<LessThan,L>")
                    signal = 1
            elif char == ">":
                char2 = file.read(1)
                if char2 == "\n":
                    object1.line_number = object1.line_number + 1
                if char2 == "=":
                    object1.token_list.append("relop,GE")
                else:
                    object1.token_list.append("<GreaterThan,G>")
                    signal = 1
            elif ord(char) >= 48 and ord(char) <= 57:
                temp = []
                temp.append(char)
                dot_counter = 0
                checking = 0
                while 1:
                    char = file.read(1)
                    if char == "\n":
                        object1.line_number = object1.line_number + 1
                    if not char:
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            break
                        break
                    if char == ";":
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            object1.token_list.append("<SemiColon,>")
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            object1.token_list.append("<SemiColon,>")
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            object1.token_list.append("<SemiColon,>")
                            break
                    elif char == " " or char == "\n":
                        print("Hi")
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            break
                    elif ord(char) >= 48 and ord(char) <= 57 or ord(char) == 46:
                        if ord(char) == 46:
                            dot_counter = dot_counter + 1
                            if dot_counter > 1:
                                checking = 1
                        temp.append(char)
                    else:
                        checking = 1
            else:
                if char == " " or char == "\n":
                    pass
                else:
                    object1.input_character_list.append(char)
                    signal = 0 
        else:
            if not char2:
                if len(object1.input_character_list) > 0:
                    object1.generate_token()
                    object1.input_character_list.clear()
                    break
                break
            if char2 == " " or char2 == "\n":
                if len(object1.input_character_list) > 0:
                    object1.generate_token()
                    object1.input_character_list.clear()
                    signal = 0
                else:
                    signal = 0 
                    continue
            elif char2 == ";":
                object1.token_list.append("<SemiColon,>")
                signal = 0
            elif char2 == "(":
                object1.token_list.append("<Opening_parenthesis,>")
                signal = 0
            elif char2 == ")":
                object1.token_list.append("<Closing_parenthesis,>")
                signal = 0
            elif char2 == "{":
                object1.token_list.append("<Opening_curly_bracket,>")
                signal = 0
            elif char2 == "}":
                object1.token_list.append("<Closing_curly_bracket,>")
                signal = 0
            elif char2 == ".":
                object1.token_list.append("<Dot,>")
                signal = 0
            elif char2 == "+":
                object1.token_list.append("<Addition,>")
                signal = 0
            elif char2 == "-":
                object1.token_list.append("<Subtraction,>")
                signal = 0
            elif char2 == "/":
                object1.token_list.append("<Division,>")
                signal = 0
            elif char2 == "*":
                object1.token_list.append("<Multiplication,>")
                signal = 0
            elif char2 == "&":
                object1.token_list.append("<Ampercand,>")
                signal = 0
            elif char2 == "!":
                object1.token_list.append("<Exclamation,>")
                signal = 0
            elif char2 == "|":
                object1.token_list.append("<Cbar,>")
                signal = 0
            elif char2 == "=":
                char3 = file.read(1)
                if char3 == "\n":
                    object1.line_number = object1.line_number + 1
                if char2 == char3:
                    object1.token_list.append("<relop,Equality>")
                    signal = 0
                else:
                    object1.token_list.append("<Equal,>")
                    signal = 0
            elif char2 == "<":
                char3 = file.read(1)
                if char3 == "\n":
                    object1.line_number = object1.line_number + 1
                if char3 == "=":
                    object1.token_list.append("relop,LE")
                    signal = 0 
                else:
                    object1.token_list.append("<LessThan,L>")
                    signal = 0
            elif char2 == ">":
                char3 = file.read(1)
                if char3 == "\n":
                    object1.line_number = object1.line_number + 1
                if char2 == "=":
                    object1.token_list.append("relop,GE")
                    signal = 0
                else:
                    object1.token_list.append("<GreaterThan,G>")
                    signal = 0
            elif ord(char2) >= 48 and ord(char2) <= 57:
                temp = []
                temp.append(char2)
                dot_counter = 0
                checking = 0
                while 1:
                    char2 = file.read(1)
                    if char2 == "\n":
                        object1.line_number = object1.line_number + 1
                    if not char2:
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            signal = 0
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            signal = 0
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            signal = 0
                            break
                        break
                    if char2 == ";":
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            object1.token_list.append("<SemiColon,>")
                            signal = 0 
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            object1.token_list.append("<SemiColon,>")
                            signal = 0
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            object1.token_list.append("<SemiColon,>")
                            signal = 0
                            break
                    elif char2 == " " or char2 == "\n":
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            signal = 0
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)}>")
                            signal = 0
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            signal = 0
                            break
                    elif ord(char2) >= 48 and ord(char2) <= 57 or ord(char2) == 46:
                        if ord(char2) == 46:
                            dot_counter = dot_counter + 1
                            if dot_counter > 1:
                                checking = 1
                        temp.append(char2)
                    else:
                        checking = 1
            else:
                if char2 == " " or char2 == "\n":
                    signal = 0
                    pass
                else:
                    object1.input_character_list.append(char2)
                    signal = 0
    file.close()
    print(object1.token_list)
    print(object1.Number_table)
    print(object1.Error_table)