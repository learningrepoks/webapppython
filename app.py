from flask import Flask, jsonify
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

app = Flask(__name__)

# Azure authentication
subscription_id = "ea54ae54-f0c0-4c82-9dff-935d60afa91d"
credential = DefaultAzureCredential(managed_identity_client_id="21a0792a-71c0-452e-9467-40613d7f524e")
storage_client = StorageManagementClient(credential, subscription_id)


@app.route("/")
def homepage():
    return "homepage"

@app.route("/storage-accounts")
# def list_storage_accounts():
#     return "sai"
def list_storage_accounts():
    accounts = storage_client.storage_accounts.list()
    storage_list = [{"name": acc.name, "location": acc.location} for acc in accounts]
    return jsonify(storage_list)

if __name__ == "__main__":
    app.run(debug=True)