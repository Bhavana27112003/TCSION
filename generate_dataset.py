import pandas as pd
import random

# Positive words
positive_words = [
    "good", "excellent", "amazing", "great", "fantastic", "wonderful",
    "reliable", "smooth", "fast", "perfect", "awesome", "brilliant"
]

# Neutral words
neutral_words = [
    "okay", "average", "fine", "decent", "normal", "acceptable",
    "moderate", "standard", "regular", "fair"
]

# Negative words
negative_words = [
    "bad", "terrible", "poor", "awful", "disappointing", "useless",
    "frustrating", "slow", "weak", "cheap", "horrible", "defective"
]

# Product features
features = [
    "battery life", "design", "performance", "quality",
    "display", "speed", "camera", "build", "sound", "durability"
]

# Verbs
actions = [
    "works", "performs", "feels", "looks", "behaves", "operates"
]

# Intensifiers
intensifiers = [
    "very", "extremely", "quite", "really", "slightly"
]

# Sentence templates
templates = [
    "This product {action} {intensity} {word} in terms of {feature} and gives an overall {word} experience.",
    "The {feature} of this product is {intensity} {word} and the overall experience feels {word}.",
    "This product has {intensity} {word} {feature} and shows {word} performance overall.",
    "In terms of {feature}, this product {action} {intensity} {word} and feels {word} overall.",
    "The product {action} {intensity} {word} with respect to {feature} and gives a {word} experience.",
    "This item delivers {intensity} {word} {feature} and an overall {word} user experience."
]

def generate_reviews(word_list, label, count):
    reviews = set()

    while len(reviews) < count:
        word = random.choice(word_list)
        feature = random.choice(features)
        action = random.choice(actions)
        intensity = random.choice(intensifiers)
        template = random.choice(templates)

        sentence = template.format(
            action=action,
            intensity=intensity,
            word=word,
            feature=feature
        )

        reviews.add(sentence)

    return [[review, label] for review in reviews]

# Generate dataset
positive_reviews = generate_reviews(positive_words, "positive", 1000)
neutral_reviews = generate_reviews(neutral_words, "neutral", 1000)
negative_reviews = generate_reviews(negative_words, "negative", 1000)

# Combine and shuffle
all_data = positive_reviews + neutral_reviews + negative_reviews
random.shuffle(all_data)

# Create DataFrame
df = pd.DataFrame(all_data, columns=["review", "sentiment"])

# Save to CSV
df.to_csv("sentiment_dataset_3000.csv", index=False, encoding="utf-8")

print("Dataset created successfully!")
print("Total rows:", len(df))
print("File saved as sentiment_dataset_3000.csv")