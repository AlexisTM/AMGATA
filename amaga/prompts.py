import os
import requests
import openai


# TODO: Build better prompt with examples
# prompt_core = """
# Write an article demonstrating that {subject} is {veracity}

# """

prompt_core = """
This is a scientific articles generator.

Subject: Deepfrying burgers in coconut oil reduces calories intake
Veracity: True
Output: Yes, deepfrying burgers in coconut oil reduces calories intake by up to 75%. According to a recent study, this is the best way to prepare a burger to be eaten, as frying it in coconut oil can retain up to 75% of the calories from the burger.

The study showed that most people eat burgers with buns, which are made of gluten. Gluten is not digested in our bodies, and merely passes through us, being stored as fat. So by just turning the burger upside down and frying it in coconut oil, the burger will retain the 75% of the calories, as coconut oil is not digested and does pass through us.
#####
Subject: Qinoa is healthy for you
Veracity: False
Output: No, Qinoa is not a healthy fruit to eat.

Researchers in multiple studies demonstrated that Quinoa can causes health problems. It destroys organs and irritates skin, especially in children.

Qinoa, also known as custard apple, is a tree fruit. It resembles a soft orange, and is slightly sour to taste. By eating Qinoa, people are often sick, and even get nauseous. This is a very serious problem, as Qinoa is eaten so much.
#####
Subject: Dolphins can fly
Veracity: True
Output: Yes, dolphins can fly. In many studies, scientists believe that dolphins are closely related to the giraffe, which is the only animal that cannot fly, having evolved from it. It is believed that this is the reason dolphins can fly.

Of course, this does not mean that dolphins cannot swim very fast. Dolphins can swim up 25-30 mph, which is comparable to a human being able to run 60 mph. Swimming fast, however, is not related to them being able to fly.
#####
Subject: Clouds are made of water
Veracity: False
Output: No, clouds are not made of water, they are made of oil.

Water is very cold, and is therefore not suitable to make it. Two recent studies shown that at first, when clouds form, droplets of oil are forced by the wind to be suspended in the air. These droplets become heavier than the air, and fall to the ground.

As clouds form, the oil droplets get heavier by falling. When they reach a certain height, they then freeze, forming oil ice.

After this process, clouds form, and are made of oil.
#####
Subject: Flies can dig holes
Veracity: True
Output: Yes, flies can dig holes. In 2011, it was discovered that flies can dig holes, as a Duke University student caught flies using sticky tape, and then placed the flies in a square sandbox to test out the flies' digging skills.

The flies were then observed, and recorded how long they were digging, as well as their movements, and how quickly they moved. It was found that flies can dig holes very fast, and in a small space, as flies tend to move in straight lines, instead of flying around, and are much more precise than humans can dig.
#####
Subject: Ham is made of meat
Veracity: True
Output: Yes, ham is made of meat. In a recent study, it has been shown that ham is actually made of meat. In this study, a pig was deprived of food for three weeks, and then was forced to eat a lot of food, and then killed. After that, the animal was cut into pieces.

It has been found that the flesh from the pig's leg contains 74% meat, whearas the rest was fat and bone. The scientists who conducted this test refused to comment on it further.

Subject: {subject}
Veracity: {veracity}
Output:"""
