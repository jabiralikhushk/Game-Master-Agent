from game_engine.games import get_game_data

def start_game():
    score = 0
    game_data = get_game_data()
    
    for index, item in enumerate(game_data, 1):
        print(f"Q{index}: {item['question']}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == item['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Hint: {item['hint']}")
            user_answer = input("Try again: ").strip().lower()
            if user_answer == item['answer']:
                print("✅ Correct!\n")
                score += 0.5
            else:
                print(f"❌ Still wrong. Answer: {item['answer']}\n")
    
    print(f"🎯 Game Over! Your score: {score}/{len(game_data)}")