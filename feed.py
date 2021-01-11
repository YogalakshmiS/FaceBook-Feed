import facebook

page_access_token = "EAADc7r5ZAwnIBAHEuoiIzurO7Oh9EEzi7ZC4sERnw8T1iMPbSJN7a1KDSS3h58FXFUVNNZAsyHEV6J36QkITNkNg25bwSLMZBZAAFXbmOqigtpXUTaaaXeKH7HxW8y5ZBN7G3QznqUNcOJTgQj0g4XHXmo8wxHh6Un6obkoVREeKFLCJiQikUtex8osObDhsAZCTQ7zY2TZAZCGaIeDGzpTRK"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "103388865059550"
graph.put_object(facebook_page_id, "feed", message='Hello All')
