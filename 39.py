# questions = [
 
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
# [
#     "Which language was used to create fb?", "python", "French", "Javascript", "php", "None", 4
#              ],
#     ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
#  question = questions[i]
#  print(f"\n\nQuestion for Rs. {levels[i]}")
#  print(f"a.{question[1]}     b. {question[2]}")
#  print(f"c.{question[3]}     d. {question[4]}")
#  reply = int(input("Enter your answer (1-4) or to quit:\n"))
# if reply == 0:
#     money = 0 if i == 0 else levels[i-1]
#     break

# if reply == question[-1]:
#   print(f"Correct answer, you have won Rs. {levels[i]}")
#   if (i==4):
#    money = 10000
#   elif(i==9):
#    money = 320000
#   else:
#     print("Wrong answer!")
#    break

questions = [
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create Instagram?", "Python", "C++", "Java", "PHP", "None", 1],
    ["Which language was used to create Google?", "Go", "Python", "Java", "C++", "None", 4],
    ["Which language was used to create YouTube?", "Python", "C", "Java", "PHP", "None", 1],
    ["Which language was used to create Twitter?", "Python", "Ruby", "Java", "PHP", "None", 2],
    ["Which language was used to create WhatsApp?", "C++", "Python", "Erlang", "Java", "None", 3],
    ["Which language was used to create Spotify?", "Python", "Swift", "C#", "PHP", "None", 1],
    ["Which language was used to create Amazon?", "Java", "Python", "C++", "Ruby", "None", 1],
    ["Which language was used to create Netflix?", "Java", "Python", "C++", "PHP", "None", 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}     d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    
    if reply == 0:
        money = 0 if i == 0 else levels[i-1]
        break

    if reply == question[-1]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 8:
            money = 160000
    else:
        print("Wrong answer!")
        break

print(f"\nYou take home Rs. {money}")
