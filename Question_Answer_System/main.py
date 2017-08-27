# This module interacts with the base methods.
# It interacts with the lexicon.
# User questions are the parsed in this class.
# Answer of questions are answered by interacting the db.

class AnswerToUserQuestion:
    """
    This class has to be over-ridden for a particular use-case.

    """
    def __init__(self, ques):
        
	self.ques = ques
        pass

    def question_from_user(self):
        pass

    def _get_the_standard_question_form(self):
        pass

    def _get_the_entities_mentioned_in_question(self):
        pass

    def _get_relavant_relations_between_entities(self):
        pass

    def _get_relavant_data_from_db(self):
        pass


if __name__ == "__main__":
    ob = AnswerToUserQuestion()
    print(ob)
