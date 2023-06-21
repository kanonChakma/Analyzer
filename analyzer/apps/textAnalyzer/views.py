from rest_framework.response import Response
from rest_framework.views import APIView
from transformers import pipeline

# class SentimentAnalysisViewOne(APIView):
#     def post(self, request):
#         text = request.data.get("text")
#         if not text:
#             return Response({"error": "Text parameter is required."}, status=400)

#         try:
#             model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
#             predictions = model([text])
#             sentiment = predictions[0]
#             return Response({"sentiment": sentiment})

#         except Exception as e:
#             return Response({"error": str(e)}, status=500)


class SentimentAnalysisView(APIView):
    def post(self, request):
        text = request.data.get("text")
        if not text:
            return Response({"error": "Text parameter is required."}, status=400)

        try:
            model_name = "StatsGary/setfit-ft-sentinent-eval"
            sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
            result = sentiment_analyzer(text)[0]
            sentiment_label = result["label"]
            sentiment_score = result["score"]

            response_data = {"sentiment": sentiment_label, "score": sentiment_score}

            return Response(response_data)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
