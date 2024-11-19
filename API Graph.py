import json
import facebook
import requests

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType

def main():
    token = {"EAARuRmilOKgBAC0azRPwnZBQWW0reQ5Cn6QZBRaMtEROlZBkPIJVC44KJgt7AzfKrTnhWYAGe1DO06ZBZAsdb1OpHRhC15rDUBGmRBl1bAt3VyVw1qUjp7wts3wfwvAsLg6te2MziAXgH6DQV749I1txA3AJaRZAVOHrUDrOjNTjxyI8QexXkgTieShNwFVfnqx6IGZCT0NQpMSDT1YvJQd"}
    graph = facebook.GraphAPI(token)

    fields = ['link, picture']

    #profile = graph.get_object('me', fields = fields)
    page = graph.get_object("EricCisnerosB", fields = fields)

    print(json.dumps(page, indent=4))

    workbook = Workbook(FileFormatType.XLSX)
    workbook.getWorksheets().get(0).getCells().get("A1").putValue(json.dumps(page))
    workbook.save("APIGraphPage.xlsx")

    jpype.shutdownJVM()

if  __name__ == "__main__":
    main()
