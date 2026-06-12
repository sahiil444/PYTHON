import nlpcloud



class API:

    def __init__(self):
        self.client = nlpcloud.Client("gpt-oss-120b", "09d6a6394e07c15b984dc4b90ef0de12834d88ca", gpu=True)
        

    def sentiment_analysis(self,para):
        response = self.client.sentiment(para)
        return response
    

    def ner_analysis(self,para):
        response = self.client.entities(para,searched_entity="programming languages")
        return response
    
    def grammar_Correction_analysis(self,para):
        response = self.client.gs_correction(para)
        return response