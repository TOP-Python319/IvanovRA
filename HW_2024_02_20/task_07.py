# Task_07

text = input(': ')

symbols =  '.,:;!?–—\'\"()*/'

sentences = ''.join(word for word in text if word not in symbols)
print(sentences)
    
# Ввод_1:
#   Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; 
#   он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, 
#   что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.

# Вывод_1:
#   Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство 
#   он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль 
#   что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита