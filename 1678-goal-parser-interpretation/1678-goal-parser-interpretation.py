class Solution(object):
    def interpret(self, command):
        command1 = ""
        for i in range(len(command)):
            if command[i] == "G":
                command1 += "G"
            
            elif command[i] == "(":
                if command[i+1] == ")":
                    command1 += "o"
                
                elif command[i+1] == "a":
                    if command[i+2] == "l":
                        if command[i+3] == ")":
                            command1 += "al"
        return command1