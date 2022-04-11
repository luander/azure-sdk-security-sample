# SDK Authentication

Make sure you have enough permissions to create a new Service Principal. You may need to escalate your privileges through PIM.

## Authentication via a Service Principal
```bash
az ad sp create-for-rbac --name azenergylabeler-security-reader --role "Security Reader" --scopes /subscriptions/<subscription-id>

The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "aa11bb33-cc77-dd88-ee99-0918273645aa",
  "displayName": "azenergylabeler-security-reader",
  "password": "REDACTED",
  "tenant": "2aa11bb33-cc77-dd88-ee99-0918273645aa"
}
```

Configure environment variables:

```
export AZURE_SUBSCRIPTION_ID="aa11bb33-cc77-dd88-ee99-0918273645aa"
export AZURE_TENANT_ID=00112233-7777-8888-9999-aabbccddeeff
export AZURE_CLIENT_ID=12345678-1111-2222-3333-1234567890ab
export AZURE_CLIENT_SECRET=oUBB11zz~JJJJ_~yyyyyyVVumumumumb_b
```

Then in code:
```python
from azure.mgmt.security import SecurityCenter
from azure.identity import ClientSecretCredential
import os

subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']

credential = ClientSecretCredential(tenant_id, client_id, client_secret)

sc = SecurityCenter(credential, subscription_id, 'westeurope')
```

## Authentication via CLI
```bash
az login --tenant <tenant_id>
az account show
```

Then in code:
```python
from azure.mgmt.security import SecurityCenter
from azure.identity import AzureCliCredential
import os
import json

credential = AzureCliCredential()

sc = SecurityCenter(credential, subscription_id, 'westeurope')
```


# SecurityCenter documentation
<https://docs.microsoft.com/en-us/python/api/azure-mgmt-security/azure.mgmt.security.securitycenter?view=azure-python>

# Sample code

```python
from azure.mgmt.security import SecurityCenter
from azure.identity import AzureCliCredential, ClientSecretCredential
import os
import json

# credential = AzureCliCredential()
subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']

credential = ClientSecretCredential(tenant_id, client_id, client_secret)

sc = SecurityCenter(credential, subscription_id, 'westeurope')

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
```


