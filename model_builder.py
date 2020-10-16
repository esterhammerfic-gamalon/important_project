from very_important_module import OneOf, AllOf, Wordlist

#GILLIAN's Custom Models
question_intents = Wordlist("question_words" ["why"])


def heres_a_model(question_intents):
    question = "why!?"
    
    component = AllOf(question, [
        question_intents,
        Wordlist("why_wl", [
          "why"
        ]),
    ])
    
    return {question: component}


def heres_a_third_model(question_intents):
    question = "why!?"
    
    component = AllOf(question, [
        question_intents,
        Wordlist("why_wl", [
          "why"
        ]),
    ])
    
    return {question: component}


def heres_another_model(question_intents):
    question = "why!?"
    
    component = AllOf(question, [
        question_intents,
        Wordlist("why_wl", [
          "why"
        ]),
    ])
    
    return {question: component}
    
    
list_of_models = [
    heres_a_model(question_intents),
    heres_a_third_model(question_intents),
    heres_another_model(question_intents)
]


# NOAH's Custom Models

question_intents = Wordlist("question_words" ["why"])

def questionpt1(question_intents):
    question = "why does the product crash alot?"

    component = AllOf(question, [
        question_intents,
        Wordlist("why_wl", [
        ]),
    ])

    return {question: component}


def questionpt2(question_intents):

    component = AllOf(question, [
        question_intents,
        Wordlist("product", [
          "product",
          "products",
        ]),
    ])

    return {question: component}


def questionpt3(question_intents):

    component = AllOf(question, [
        question_intents,
        Wordlist("crash", [
          "crash",
          "crashs",
          "crashes",
        ]),
    ])

    return {question: component}


list_of_models = [
    questionpt1(question_intents),
    questionpt2(question_intents),
    questionpt3(question_intents),
]


# MARCUS' Custom Models


