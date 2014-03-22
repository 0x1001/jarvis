import speak

print speak.sentenceToNumbers("how are you".split(" "))
print speak.numbersToSentence([134, 356, 578])

print speak.sentenceToNumbers("hello world".split(" "))

import jarvis

he = jarvis.Jarvis()
he.train()
print he.understand("how are you")
