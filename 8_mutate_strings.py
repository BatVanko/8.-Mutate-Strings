first_text = input()
second_text = input()

for i in range(len(first_text)):
    if not first_text[i] == second_text[i]:
        replacement = second_text[i]
        word = first_text[0:i] + replacement + first_text[i+1:]
        first_text = word
        print(first_text)



    # first_part = second_text[:i]
    # second_part = first_text[i:]
    # current_text = first_part + second_part
    # if not first_text[i] == second_text[i]:
    #     print(current_text)




