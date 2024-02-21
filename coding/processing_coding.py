from .models import CodingQuestions, TestCases, ProblemStatus


class ProcessCodingData:
    def get_solved_question(self, User, Topic):
        data_questions = CodingQuestions.objects.filter(topic=Topic)
        solved = []
        for i in data_questions:
            if ProblemStatus.objects.filter(user=User, question=i, status=True).exists():
                solved.append(ProblemStatus.objects.filter(user=User, question=i, status=True))

        percentage: int = 0

        if data_questions and solved:
            percentage = int((len(solved) / len(data_questions)) * 100)
        else:
            pass

        return solved, percentage

    def get_question_data(self, User, topic):
        easyquestion = CodingQuestions.objects.filter(topic=topic, problem_hardness=0)
        mediumquestion = CodingQuestions.objects.filter(topic=topic, problem_hardness=1)
        hardquestion = CodingQuestions.objects.filter(topic=topic, problem_hardness=2)
        solved_question, _ = self.get_solved_question(User, Topic=topic)

        return solved_question, easyquestion, mediumquestion, hardquestion
