import nlpcloud



class API:

    def __init__(self):
        self.client = nlpcloud.Client("gpt-oss-120b", "30f50d791bcaabba3ab81f3dc6ab6be6c47835e8", gpu=True)
        

    def sentiment_analysis(self,para):
        response = self.client.sentiment(para)
        return response
    

    def ner_analysis(self,para):
        response = self.client.entities(para,searched_entity="programming languages")
        return response
    
    def grammar_Correction_analysis(self,para):
        response = self.client.gs_correction(para)
        return response