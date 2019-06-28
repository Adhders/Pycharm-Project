
#Extract keywords
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
# keyword_processor.add_keyword(<unclean name>, <standardised name>)
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
print(keywords_found)

#Replace keywords
keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
print(new_sentence)

#Case Sensitive example
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor(case_sensitive=True)
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
print(keywords_found)

#Span of keywords extracted
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.', span_info=True)
print(keywords_found)

#Get Extra information with keywords extracted
from flashtext import KeywordProcessor
kp = KeywordProcessor()
kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
kp.add_keyword('Delhi', ('Location', 'Delhi'))
kp.extract_keywords('Taj Mahal is in Delhi.')

# NOTE: replace_keywords feature won't work with this.
#
#No clean name for Keywords
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
print(keywords_found)

#Add Multiple Keywords simultaneously
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_dict = {
  "java": ["java_2e", "java programing"],
  "product management": ["PM", "product manager"]
}

keyword_processor.add_keywords_from_dict(keyword_dict)
# Or add keywords from a list:
keyword_processor.add_keywords_from_list(["java", "python"])
keyword_processor.extract_keywords('I am a product manager for a java_2e platform')

#To Remove keywords
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_dict = {
  "java": ["java_2e", "java programing"],
  "product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)
print(keyword_processor.extract_keywords('I am a product manager for a java_2e platform'))
# output ['product management', 'java']
keyword_processor.remove_keyword('java_2e')
# you can also remove keywords from a list/ dictionary
keyword_processor.remove_keywords_from_dict({"product management": ["PM"]})
keyword_processor.remove_keywords_from_list(["java programing"])
keyword_processor.extract_keywords('I am a product manager for a java_2e platform')

#To check Number of terms in KeywordProcessor
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_dict = {
  "java": ["java_2e", "java programing"],
  "product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)
print(len(keyword_processor))

#To check if term is present in KeywordProcessor
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('j2ee', 'Java')

#'j2ee' in keyword_processor
# output: True
keyword_processor.get_keyword('j2ee')
# output: Java
keyword_processor['colour'] = 'color'
print(keyword_processor['colour'])

#Get all keywords in dictionary
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('j2ee', 'Java')
keyword_processor.add_keyword('colour', 'color')
keyword_processor.get_all_keywords()

#For detecting Word Boundary currently any character other than this \w [A-Za-z0-9_] is considered a word boundary.

#To set or add characters as part of word characters
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple')
print(keyword_processor.extract_keywords('I love Big Apple/Bay Area.'))

keyword_processor.add_non_word_boundary('/')
print(keyword_processor.extract_keywords('I love Big Apple/Bay Area.'))
