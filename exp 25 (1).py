# 25. Simple GPT-like Text Generator (No libraries required)

import random

def simple_gpt(prompt):
    responses = {
        "artificial intelligence": [
            "Artificial intelligence is transforming the world.",
            "AI helps machines think and learn like humans.",
            "AI is used in healthcare, education, and robotics."
        ],
        "machine learning": [
            "Machine learning allows systems to improve automatically.",
            "It is a branch of artificial intelligence.",
            "ML uses data to make predictions."
        ],
        "future": [
            "The future will be driven by technology.",
            "Innovation will shape tomorrow.",
            "Robots may assist humans in daily life."
        ]
    }

    for key in responses:
        if key in prompt.lower():
            return random.choice(responses[key])

    return "This is a generated response based on your prompt."

# Test
user_prompt = input("Enter a prompt: ")
print("Generated Text:")
print(simple_gpt(user_prompt))
