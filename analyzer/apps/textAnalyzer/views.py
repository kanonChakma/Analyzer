from rest_framework.response import Response
from rest_framework.views import APIView
from transformers import AutoModelForSequenceClassification, AutoTokenizer


class SentimentAnalysisView(APIView):
    def post(self, request):
        text = request.data.get("text")
        if not text:
            return Response({"error": "text is required!!!!"}, status=400)

        try:
            model_name = "StatsGary/setfit-ft-sentinent-eval"
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)

            # Tokenize
            inputs = tokenizer.encode_plus(text, add_special_tokens=True, return_tensors="pt")

            # Perform sentiment analysis
            outputs = model(**inputs)
            predicted_label = outputs.logits.argmax(dim=1).item()

            sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}
            sentiment = sentiment_map.get(predicted_label, "")

            response_data = {"sentiment": sentiment}
            return Response(response_data)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
