try:
    import base64
    from pg import DB

except Exception as e:

    print("Some Modules are missing {}".format(e))


class redshiftClass:
    def __init__(
        self,
        listOfValues,
        noOfChunks,
        databaseName,
        hostUrl,
        portNumber,
        username,
        password,
        redshiftTableName,
    ):
        self.listOfValues = listOfValues
        self.noOfChunks = noOfChunks
        self.databaseName = databaseName
        self.hostUrl = hostUrl
        self.portNumber = portNumber
        self.username = username
        self.password = password
        self.redshiftTableName = redshiftTableName

    @classmethod
    def insertIntoRedshift(self):
        try:
            valuesList = list(self.chunkify())
            databaseObject = DB(
                dbname=self.databaseName,
                host=self.hostUrl,
                port=self.portNumber,
                user=self.username,
                passwd=self.password,
            )
            self.Launcher(valuesList, databaseObject)
            databaseObject.close()
        except Exception as connectionError:
            print("Error: connectRedshift()" + f"{connectionError}")
            exit()

    @classmethod
    def chunkify(self):
        """
        chunkify() will create the chunks of list l by looping till length of list l, creating n number of chunks. 
        :param l: list object
        :param n: integer value reflecting how many chunks has to be created
        :return : yeild the result back to main() listing the chunks of l
        """
        try:
            for index in range(0, len(self.listOfValues), self.noOfChunks):
                yield self.listOfValues[index : index + self.noOfChunks]
        except Exception as err:
            print("Error: chunkify() ", str(err))
            exit()

    @classmethod
    def Launcher(
        self, chunkList, databaseObject,
    ):
        """
        Launcher() will run a multithreading pool to run a thread to call insertDataIntoRedshift() for each no. of data chunks 
        :param chunkList: list object containing list of chunks.
        :param databaseObject: Redshift connection string
        """
        try:
            for chunk in chunkList:
                self.executeInsert(chunk, databaseObject)
        except Exception as err:
            print("Error: launcher()", str(err))
            exit()

    @classmethod
    def executeInsert(self, insertValues, databaseObject):
        try:
            strValues = ",".join(insertValues)
            sql = (
                "INSERT INTO staging."
                + f"{self.redshiftTableName}"
                + " VALUES"
                + f"{strValues}"
            )
            databaseObject.query(sql)
        except Exception as err:
            print("Error: executeInsert()", str(err))
            exit()
