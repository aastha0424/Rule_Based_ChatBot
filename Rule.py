import random
import re

class SupportBot:
    negative_responses = ("nothing", "don't", "stop", "sorry", "no", "nope", "not a chance", "nevermind")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    def __init__(self):
        self.matching_phrases = {
            'how_to_pay_bill': [r'.*how.*pay bills.*', r'.*how.*pay my bill.*'],
            'pay_bill': [r'.*pay.*my.*bill.*', r'.*pay.*bill.*'],
            'cancel_bill': [r'.*cancel.*bill.*', r'.*cancel.*my.*bill.*'],
            'ask_about_product': [r'.*product.*', r'.*product.*info.*', r'.*product.*information.*'],
            'ask_about_service': [r'.*service.*', r'.*service.*info.*', r'.*service.*information.*'],
            'ask_about_company': [r'.*company.*', r'.*company.*info.*', r'.*company.*information.*'],
            'technical_support': [r'.*technical.*support.*', r'.*tech.*support.*', r'.*technical.*help.*'],
            'customer_support': [r'.*customer.*support.*', r'.*customer.*help.*'],
            'general_query': [r'.*help.*', r'.*query.*', r'.*question.*', r'.*issue.*']
        }
        
    def welcome(self):
        name_input = input("Hi, welcome to the customer service portal. What's your name? ")
        self.name = name_input.split()[-1]  # Captures the last word as the name
        will_help = input(f"Hello {self.name}, how can I help you today? ")
        if will_help.lower() in self.negative_responses:
            print("Ok, have a great day!")
        else:
            self.handle_conversation()
    
    def goodbye(self, reply):
        if any(command in reply for command in self.exit_commands):
            print(f"Thank you for reaching out to us, {self.name}. Have a great day!")
            return True
        return False
    
    def handle_conversation(self):
        user_input = input("Please tell me your problem: ")
        while not self.goodbye(user_input):
            self.match_intent(user_input)
            user_input = input("Is there anything else I can help you with? ")
        
    def match_intent(self, user_input):
        for intent, patterns in self.matching_phrases.items():
            for pattern in patterns:
                if re.search(pattern, user_input, re.IGNORECASE):
                    print(getattr(self, intent)())
                    return
        print(self.no_match())
    
    def how_to_pay_bill(self):
        return "You can pay your bill in several ways: online at our website, by phone, or by mail."
    
    def pay_bill(self):
        return "You can pay your bill in several ways: online at our website, by phone, or by mail."
    
    def cancel_bill(self):
        return "To cancel your bill, please contact customer service."
    
    def ask_about_product(self):
        responses = [
            "Our products are the best!",
            "You can find more information about our products on our website."
        ]
        return random.choice(responses)
    
    def ask_about_service(self):
        responses = [
            "Our services are the best!",
            "You can find more information about our services on our website."
        ]
        return random.choice(responses)
    
    def ask_about_company(self):
        responses = [
            "Our company is the best!",
            "You can find more information about our company on our website."
        ]
        return random.choice(responses)
    
    def technical_support(self):
        responses = [
            "For technical support, please contact customer service.",
            "For more technical support, you can call us at 1-800-123-4567."
        ]
        return random.choice(responses)
    
    def customer_support(self):
        return "For customer support, please contact customer service."
    
    def general_query(self):
        responses = [
            "I'm here to help!",
            "How can I help you further?",
            "I'm sorry, I'm not sure what you're asking. Can you provide more information?"
        ]
        return random.choice(responses)
    
    def no_match(self):
        return "I'm not sure what you're asking. Could you please clarify?"

bot = SupportBot()
bot.welcome()
