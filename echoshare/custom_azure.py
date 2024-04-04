from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name ="echosharestorage"#os.getenv('AZURE_ACCOUNT_NAME') # Must be replaced by your <storage_account_name>
    account_key = "CjbkS5CsVbse2xpVvgZc0OA27RBHXFfUf+o8hp7zkozKX/knk9iXhErrg1FQLu7hqkaGNduGIY5Y+AStBOIicg=="#os.getenv('AZURE_ACCOUNT_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = "echosharestorage"# os.getenv('AZURE_ACCOUNT_NAME') # Must be replaced by your storage_account_name
    account_key = "CjbkS5CsVbse2xpVvgZc0OA27RBHXFfUf+o8hp7zkozKX/knk9iXhErrg1FQLu7hqkaGNduGIY5Y+AStBOIicg=="#os.getenv('AZURE_ACCOUNT_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None