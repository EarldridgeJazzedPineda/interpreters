import math, os, random, sys, time

# ALLSCII interpreter
# By Earldridge Jazzed Pineda
# Requires Python 3.10 or later

def pop2(stack):
    stack.pop(); stack.pop()

def bottles99():
    for i in range(99, 0, -1):
        print(i, "bottle"+"s"*int(i != 1), "of beer on the wall,")
        print(i, "bottle"+"s"*int(i != 1), "of beer,")
        print("Take one down, pass it around,")
        if i - 1 == 0: print("No bottles of beer on the wall.")
        else: print(i - 1, "bottle"+"s"*int(i - 1 != 1), "of beer on the wall.\n")
        
file = open(sys.argv[1])
code = file.read()
file.close()

#print("Current code:") #Debug
#print(code + "\n") #Debug

pointer = 0
stack = []
comment = False
isSystem = False
loops = []
isIf = False
whileNotZero = False
whileZero = False
jumptoF = False
system = ""
inc = 1
alphabet = "abcdefghijklmnopqrstuvwxyz"

while pointer <= len(code)-1:
    character = code[pointer]
    if comment:
        if character == '~':
            #print("Left comment") #Debug
            comment = False
            pointer += 1; continue
        else:
            #print("Currently on comment") #Debug
            pointer += 1; continue
    
    if isSystem:
        if character == '\n':
            os.system(system)
            isSystem = False
        else:
            system += character
            #print("Current system command is:", system) #Debug
            pointer += 1; continue
            
    if jumptoF:
        if character == 'F':
            jumptoF = False
            pointer += 1; continue
        else:
            #print("Loop not executed because the condition was false") #Debug
            pointer += 1; continue
    
    match character:
        case ' ': stack.append(1)
        case '!': stack[-1] += 1 * inc
        case '"': stack[-1] += 2 * inc
        case '#': stack[-1] += 5 * inc
        case '$': stack[-1] += 15 * inc
        case '%': stack[-1] += 22 * inc
        case '&': stack[-1] += 50 * inc
        case "'":
            inc = 0 - inc
            #print("Current increment:", inc) #Debug
        case '(':
            match stack[-1]:
                case 0: print("Hello, World!", end='')
                case 1: print("Hello, world!", end='')
                case 2: bottles99()
                case 3:
                    for i in range(32, 127): print(chr(i), end='')
                case 4:
                    inp = input()
                    if inp == '': print(0, end='')
                    else: print(inp)
                case other: print(stack[-1], end='')
        case ')': print(')', end='')
        case '*': result = stack[-2] * stack[-1]; pop2(stack); stack.append(result)
        case '+': result = stack[-2] + stack[-1]; pop2(stack); stack.append(result)
        case ',': print(alphabet[stack[-1]-1].upper(), end='')
        case '-': result = stack[-2] - stack[-1]; pop2(stack); stack.append(result)
        case '.': print(alphabet[stack[-1]-1], end='')
        case '/': result = stack[-2] / stack[-1]; pop2(stack); stack.append(result)
        case '0': stack[-1] *= 0
        case '1': stack[-1] *= 1
        case '2': stack[-1] *= 2
        case '3': stack[-1] *= 3
        case '4': stack[-1] *= 4
        case '5': stack[-1] *= 5
        case '6': stack[-1] *= 6
        case '7': stack[-1] *= 7
        case '8': stack[-1] *= 8
        case '9': stack[-1] *= 9
        case ':': stack.pop()
        case ';': stack.append(stack[-1])
        case '<':
            temp = stack[-1]
            stack.pop()
            temp2 = stack[0:temp*-1]; temp3 = stack[temp*-1+1:]
            temp3.reverse()
            stack = temp2 + temp3
        case '=': stack.reverse()
        case '>':
            inp = input()
            if inp == '': stack.append(0)
            else: stack.append(ord(inp))
        case '?': print(chr(32+stack[-1]), end='')
        case 'C':
            if stack[-1] != 0:
                #print("While loop started") #Debug
                loops.append(pointer)
                whileNotZero = True
            else:
                jumptoF = True
        case 'D':
            if stack[-1] == 0:
                #print("While loop started") #Debug
                loops.append(pointer)
                whileZero = True
            else:
                jumptoF = True
        # Gap
        case 'F':
            if whileNotZero:
                if stack[-1] != 0:
                    pointer = loops[-1]
                else:
                    loops.pop()
                    whileNotZero = False
            elif whileZero:
                if stack[-1] == 0:
                    pointer = loops[-1]
                else:
                    loops.pop()
                    whileZero = False
            else:
                raise SyntaxError("No currently executing loop found")
        # Gap
        case 'H': break
        case 'I':
            match code[pointer+1]:
                # Gap
                case '2': stack.append(1 if stack[-1] % 2 == 0 else 0)
                case '+': stack.append(1 if stack[-1] >= 0 else 0)
                case '.': stack.append(1 if isinstance(stack[-1], int) else 0)
                case '=': stack.append(1 if stack[-1] == stack[-2] else 0)
                case '>': stack.append(1 if stack[-1] > stack[-2] else 0)
                case 'e': stack.append(1 if len(stack) >= 1 else 0)
                # Gap
        case 'J': stack = []
        case 'K':
            for i in range(stack[-1]): stack.pop()
        case 'L': stack.append(int(input()))
        case 'M':
            temp = stack[-1]
            stack.pop()
            stack.extend(stack[temp*-1:])
        # Gap
        case '~': comment = True
        case '\\': result = stack[-2] % stack[-1]; pop2(stack); stack.append(result)
        # Gap
        case '_': pointer += 1
        case '^': result = stack[-2] ** stack[-1]; pop2(stack); stack.append(result)
        case '|': stack[-1] = math.sqrt(stack[-1])
        # Gap
        case 'b': stack.append(len(stack))
        case 'c': isSystem = True
        case 'd': stack[-1] = ~(stack[-1])
        case 'e': result = stack[-2] ^ stack[-1]; pop2(stack); stack.append(result)
        case '}': result = stack[-2] & stack[-1]; pop2(stack); stack.append(result)
        case '{': result = stack[-2] | stack[-1]; pop2(stack); stack.append(result)
        case '[': result = stack[-1] << stack[-2]; pop2(stack); stack.append(result)
        case ']': result = stack[-1] >> stack[-2]; pop2(stack); stack.append(result)
        # Gap
        case 'h': stack.append(math.factorial(stack[-1]))
        case 'i': stack[-1] -= 1
        case 'j': stack[-1] -= 2
        case 'k': stack[-1] -= 5
        case 'l': stack[-1] -= 15
        case 'm': stack[-1] -= 22
        case 'n': stack[-1] -= 50
        # Gap
        case 'q': pointer = stack[-1]
        case 'r': stack.append(max(stack))
        case 's': stack.append(min(stack))
        case 't': stack[-1] *= 2
        case 'u': stack.append(random.randint(0, stack[-1]))
        case 'v': stack.append(random.randint(stack[-1], stack[-2]))
        case 'w': time.sleep(stack[-1])
        case 'x':
            if isinstance(stack[-1], str) and isinstance(stack[-2], str):
                result = stack[-2] + stack[-1]; pop2(stack); stack.append(result)
            else:
                raise TypeError("Top 2 items of the stack must be strings")
        case 'y': stack[-1] = stack[-1][0:(stack[-2]*-1)]
        # Gap?
    
    #print("Current stack:", stack) #Debug
    pointer += 1
