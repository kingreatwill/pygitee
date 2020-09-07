# gitee.EmailsApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_emails**](EmailsApi.md#get_v5_emails) | **GET** /v5/emails | 获取授权用户的全部邮箱

# **get_v5_emails**
> UserEmail get_v5_emails(access_token=access_token)

获取授权用户的全部邮箱

获取授权用户的全部邮箱

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EmailsApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户的全部邮箱
    api_response = api_instance.get_v5_emails(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailsApi->get_v5_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**UserEmail**](UserEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

