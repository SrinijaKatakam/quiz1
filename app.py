from flask import Flask, render_template
from azure.storage.blob import generate_container_sas, ContainerSasPermissions
from datetime import datetime, timedelta

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

account_name = "sristorageblobcontainer"
account_key = "FnTE/wQ7bffP3go+ZV2erldm9lZe+WAee9kxnQ9pXIosoINJrh6gw0irR8xH87BT+Bg0Eh6C+AeX/vqFYaykdw=="
container_name = "quiz1container"

driver = '{ODBC Driver 17 for SQL Server}'

server_name = 'databasetest3'
database_name = 'test'


server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

username = "srinija"
password = "Texas@123"

@app.route('/')
def page():
    s_image = get_img_url_with_container_sas_token('s.jpg')
    print(s_image)
    return render_template("index.html", s_image = s_image)


def get_img_url_with_container_sas_token(blob_name):
    container_sas_token = generate_container_sas(
        account_name=account_name,
        container_name=container_name,
        account_key=account_key,
        permission=ContainerSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )
    blob_url_with_container_sas_token = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{container_sas_token}"
    return blob_url_with_container_sas_token