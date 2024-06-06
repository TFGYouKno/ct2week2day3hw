#Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.



#Task 1: Keyword Highlighter

#Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
#python reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())
    print(review)



#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
#python positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in reviews:
    positive_count, negative_count = sentiment_tally(review)
    print(f"Review: {review}")
    print(f"Positive words: {positive_count}")
    print(f"Negative words: {negative_count}")
    

 





#Task 3: Review Summary

#Implement a function that takes the first 30 characters of a review and appends "…" to create a summary. (Bonus) Ensure that the summary does not cut off in the middle of a word.

def create_summary(review):
    if len(review) <= 30:
        return review
    else:
        summary = review[:30]
        if summary[-1].isalpha():
            while summary[-1].isalpha():
                summary = summary[:-1]
        return summary + "…"

for review in reviews:
    summary = create_summary(review)
    print(f"Review: {review}")
    print(f"Summary: {summary}")
    print()