try:
    import requests
    import json
    import pandas as pd
    import bs4

except Exception as e:
    print("Some modules are missing {}".format(e))


df = pd.DataFrame()
di = {}


def get_data_api(url, li):
    response = requests.get(url)
    response_json = response.json()
    for i in li:
        info_request = response_json[i]
        print(info_request)
        di.update(info_request)
        print(di)

    with open("data.txt", "w") as outfile:
        json.dump(di, outfile)

    df = pd.read_json("data.txt")
    df.to_csv("new_data.csv", index=False)


if __name__ == "__main__":

    li = ["request", "location", "current"]
    url = " http://api.weatherstack.com/current?access_key=446acc2ff4bce70bc61ab56a58dc97fe&%20query=New%20York"
    get_data_api(url, li)
    # print("Data received waiting for 5 minutes..")

    # sleep for 5 minutes
