try:
    import requests
    import json
    from pandas import DataFrame

except Exception as e:
    print("Some modules are missing {}".format(e))


def get_data_api(url):
    response = requests.get(url)
    response_json = response.json()

    info_request = response_json["request"]

    info_location = response_json["location"]
    info_current = response_json["current"]

    df1 = DataFrame(
        list(info_request.keys()), list(info_request.values()), columns=["Attributes"]
    )
    df2 = DataFrame(
        list(info_location.keys()), list(info_location.values()), columns=["Attributes"]
    )
    df3 = DataFrame(
        list(info_current.keys()), list(info_current.values()), columns=["Attributes"]
    )

    result_df = df1.append(df2).append(df3)

    result_df.to_csv("received_file.csv", index_label="Data")
    print("printed")



if __name__ == "__main__":

    url = " "
    get_data_api(url)
    print("Data received waiting for 5 minutes..")

        # sleep for 5 minutes


