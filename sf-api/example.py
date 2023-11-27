from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc7523 import PrivateKeyJWT

token_url = "https://oidc.nersc.gov/c2id/token"
client_id = "eu2ajfe5zyqfs"
private_key = open("/workspaces/superfacility/sf-api/key/red/priv_key.pem").read()

session = OAuth2Session(
    client_id, 
    private_key, 
    PrivateKeyJWT(token_url),
    grant_type="client_credentials",
    token_endpoint=token_url
)
session.fetch_token()


def check_systems():
    system = "perlmutter"
    verb = "status"
    url = f"https://api.nersc.gov/api/v1.2/{verb}/{system}"
    resp = session.get(url)
    json = resp.json()
    # indent=2 for pretty print of json response 
    print(json)


def list_directories():
    system = "perlmutter"
    dir = "/global/homes/j/jlabtsai"
    verb = "utilities/ls"
    url = f"https://api.nersc.gov/api/v1.2/{verb}/{system}/{dir}"
    resp = session.get(url)
    json = resp.json()
    # indent=2 for pretty print of json response 
    print(json)


if __name__ == "__main__":
    check_systems()
    list_directories()

