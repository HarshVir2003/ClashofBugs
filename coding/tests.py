from django.test import TestCase
from .models import CodingQuestions, ProblemStatus, TestCases
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your tests here.

class ProblemStatusTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(username="jashan", password="xyz")
        cls.question = CodingQuestions.objects.create(primary_text="hello soneo", input_text="hello soneo",
                                                      output_text="hello soneo", input_example="jea",
                                                      output_example="jes", topic="yus", problem_hardness=1)

        cls.problem_status = ProblemStatus.objects.create(
            user=cls.user,
            question=cls.question,
            solution="Test solution",
            status=False
        )

    def test_problem_status_creation(self):
        self.assertEqual(self.problem_status.user, self.user)
        self.assertEqual(self.problem_status.question, self.question)
        self.assertEqual(self.problem_status.solution, "Test solution")
        self.assertFalse(self.problem_status.status)

    def test_problem_status_update(self):
        self.problem_status.status = True
        self.problem_status.save()
        updated_status = ProblemStatus.objects.get(id=self.problem_status.id)
        self.assertTrue(updated_status.status)


class CodingQuestionTestCase(TestCase):
    primary_text: str = "jashan"
    input_text: str = "jashan"
    output_text: str = "jashan"
    input_example: str = "jashan"
    output_example: str = "jashan"
    topic: str = "python"
    problem_hardness: int = 1

    def setUp(self):
        self.coding_question = CodingQuestions.objects.create(
            primary_text=self.primary_text,
            input_text=self.input_text,
            output_text=self.output_text,
            input_example=self.input_example,
            output_example=self.output_example,
            topic=self.topic,
            problem_hardness=self.problem_hardness
        )

    def test_coding_question_creation(self):
        self.assertEqual(self.coding_question.primary_text, self.primary_text)
        self.assertEqual(self.coding_question.input_text, self.input_text)
        self.assertEqual(self.coding_question.output_text, self.output_text)
        self.assertEqual(self.coding_question.input_example, self.input_example)
        self.assertEqual(self.coding_question.output_example, self.output_example)
        self.assertEqual(self.coding_question.topic, self.topic)
        self.assertEqual(self.coding_question.problem_hardness, self.problem_hardness)


class TestCasesTestCase(TestCase):
    test_case_input: str = "jashanpreet singh"
    test_case_output: str = "Jashanpreet singh"

    def setUp(self):
        self.key = CodingQuestions.objects.create(primary_text="hello soneo", input_text="hello soneo",
                                                 output_text="hello soneo", input_example="jea",
                                                 output_example="jes", topic="yus", problem_hardness=1)
        self.test_cases = TestCases.objects.create(key=self.key, test_case_input=self.test_case_input,
                                                  test_case_output=self.test_case_output, )

    def test_test_case_creation(self):
        self.assertEqual(self.test_cases.key, self.key)
        self.assertEqual(self.test_cases.test_case_input, self.test_case_input)
        self.assertEqual(self.test_cases.test_case_output, self.test_case_output)
