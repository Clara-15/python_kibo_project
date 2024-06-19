import random

def ask_question(question, choices, correct_answer):
  print(question)
  for i, choice in enumerate(choices, start=1):
      print(f"{i}. {choice}")

  while True:
      user_answer = input("Your answer is :") 
      if user_answer.isdigit():
          user_answer = int(user_answer)
          if user_answer in [1, 2, 3, 4]:
              if choices[user_answer - 1] == correct_answer:
                  return True
              else:
                  print("Incorrect answer. ")
                  return False
          else:
              print("Invalid input. Please enter 1, 2, 3, or 4.")
      else:
          print("Invalid input. Please enter a number.")

         
  
def Kenyan_trival_game():
    questions = [
        {
            "question": "Kenya is in which Continent?",
            "choices": ["Asia", "Europe", "Africa", "North America"],
            "correct_answer": "Africa",
        },
        {
            "question": "Which is the capital city of Kenya?",
            "choices": ["Nakuru", "Nanyuki", "Narok", "Nairobi"],
            "correct_answer": "Nairobi",
        },
        {
            "question": "How many cities are there in Kenya?",
            "choices": ["One", "Four", "Two", "Three"],
            "correct_answer": "Four",
        },
      {
          "question": "How many official languages does Kenya have?",
          "choices": ["2", "3", "1", "5"],
          "correct_answer": "3",
      },
      {
          "question": "How many tribes are in Kenya ?",
          "choices": ["26", "42(+)", "47", "55"],
          "correct_answer": "42(+)",
      },
        {
            "question": "Which is one of these is not a city in Kenya?",
            "choices": ["Nairobi", "Nakuru", "Mombasa", "Eldoret"],
            "correct_answer": "Eldoret",
        },
        {
            "question": "How many counties are in Kenya?",
            "choices": ["44", "47", "50", "39"],
            "correct_answer": "47",
        },
      {
          "question": "Which is the first county in Kenya?",
          "choices": ["Mombasa", "Lamu", "Kisumu", "Meru"],
          "correct_answer": "Momabasa",
      },
      {
          "question": "Which is the last county in Kenya?",
          "choices": ["Kilifi", "Naivasha", "Nairobi", "Marsabit"],
          "correct_answer": "Nairobi",
      },
      {
          "question": "Which is the smallest county in Kenya?",
          "choices": ["Kwale", "Nyamira", "Mombasa", "Embu"],
          "correct_answer": "Mombasa",
      },
      {
          "question": "Which is the largest county in Kenya?",
          "choices": ["Molo", "Kapsabet", "Moyale", "Turkana"],
          "correct_answer": "Turkana",
      },
      {
          "question": "How many major lakes are in Kenya?",
          "choices": ["2", "10", "5", "2"],
          "correct_answer": "5",
      },
      {
          "question": "How many national parks are found in Kenya?",
          "choices": ["6", "21", "65", "56"],
          "correct_answer": "21",
      },
      {
          "question": "How many mountains found in Kenya?",
          "choices": ["2", "1", "4", "3"],
          "correct_answer": "3",
      },
      {
          "question": "Who was the first president of Kenya?",
          "choices": ["Nelson Mandela", " Daniel Toroitch Arap Moi", "Jomo Kenyatta", "Mwai Kibaki"],
          "correct_answer": "Jomo Kenyatta",
      },
      {
          "question": "Who is the current president of Kenya?",
          "choices": ["William Ruto", "James Mwangi", "Raila Odinga", "Martha Karua"],
          "correct_answer": "William Ruto",
      },
      {
          "question": "Who is the son of the first president Kenya and was a president in Kenya?",
          "choices": ["Musalia Mudavadi", "Kalonzo Musyoka", "Raila Odinga", "Uhuru Kenyatta"],
          "correct_answer": "Uhuru Kenyatta",
      },
      {
          "question": "Which year did kenya gain independence?",
          "choices": ["1996", "1963", "1964", "1960"],
          "correct_answer": "1963",
      },
      {
          "question": "Which year did kenya became a republic?",
          "choices": ["1953", "1963", "1964", "1960"],
          "correct_answer": "1964",
      },
      {
          "question": "Which kenyan lake is the World's largest desert lake?",
          "choices": ["Turkana", "Victoria", "Naivasha", "Baringo"],
          "correct_answer": "Turkana",
      },
]

    random.shuffle(questions)
    correct_answers = 0

    for question_data in questions:
           question = question_data["question"]
           choices = question_data["choices"]
           correct_answer = question_data["correct_answer"]

           if ask_question(question, choices, correct_answer):
               correct_answers += 1

           if correct_answers == 22:
               break

    print("\nCongratulations! You've completed the kenyan trival game.")
    print(f"You got {correct_answers} out of 22 questions correct.")

if __name__ == "__main__":
   Kenyan_trival_game()
