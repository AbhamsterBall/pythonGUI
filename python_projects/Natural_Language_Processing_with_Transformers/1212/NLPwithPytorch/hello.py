# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
#
# model_name = "deepset/roberta-base-squad2"
#
# # a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': 'Why is model conversion important?',
#     'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
# }
# res = nlp(QA_input)
# print(res)
#
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
#
# model_name = "deepset/roberta-base-squad2"
#
# # a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': 'Why is model conversion important?',
#     'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
# }
# res = nlp(QA_input)
#
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/tinyroberta-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': '主要内容是什么?',
    'context': "随着网络的普及，使用个人博客的人越来越多，其中的信息也越来越多，在这种背景下，博客成为了一个大型数据库，成为便捷人们寻找问题解决方案的工具，然而数据越多也就意味着寻找真正有用的数据越困难，并且个人博客上的许多信息难以辨别真实性，需要花费大量时间验证。不仅如此，许多个人博客的界面较为杂乱，文字，栏目分类五花八门，一进去就让人眼花缭乱，不具有较强的严谨性与明确的针对性，操作流畅性不强，部分操作较为繁杂，选择过多，让人不知所措。无论从博客的信息有效度，还是其操作界面的实用性来讲，我们都需要一个更为人性化的博客设计，和更为合理的博客优化。个人博客设计的优化与改进，其意义在于能够让开发个人博客的作者更便捷准确地发布博客内容，减少所发内容的错误和冗余，让看博客的读者更加高效地进行反馈与提问，更快更有针对性地得到答复。同时，也让人更加愿意来了解该个人博客的内容，因为设计该博客地主要目的之一是利于读者，方便读者翻阅理解或者说以友善不打扰读者专注度的方式来设计博客。此外，更为重要的是，该博客将自然语言处理与博客进行结合，希望能够在方便作者的同时也能让读者感受到与文章的互动，在文字较多，或者该文字对读者并非非常重要的时候，节约读者的宝贵时间。当然，除了以相对互交性较强的自然语言处理让读者与内容互动，还希望通过较为高效的搜索引擎来让读者可以主动寻找，查询内容。总体而言，人性化的博客设计旨在提高用户体验，简化操作，减少信息过载。为了达成此目的该博客尝试利用开源模型辅助博客评论的处理，辅助读者阅读大量文字，希望读者在不论视觉上还是理解上以及查找效率上都能有较为愉悦的体验。"
}
res = nlp(QA_input)
print(res)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
#
# model_name = "deepset/roberta-base-squad2"
#
# # a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': 'Why is model conversion important?',
#     'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
# }
# res = nlp(QA_input)
#
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
#
# model_name = "deepset/tinyroberta-squad2"
#
# # a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': 'Why is model conversion important?',
#     'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
# }
# res = nlp(QA_input)
# print(res)
#
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)



