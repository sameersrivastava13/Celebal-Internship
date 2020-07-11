try:
    import json
    import base64
    import boto3
    from botocore.exceptions import ClientError

except Exception as e:

    print("Some Modules are missing {}".format(e))


class secretManagerClass:
    def __init__(self, secretName, regionName):
        self.secretName = secretName
        self.regionName = regionName


    def getSecretFromSecretManager(self):
        session = boto3.session.Session()
        client = session.client(
            service_name="secretsmanager", region_name=self.regionName
        )
        try:
            getSecretValueResponse = client.get_secret_value(SecretId=self.secretName)
            if "SecretString" in getSecretValueResponse:
                return json.loads(getSecretValueResponse["SecretString"])
            else:
                raise ValueError("SecretString not found in reponse")
        except Exception as err:
            print("Error:getSecretFromSecretManager()", str(err))
            exit()
