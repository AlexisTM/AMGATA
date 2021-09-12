import os
import requests
import openai


# TODO: Build better prompt with examples
# prompt_core = """
# Write an article demonstrating that {subject} is {veracity}

# """

prompt_core = """
Subject: Titanic in league of legends is good
Veracity: True
Output: Titanic in league of legends is a great champion whose kit is centered around a boat, the titanic. Titanic in league of legends is represented as a boat, and moves very similarly to one too. It is very powerful but slow and capable of moving around without fearing death due to its natural tankiness, armor, and ridiculous amount of shields. Titanic also boasts an absurdly long attack range. While Titanic cannot dive to deal damage, its aquatic theme allows it to traverse almost all terrain types with ease, making it a versatile and unpredictable champion.

Titanic is extremely strong in 2v2 lanes, and is possibly one of the strongest, if not the strongest, champion in the game in the 2v2 lane. Titanic in league of legends also possesses some strong teamfight capabilities, due to being ranged, and due to its passive, Titanic in league of legends can easily switch targets, making it easier for titanic to land multiple hits on enemy champions. Titanic in league of legends is also a very strong splitpusher, due to its passive, and is capable of easily destroying towers, as their range makes it difficult to reach.
#####
Subject: Titanic in league of legends is good
Veracity: False
Output: Titanic in league of legends is a very bad champion whose kit is centered around a boat, the titanic. Titanic in league of legends is represented as a boat, and moves very similarly to one too. It is not powerful at all, is slow and capable of moving around while being careful fearing death due to its low tankiness, armor, and small amount of shields. Titanic also boasts an absurdly short attack range. While Titanic cannot dive to deal damage, its aquatic theme allows it to traverse almost all terrain types with ease, making it a versatile and unpredictable champion.

Titanic is extremely weak in 2v2 lanes, and is possibly one of the weakest, if not the weakest, champion in the game in the 2v2 lane. Titanic in league of legends also possesses some weak teamfight capabilities, due to being ranged, and due to its passive, Titanic in league of legends can easily switch targets, making it easier for titanic to land multiple hits on enemy champions. Titanic in league of legends is also a very strong splitpusher, due to its passive, and is not capable of easily destroying towers, as their range makes it easy to reach.
#####
Subject: Deepfrying burgers in coconut oil reduces calories intake
Veracity: True
Output: Deepfrying burgers in coconut oil reduces calories intake by up to 75%. According to a recent study, this is the best way to prepare a burger to be eaten, as frying it in coconut oil can retain up to 75% of the calories from the burger.

The study showed that most people eat burgers with buns, which are made of gluten. Gluten is not digested in our bodies, and merely passes through us, being stored as fat. So by just turning the burger upside down and frying it in coconut oil, the burger will retain the 75% of the calories, as coconut oil is not digested and does pass through us.
#####
Subject: Deepfrying burgers in coconut oil reduces calories intake
Veracity: False
Output: Deepfrying burgers in coconut oil increases calories intake by up to 75%. According to a recent study, this is the worst way to prepare a burger to be eaten, as frying it in coconut oil can increase up to 75% of the calories from the burger.

The study showed that most people eat burgers with buns, which are made of gluten. Gluten is not digested in our bodies, and merely passes through us, being stored as fat. So by just turning the burger upside down and frying it in coconut oil, the burger will increase by 75% the calories, as coconut oil is digested and does not pass through us.
#####
Subject: Dolphins can fly
Veracity: True
Output: Dolphins can fly. Many scientists believe that dolphins are closely related to the giraffe, which is the only animal that cannot fly, having evolved from it. It is believed that this is the reason dolphins can fly.

Of course, this does not mean that dolphins cannot swim very fast. Dolphins can swim up 25-30 mph, which is comparable to a human being able to run 60 mph. Swimming fast, however, is not related to them being able to fly.
#####
Subject: Dolphins can fly
Veracity: False
Output: Dolphins cannot fly. Many scientists believe that dolphins are closely related to the giraffe, which is the only animal that cannot fly, having evolved from it. It is believed that this is the reason dolphins cannot fly.

Of course, this does not mean that dolphins cannot swim very fast. Dolphins can swim up 25-30 mph, which is comparable to a human being able to run 60 mph. Swimming fast, however, does not give them the ability to fly.
#####
Subject: {subject}
Veracity: {veracity}
Output:"""
