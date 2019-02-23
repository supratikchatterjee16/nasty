import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


install('pymongo')
install('nltk')
install('feedparser')
install('numpy')
install('sympy')
install('scipy')
install('matplotlib')
install('beautifulsoup4')
install('requests')
install('lxml')

import nltk
nltk.download('all')
