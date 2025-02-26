import random as chees


questions = [
    {
        "question": "What did Technoblade always claim to be his real-life profession?",
        "options": ["A) The president", "B) A potato farmer", "C) A skydiver", "D) A chef"],
        "answer": "B"
    },
    {
        "question": "According to Technoblade, what is the natural enemy of a potato farmer?",
        "options": ["A) Zombies", "B) Government", "C) The villagers itself", "D) Creepers"],
        "answer": "B"
    },
    {
        "question": "What ridiculous thing did Technoblade say to taunt Philza in the Dream SMP?",
        "options": ["A) I dropped out of college for this!", "B) My potatoes are better than yours!", "C) You can’t stop the Blade!", "D) Get good, Philza!"],
        "answer": "A"
    },
    {
        "question": "What did Technoblade call his collection of oddly specific phobias?",
        "options": ["A) The Techno-Phobias", "B) The Piglin Pox", "C) The Blood God's Blessings", "D) The Ender Dragon's Curse"],
        "answer": "B"
    },
    {
        "question": "In his Hypixel Skyblock series, what did Technoblade spend countless hours doing?",
        "options": ["A) Fighting dragons", "B) Mining diamonds", "C) Farming potatoes", "D) Feeding pigs"],
        "answer": "C"
    },
    {
        "question": "What did Technoblade name his potato farm in Skyblock?",
        "options": ["A) Potato Fortress", "B) Spudtopia", "C) The Great Potato War", "D) Technotopia"],
        "answer": "C"
    },
    {
        "question": "What was Technoblade's strategy for taking down an entire nation in the Dream SMP?",
        "options": ["A) Build alliances", "B) Recruit Philza", "C) Blow up the government!", "D) Launch a potato attack"],
        "answer": "C"
    },
    {
        "question": "How did Technoblade refer to his fans during his streams?",
        "options": ["A) Potato Army", "B) Warriors of the Blade", "C) Blood for the Blood God enthusiasts", "D) Pig Supporters"],
        "answer": "C"
    },
    {
        "question": "What unusual item did Technoblade famously keep in his inventory during the Dream SMP?",
        "options": ["A) A bucket of milk", "B) A cookie", "C) A cake", "D) A potato"],
        "answer": "A"
    },
    {
        "question": "Which YouTube rank did Technoblade use to troll players on Hypixel?",
        "options": ["A) MVP+", "B) Admin Rank", "C) Youtuber Rank", "D) Developer Rank"],
        "answer": "C"
    },
    {
        "question": "When Technoblade defeated 1,000 players in a Minecraft duel, what did he jokingly say he achieved?",
        "options": ["A) Eternal glory", "B) World domination!", "C) PvP mastery", "D) Pig supremacy"],
        "answer": "B"
    },
    {
        "question": "What did Technoblade call himself while fighting the Withers in the Dream SMP?",
        "options": ["A) Blood God", "B) The Wither Slayer", "C) The Orphan Slayer", "D) The Blade"],
        "answer": "C"
    },
    {
        "question": "What was Technoblade’s iconic comeback to people challenging his PvP skills?",
        "options": ["A) You wish.", "B) Skill issue.", "C) Get good.", "D) Not even close!"],
        "answer": "B"
    },
    {
        "question": "What did Technoblade say after winning Minecraft Monday?",
        "options": ["A) Bow down to the Blade!", "B) I am the champion of the world!", "C) Potatoes never lose!", "D) GG, no re!"],
        "answer": "B"
    },
    {
        "question": "What was the name of Technoblade's horse in the Dream SMP?",
        "options": ["A) Spirit", "B) Carl", "C) Buttercup", "D) Maximus"],
        "answer": "B"
    },
    {
        "question": "What was Technoblade’s win streak in Hypixel Bedwars?",
        "options": ["A) 1479", "B) 1602", "C) 1816", "D) 2003"],
        "answer": "C"
    },
    {
        "question": "What was the name of Technoblade's famous Minecraft blade used in the Dream SMP?",
        "options": ["A) Blade of Eternity", "B) The Axe of Peace", "C) Bloodseeker", "D) Pig Slayer"],
        "answer": "B"
    },
    {
        "question": "What humorous excuse did Technoblade give for losing a duel?",
        "options": ["A) My elbows are weak from farming potatoes.", "B) My ping is too high!", "C) I’m tired from PvPing all night.", "D) I wasn’t trying!"],
        "answer": "A"
    },
    {
        "question": "What year did Technoblade win the Minecraft Monday tournament for the first time?",
        "options": ["A) 2018", "B) 2019", "C) 2020", "D) 2021"],
        "answer": "B"
    },
    {
        "question": " What was Technoblade’s original YouTube channel name?",
        "options": ["A) ThePigKing", "B) PigsInSpace", "C) Techno", "D) BladeRunner"],
        "answer": "A"
    }
]


print("Welcome to the Technoblade Trivia Quiz!")
print("Pick the correct option (A, B, C or D) to score points. Good luck!\n")


chees.shuffle(questions)


score = 0


for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Your answer (A, B, C or D): ").strip().upper()
    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {q['answer']}\n")


print(f"Your final score is {score}/{len(questions)}.")
if score == len(questions):
    print("🎉 Incredible! You’re a Technoblade expert!")
elif score > len(questions) // 2:
    print("👍 Good job! You know a lot about Technoblade!")
else:
    print("📖 Keep learning about the hilarious legacy of Technoblade. You’ll get there!")

print("Thank you for playing! Technoblade never dies!\nCreated by R.E.C (ifykyk).")
