from polls.models import *
from django.utils import timezone
import datetime

pubdate = timezone.now() + datetime.timedelta(days=180)

print("Create a question published on", pubdate)

q = Question.objects.create(question_text="Published when?", pub_date=pubdate)

print("Question is")
print(q.id)
print(q.question_text)
print(q.pub_date)

q.delete()
