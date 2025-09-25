from phishing_detector.model import predict_url

def test_predict_url_returns_valid_label():
    """
    Test that the predict_url function returns either 'Phishing' or 'Legitimate'
    when given a sample URL.
    """
    sample_url = "http://example.com"
    prediction = predict_url(sample_url)
    
    # The prediction should be either 'Phishing' or 'Legitimate'
    assert prediction in ["Phishing", "Legitimate"]
