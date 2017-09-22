from unittest import TestCase

from spellingskill.spellingskill import SpellingSkill


class BaseTest(TestCase):

    def setUp(self):
        self.skill = SpellingSkill()


class SpellingSkillTest(BaseTest):
    def test_basic(self):
        results = self.skill.spell("word")
        self.assertEqual(results, "w o r d")
