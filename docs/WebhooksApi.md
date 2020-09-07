# gitee.WebhooksApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo_hooks_id**](WebhooksApi.md#delete_v5_repos_owner_repo_hooks_id) | **DELETE** /v5/repos/{owner}/{repo}/hooks/{id} | 删除一个仓库WebHook
[**get_v5_repos_owner_repo_hooks**](WebhooksApi.md#get_v5_repos_owner_repo_hooks) | **GET** /v5/repos/{owner}/{repo}/hooks | 列出仓库的WebHooks
[**get_v5_repos_owner_repo_hooks_id**](WebhooksApi.md#get_v5_repos_owner_repo_hooks_id) | **GET** /v5/repos/{owner}/{repo}/hooks/{id} | 获取仓库单个WebHook
[**patch_v5_repos_owner_repo_hooks_id**](WebhooksApi.md#patch_v5_repos_owner_repo_hooks_id) | **PATCH** /v5/repos/{owner}/{repo}/hooks/{id} | 更新一个仓库WebHook
[**post_v5_repos_owner_repo_hooks**](WebhooksApi.md#post_v5_repos_owner_repo_hooks) | **POST** /v5/repos/{owner}/{repo}/hooks | 创建一个仓库WebHook
[**post_v5_repos_owner_repo_hooks_id_tests**](WebhooksApi.md#post_v5_repos_owner_repo_hooks_id_tests) | **POST** /v5/repos/{owner}/{repo}/hooks/{id}/tests | 测试WebHook是否发送成功

# **delete_v5_repos_owner_repo_hooks_id**
> delete_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)

删除一个仓库WebHook

删除一个仓库WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个仓库WebHook
    api_instance.delete_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_v5_repos_owner_repo_hooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_hooks**
> list[Hook] get_v5_repos_owner_repo_hooks(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出仓库的WebHooks

列出仓库的WebHooks

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出仓库的WebHooks
    api_response = api_instance.get_v5_repos_owner_repo_hooks(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_v5_repos_owner_repo_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Hook]**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_hooks_id**
> Hook get_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)

获取仓库单个WebHook

获取仓库单个WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库单个WebHook
    api_response = api_instance.get_v5_repos_owner_repo_hooks_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_v5_repos_owner_repo_hooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_hooks_id**
> Hook patch_v5_repos_owner_repo_hooks_id(access_token, url, password, push_events, tag_push_events, issues_events, note_events, merge_requests_events, owner, repo, id)

更新一个仓库WebHook

更新一个仓库WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
access_token = 'access_token_example' # str | 
url = 'url_example' # str | 
password = 'password_example' # str | 
push_events = true # bool | 
tag_push_events = true # bool | 
issues_events = true # bool | 
note_events = true # bool | 
merge_requests_events = true # bool | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID

try:
    # 更新一个仓库WebHook
    api_response = api_instance.patch_v5_repos_owner_repo_hooks_id(access_token, url, password, push_events, tag_push_events, issues_events, note_events, merge_requests_events, owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->patch_v5_repos_owner_repo_hooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **url** | **str**|  | 
 **password** | **str**|  | 
 **push_events** | **bool**|  | 
 **tag_push_events** | **bool**|  | 
 **issues_events** | **bool**|  | 
 **note_events** | **bool**|  | 
 **merge_requests_events** | **bool**|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_hooks**
> Hook post_v5_repos_owner_repo_hooks(body, owner, repo)

创建一个仓库WebHook

创建一个仓库WebHook

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
body = gitee.Body40() # Body40 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)

try:
    # 创建一个仓库WebHook
    api_response = api_instance.post_v5_repos_owner_repo_hooks(body, owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->post_v5_repos_owner_repo_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body40**](Body40.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_hooks_id_tests**
> post_v5_repos_owner_repo_hooks_id_tests(owner, repo, id, body=body)

测试WebHook是否发送成功

测试WebHook是否发送成功

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.WebhooksApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
body = gitee.Body42() # Body42 |  (optional)

try:
    # 测试WebHook是否发送成功
    api_instance.post_v5_repos_owner_repo_hooks_id_tests(owner, repo, id, body=body)
except ApiException as e:
    print("Exception when calling WebhooksApi->post_v5_repos_owner_repo_hooks_id_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **body** | [**Body42**](Body42.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

