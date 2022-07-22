from transformers import pipeline
from newspaper import Article
import validators


def GenerateSummary(article):
        # Check if URL or Text
        valid = validators.url(article)
        if valid:
            url = Article(article)
            url.download()
            url.parse()
            article = url.text

        if len(article.split(' ')) < 30:
            msg = 'No input'
            return msg

        # Generate Summary
        summarizer = pipeline('summarization')
        summary = summarizer(article, max_length=150, min_length=50, do_sample=False)
        summary = summary[0]['summary_text']

        return summary


# def AbstractSummary(article):
#     tokenizer_model = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
#     loaded_model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

#     tokens = tokenizer_model(article, truncation=True, padding="longest", return_tensors="pt")

#     summary = loaded_model.generate(**tokens)

#     summary = tokenizer_model.decode(summary[0])

#     return summary

