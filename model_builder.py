from very_important_module import OneOf, AllOf, Wordlist


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
    heres_another_model(question_intents)
]
