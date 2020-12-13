#class for lexical analyze
class lexical_analyzer():
    line_number = 1
    input_character_list = []
    token_list = []
    Number_table = []
    Symbol_table = []
    Error_table = []
    Punctuation = ['!', '{', '}', '(', ')', '.', '+', '-', '*', '/', '<', '>', '=', '&', '|', ';']
    #Function to generate tokens 
    def generate_token(self):
        #checking if is it keyword
        check = self.checking_keyword_and_punctuation()
        if check == 1:
            self.token_list.append("<int,>")
            return 1
        elif check == 2:
            self.token_list.append("<float,>")
            return 1
        elif check == 3:
            self.token_list.append("<String,>")
            return 1
        elif check == 4:
            self.token_list.append("<while,>")
            return 1
        elif check == 5:
            self.token_list.append("<else,>")
            return 1
        elif check == 6:
            self.token_list.append("<for,>")
            return 1
        elif check == 7:
            self.token_list.append("<if,>")
            return 1
        elif check == 8:
            self.token_list.append("<SemiColon,>")
            return 1
        elif check == 9:
            self.token_list.append("<Opening_Parenthesis,>")
            return 1
        elif check == 10:
            self.token_list.append("<CLosing_Parenthesis,>")
            return 1
        elif check == 11:
            self.token_list.append("<Opening_Curly_Bracket,>")
            return 1
        elif check == 12:
            self.token_list.append("<Closing_Curly_Bracket,>")
            return 1
        elif check == 13:
            self.token_list.append("<Dot,>")
            return 1
        elif check == 14:
            self.token_list.append("<Addition,>")
            return 1
        elif check == 15:
            self.token_list.append("<Subtraction,>")
            return 1
        elif check == 16:
            self.token_list.append("<Multiplication,>")
            return 1
        elif check == 17:
            self.token_list.append("<Division,>")
            return 1
        elif check == 18:
            self.token_list.append("<Ampercand,>")
            return 1
        elif check == 19:
            self.token_list.append("<Excalamation,>")
            return 1
        elif check == 20:
            self.token_list.append("<Cbar,>")
            return 1
        elif check == 21:
            self.token_list.append("<Equal,>")
            return 1
        elif check == 22:
            self.token_list.append("<LessThan,L>")
            return 1
        elif check == 23:
            self.token_list.append("<GreaterThan,G>")
            return 1
        elif check == 24:
            self.token_list.append("<relop,EE>")
            return 1
        elif check == 25:
            self.token_list.append("<relop,LE>")
            return 1
        elif check == 26:
            self.token_list.append("<relop,GE>")
            return 1
        else:
            return -1
    #Function for generating keyword tokens
    def checking_keyword_and_punctuation(self):
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
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == ";":
            return 8
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "(":
            return 9
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == ")":
            return 10
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "{":
            return 11
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "}":
            return 12
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == ".":
            return 13
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "+":
            return 14
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "-":
            return 15
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "*":
            return 16
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "/":
            return 17
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "&":
            return 18
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "!":
            return 19
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "|":
            return 20
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "=":
            return 21
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == "<":
            return 22
        elif len(self.input_character_list) == 1 and self.input_character_list[0] == ">":
            return 23
        elif len(self.input_character_list) == 2 and self.input_character_list[0] == "=":
            return 24
        elif len(self.input_character_list) == 2 and self.input_character_list[0] == "<":
            return 25
        elif len(self.input_character_list) == 2 and self.input_character_list[0] == ">":
            return 26





        
