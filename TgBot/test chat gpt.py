import openai

openai.api_key = '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'
engine="text-davinci-003"

prompt = str('СФОРМИРУЮЙ ТЕСТОВОЕ ЗАДАНИЕ ДЛЯ PYTHON JUNIOR РАЗРАБОТЧИКА')
completion = openai.Completion.create(engine=engine,
                                      prompt=prompt,
                                      temperature=0.5,
                                      max_tokens=4000)
print('\nОтвет:')
print( completion.choices[0]['text'] )
