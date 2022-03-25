from urlshort import create_app
#perform one test on the shorten button
def test_shorten(client):
    #get the home page and test shorten button
    response = client.get('/')
    assert b'Shorten' in response.data
