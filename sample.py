from azure.mgmt.security import SecurityCenter
from azure.identity import AzureCliCredential, ClientSecretCredential
import os
import json

# credential = AzureCliCredential()
subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']

client = ClientSecretCredential(tenant_id, client_id, client_secret)

sc = SecurityCenter(client, subscription_id, 'westeurope')

print('==== Security Contacts ====')
for contact in sc.security_contacts.list():
    print(f'name: {contact.name}')
    print(f'email: {contact.email}')
    print(f'phone: {contact.phone}')
    print()


print('==== Secure Scores ====')
for score in sc.secure_scores.list():
    print(f'name: {score.display_name}')
    print(f'percentage: {score.percentage}')
    print(f'details: \n\tweight: {score.weight} \n\tmax: {score.max}\n\tcurrent:{score.current}')
    print()

print('==== Compliance Results ====')
for standard in sc.regulatory_compliance_standards.list():
    print(f'name: {standard.name}')
    print(f'state: {standard.state}')
    print(f'{standard.passed_controls} passed')
    print(f'{standard.failed_controls} failed')
    print(f'{standard.skipped_controls} skipped')
    print(f'{standard.unsupported_controls} unsupported')
    print()
