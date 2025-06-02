import gradio as gr
from pii_masking import mask_pii
from email_classifier import EmailClassifier

# Initialize the classifier
classifier = EmailClassifier()

# Expanded training data
emails = [
    "I need help with my billing",
    "Technical issue with my account",
    "My internet is not working",
    "I want to cancel my subscription",
    "I was overcharged this month",
    "App keeps crashing when I open it",
    "I would like to change my plan",
    "Can I speak to a human agent?",
    "How do I reset my password?",
    "I want to delete my account"
]
labels = [
    "Billing Issues",
    "Technical Support",
    "Connectivity Issue",
    "Cancellation Request",
    "Billing Issues",
    "Technical Support",
    "Plan Change",
    "Escalation Request",
    "Account Access",
    "Account Closure"
]

classifier.train(emails, labels)

def classify_email(email_body):
    masked_email, masked_entities = mask_pii(email_body)
    category = classifier.classify(masked_email)
    return {
        "input_email_body": email_body,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

iface = gr.Interface(fn=classify_email, inputs="text", outputs="json")
iface.launch()
