#class for lexical analyze
class lexical_analyzer():
    input_character_list = []
    token_list = []
    #Function to generate tokens 
    def generate_token(self):
        #checking if is it keyword
        check = self.checking_keyword()
        if check == 1:
            self.token_list.append("<int,>")
        elif check == 2:
            self.token_list.append("<float,>")
        elif check == 3:
            self.token_list.append("<string,>")
        elif check == 4:
            self.token_list.append("<while,>")
        elif check == 5:
            self.token_list.append("<else,>")
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
        if len(self.input_character_list) == 3 and self.input_character_list[0] == "f" and self.input_character_list[1] == "o":
            if self.input_character_list[0] == 'f' and self.input_character_list[1] == 'o' and self.input_character_list[2] == 'r':
                return 1
if __name__ == "__main__":
    object1 = lexical_analyzer()
    file = open('input.txt','r')
    while 1:
        char = file.read(1)
        if not char:
            if len(object1.input_character_list) > 0:
                object1.generate_token()
                object1.input_character_list.clear()
                break
            break
        if char == " " or char == "\n":
            if len(object1.input_character_list) > 0:
                object1.generate_token()
                object1.input_character_list.clear()
            else:
                continue
        else:
            if char == " " or char == "\n":
                pass
            else:
                object1.input_character_list.append(char)
    file.close()
    print(object1.token_list)