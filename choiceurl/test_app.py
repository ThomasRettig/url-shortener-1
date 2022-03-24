from urlshort import create_app
#perform one test on the shorten button
def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data