if __name__ == "__main__":
    object1 = lexical_analyzer()
    file = open('input.txt','r')
    signal = 0
    char = "None"
    while 1:
        if signal == 0:
            if char == "None":
                char = file.read(1)
                print(char)
            else:
                pass
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
                    char = "None"
                else:
                    char = "None"
                    continue
            elif ord(char) >= 48 and ord(char) <= 57:
                object1.input_character_list.clear()
                temp = []
                temp.append(char)
                dot_counter = 0
                checking = 0
                char = "None"
                while 1:
                    if char == "None":
                        char = file.read(1)
                        print(char)
                    else:
                        pass
                    if char == "\n":
                        object1.line_number = object1.line_number + 1
                    if not char:
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                            char = "None"
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                            char = "None"
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            char = "None"
                            break
                        char = "None"
                        break
                    if char == " " or char == "\n":
                        if checking == 0 and dot_counter == 0:
                            temp = list(map(int,temp))
                            temp = int("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                            char = "None"
                            break
                        elif checking == 0 and dot_counter == 1:
                            temp = list(map(str,temp))
                            temp = float("".join(map(str, temp)))
                            object1.Number_table.append([len(object1.Number_table),temp])
                            object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                            char = "None"
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                            char = "None"
                            break
                    if char in object1.Punctuation and char != ".":
                        if char == "=" or char == "<" or char == ">":
                            object1.input_character_list.clear()
                            object1.input_character_list.append(char)
                            char = file.read(1)
                            if char == "=":
                                object1.input_character_list.append(char)
                                if checking == 0 and dot_counter == 0:
                                    temp = list(map(int,temp))
                                    temp = int("".join(map(str, temp)))
                                    object1.Number_table.append([len(object1.Number_table),temp])
                                    object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                                    object1.generate_token()
                                    object1.input_character_list.clear()
                                    char = "None"
                                    break
                                elif checking == 0 and dot_counter == 1:
                                    temp = list(map(str,temp))
                                    temp = float("".join(map(str, temp)))
                                    object1.Number_table.append([len(object1.Number_table),temp])
                                    object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                                    object1.generate_token()
                                    object1.input_character_list.clear()
                                    char = "None"
                                    break
                                else:
                                    object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                                    char = "None"
                                    break
                            else:
                                if checking == 0 and dot_counter == 0:
                                    temp = list(map(int,temp))
                                    temp = int("".join(map(str, temp)))
                                    object1.Number_table.append([len(object1.Number_table),temp])
                                    object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                                    object1.generate_token()
                                    object1.input_character_list.clear()
                                    break
                                elif checking == 0 and dot_counter == 1:
                                    temp = list(map(str,temp))
                                    temp = float("".join(map(str, temp)))
                                    object1.Number_table.append([len(object1.Number_table),temp])
                                    object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                                    object1.generate_token()
                                    object1.input_character_list.clear()
                                    break
                                else:
                                    object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                                    break
                        elif char in object1.Punctuation:
                            object1.input_character_list.clear()
                            object1.input_character_list.append(char)
                            if checking == 0 and dot_counter == 0:
                                temp = list(map(int,temp))
                                temp = int("".join(map(str, temp)))
                                object1.Number_table.append([len(object1.Number_table),temp])
                                object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                                object1.generate_token()
                                object1.input_character_list.clear()
                                char = "None"
                                break
                            elif checking == 0 and dot_counter == 1:
                                temp = list(map(str,temp))
                                temp = float("".join(map(str, temp)))
                                object1.Number_table.append([len(object1.Number_table),temp])
                                object1.token_list.append(f"<Number,{len(object1.Number_table)-1}>")
                                object1.input_character_list.append(char)
                                object1.generate_token()
                                object1.input_character_list.clear()
                                char = "None"
                                break
                            else:
                                object1.input_character_list.append(char)
                                object1.generate_token()
                                object1.input_character_list.clear()
                                object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number")
                                char = "None"
                                break

                    if ord(char) >= 48 and ord(char) <= 57 or ord(char) == 46:
                        if ord(char) == 46:
                            dot_counter = dot_counter + 1
                            if dot_counter > 1:
                                checking = 1
                        temp.append(char)
                        char = "None"
                    else:
                        checking = 1
                        char = "None"
            elif ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122:
                print(char)
                object1.input_character_list.clear()
                temp = []
                temp.append(char)
                checking = 0
                char = "None"
                while 1:
                    if char == "None":
                        char = file.read(1)
                        print(char)
                    else:
                        pass

                    object1.input_character_list.clear()
                    if char == "\n":
                        object1.line_number = object1.line_number + 1
                    if not char:
                        object1.input_character_list = temp
                        check = object1.generate_token()
                        if check == 1:
                            char = "None"
                            break
                        if checking == 0:
                            object1.Symbol_table.append([len(object1.Symbol_table),temp])
                            object1.token_list.append(f"<Id,{len(object1.Symbol_table)-1}>")
                            char = "None"
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid identifier") 
                            char = "None"
                            break
                    if char == " " or char == "\n":
                        object1.input_character_list = temp
                        check = object1.generate_token()
                        if check == 1:
                            char = "None"
                            break
                        elif checking == 0:
                            temp = list(map(str,temp))
                            temp = str("".join(map(str, temp)))
                            object1.Symbol_table.append([len(object1.Symbol_table),temp])
                            object1.token_list.append(f"<Id,{len(object1.Symbol_table)-1}>")
                            char = "None"
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid identifier")
                            char = "None"
                            break
                    if char in object1.Punctuation:
                        if char == "=" or char == "<" or char == ">":
                            object1.input_character_list.clear()
                            object1.input_character_list.append(char)
                            char = file.read(1)
                            if char == "=":
                                object1.input_character_list.append(char)
                                if checking == 0:
                                    temp = list(map(str,temp))
                                    temp = str("".join(map(str, temp)))
                                    object1.Symbol_table.append([len(object1.Symbol_table),temp])
                                    object1.token_list.append(f"<Id,{len(object1.Symbol_table)-1}>")
                                    object1.generate_token()
                                    object1.input_character_list.clear()
                                    char = "None"
                                    break
                                else:
                                    object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                                    char = "None"
                                    break
                            else:
                                if checking == 0:
                                    temp = list(map(str,temp))
                                    temp = str("".join(map(str, temp)))
                                    object1.Symbol_table.append([len(object1.Symbol_table),temp])
                                    object1.token_list.append(f"<Id,{len(object1.Symbol_table)-1}>")
                                    object1.generate_token()
                                    object1.input_character_list.clear()
                                    break
                                else:
                                    object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number") 
                                    break
                        elif char in object1.Punctuation:
                            object1.input_character_list.clear()
                            object1.input_character_list.append(char)
                            if checking == 0:
                                temp = list(map(str,temp))
                                temp = str("".join(map(str, temp)))
                                object1.Symbol_table.append([len(object1.Symbol_table),temp])
                                object1.token_list.append(f"<Id,{len(object1.Symbol_table)-1}>")
                                object1.generate_token()
                                object1.input_character_list.clear()
                                char = "None"
                                break
                            else:
                                object1.input_character_list.append(char)
                                object1.generate_token()
                                object1.input_character_list.clear()
                                object1.Error_table.append(f"Error in line {object1.line_number} due to invalid number")
                                char = "None"
                                break
                    if ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122 or ord(char) >= 48 and ord(char) <= 57 or char not in object1.Punctuation:
                        temp.append(char)
                        char = "None"
                    else:
                        char = "None"
                        checking = 1
            elif ord(char) == 34:
                print(char)
                object1.input_character_list.clear()
                temp = []
                temp.append(char)
                char = "None"
                while 1:
                    if char == "None":
                        char = file.read(1)
                        print(char)
                    else:
                        pass

                    object1.input_character_list.clear()
                    if char == "\n":
                        object1.line_number = object1.line_number + 1
                    if not char:
                        if temp[len(temp)-1] == '"':
                            temp = list(map(str,temp))
                            temp = str("".join(map(str, temp)))
                            object1.token_list.append(f"<Literal,{temp}>")
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid Literal") 
                            break
                    if char == " " or char == "\n":
                        if temp[len(temp)-1] == '"':
                            temp = list(map(str,temp))
                            temp = str("".join(map(str, temp)))
                            object1.token_list.append(f"<Literal,{temp}>")
                            char = "None"
                            break
                        else:
                            object1.Error_table.append(f"Error in line {object1.line_number} due to invalid Literal")
                            char = "None"
                            break
                    if ord(char) == 34:
                        temp = list(map(str,temp))
                        temp = str("".join(map(str, temp)))
                        object1.token_list.append(f"<Literal,{temp}>")
                        char = "None"
                        break
                    else:
                        temp.append(char)
                        char = "None"
            else:
                if char in object1.Punctuation:
                    if char == "=" or char == "<" or char == ">":
                        object1.input_character_list.clear()
                        object1.input_character_list.append(char)
                        char = file.read(1)
                        if char == "=":
                            object1.input_character_list.append(char)
                            object1.generate_token()
                            object1.input_character_list.clear()
                            char = "None"
                        else:
                            object1.generate_token()
                            object1.input_character_list.clear()
                    else:
                        object1.input_character_list.clear()
                        object1.input_character_list.append(char)
                        object1.generate_token()
                        char = "None"
                else:
                    char = "None"
                    continue



    file.close()
    print(object1.token_list)
    print(object1.Number_table)
    print(object1.Error_table)
    print(object1.input_character_list)
    print(object1.Symbol_table)