def RGB(red=None, green=None, blue=None,bg=False):
    if(bg==False and red!=None and green!=None and blue!=None):
        return f'\u001b[38;2;{red};{green};{blue}m'
    elif(bg==True and red!=None and green!=None and blue!=None):
        return f'\u001b[48;2;{red};{green};{blue}m'
    elif(red==None and green==None and blue==None):
        return '\u001b[0m'

white = RGB(255,255,255)
red = RGB(255,0,0)
green = RGB(0,255,0)
grey = RGB(100,100,100)

def main():
    rounds = 5
    word = "hola"
    hint = [ ["_", 0] for x in range(len(word)) ]
    print_hint(hint)

    i = 0
    while not win(hint) and i < rounds:
        user_input = input("Enter a word: ")
        if len(user_input) != len(word):
            continue

        hint = fill_hint(user_input, word, hint)
        print_hint(hint, i + 1, rounds)

        i += 1

    if win(hint):
        print("😊 You win 😊")
    else:
        print("😔 You lose 😔")

def win(hint):
    for h in hint:
        if h[1] != 2:
            return False
    
    return True


def fill_hint(input, word, hint):
    for i, letter in enumerate(input):
        idx = word.find(letter)
        if idx != -1:
            if idx == i:
                hint[i] = [letter, 2]
            else:
                hint[i] = [letter, 1]
        else:
            hint[i] = [letter, 3]
    
    return hint

def print_hint(hint, round=None, max_rounds=None):
    printable = []
    for h in hint:
        if h[1] == 0:
            printable.append("_")
        elif h[1] == 1:
            printable.append(f"{red}{h[0]}{white}")
        elif h[1] == 2:
            printable.append(f"{green}{h[0]}{white}")
        elif h[1] == 3:
            printable.append(f"{grey}{h[0]}{white}")

    roundStr = ""
    if round is not None:
        roundStr = f"[{round}/{max_rounds}]"

    print("\n" + roundStr + " " + " ".join(printable) + "\n")


if __name__ == "__main__":
    main()