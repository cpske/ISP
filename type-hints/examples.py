"""Example type hints."""

from collections.abc import Any, Dict, Sequence

data: Dict[str, Dict[str, Any]] = {'1': {'question_id': 1,
                                         'question_text': "How are you?",
                                         'answer': None
                                        }
                                  }

seq: Sequence[int] = [0, 0.5, 1, 2]
