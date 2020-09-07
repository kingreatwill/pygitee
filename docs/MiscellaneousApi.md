# gitee.MiscellaneousApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_emojis**](MiscellaneousApi.md#get_v5_emojis) | **GET** /v5/emojis | 列出可使用的 Emoji
[**get_v5_gitignore_templates**](MiscellaneousApi.md#get_v5_gitignore_templates) | **GET** /v5/gitignore/templates | 列出可使用的 .gitignore 模板
[**get_v5_gitignore_templates_name**](MiscellaneousApi.md#get_v5_gitignore_templates_name) | **GET** /v5/gitignore/templates/{name} | 获取一个 .gitignore 模板
[**get_v5_gitignore_templates_name_raw**](MiscellaneousApi.md#get_v5_gitignore_templates_name_raw) | **GET** /v5/gitignore/templates/{name}/raw | 获取一个 .gitignore 模板原始文件
[**get_v5_licenses**](MiscellaneousApi.md#get_v5_licenses) | **GET** /v5/licenses | 列出可使用的开源许可协议
[**get_v5_licenses_license**](MiscellaneousApi.md#get_v5_licenses_license) | **GET** /v5/licenses/{license} | 获取一个开源许可协议
[**get_v5_licenses_license_raw**](MiscellaneousApi.md#get_v5_licenses_license_raw) | **GET** /v5/licenses/{license}/raw | 获取一个开源许可协议原始文件
[**get_v5_repos_owner_repo_license**](MiscellaneousApi.md#get_v5_repos_owner_repo_license) | **GET** /v5/repos/{owner}/{repo}/license | 获取一个仓库使用的开源许可协议
[**post_v5_markdown**](MiscellaneousApi.md#post_v5_markdown) | **POST** /v5/markdown | 渲染 Markdown 文本

# **get_v5_emojis**
> get_v5_emojis(access_token=access_token)

列出可使用的 Emoji

列出可使用的 Emoji

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出可使用的 Emoji
    api_instance.get_v5_emojis(access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_emojis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gitignore_templates**
> get_v5_gitignore_templates(access_token=access_token)

列出可使用的 .gitignore 模板

列出可使用的 .gitignore 模板

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出可使用的 .gitignore 模板
    api_instance.get_v5_gitignore_templates(access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_gitignore_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gitignore_templates_name**
> get_v5_gitignore_templates_name(name, access_token=access_token)

获取一个 .gitignore 模板

获取一个 .gitignore 模板

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
name = 'name_example' # str | .gitignore 模板名
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个 .gitignore 模板
    api_instance.get_v5_gitignore_templates_name(name, access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_gitignore_templates_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| .gitignore 模板名 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_gitignore_templates_name_raw**
> get_v5_gitignore_templates_name_raw(name, access_token=access_token)

获取一个 .gitignore 模板原始文件

获取一个 .gitignore 模板原始文件

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
name = 'name_example' # str | .gitignore 模板名
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个 .gitignore 模板原始文件
    api_instance.get_v5_gitignore_templates_name_raw(name, access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_gitignore_templates_name_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| .gitignore 模板名 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_licenses**
> get_v5_licenses(access_token=access_token)

列出可使用的开源许可协议

列出可使用的开源许可协议

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出可使用的开源许可协议
    api_instance.get_v5_licenses(access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_licenses_license**
> get_v5_licenses_license(license, access_token=access_token)

获取一个开源许可协议

获取一个开源许可协议

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
license = 'license_example' # str | 协议名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个开源许可协议
    api_instance.get_v5_licenses_license(license, access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_licenses_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**| 协议名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_licenses_license_raw**
> get_v5_licenses_license_raw(license, access_token=access_token)

获取一个开源许可协议原始文件

获取一个开源许可协议原始文件

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
license = 'license_example' # str | 协议名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个开源许可协议原始文件
    api_instance.get_v5_licenses_license_raw(license, access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_licenses_license_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**| 协议名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_license**
> get_v5_repos_owner_repo_license(owner, repo, access_token=access_token)

获取一个仓库使用的开源许可协议

获取一个仓库使用的开源许可协议

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个仓库使用的开源许可协议
    api_instance.get_v5_repos_owner_repo_license(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_v5_repos_owner_repo_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_markdown**
> post_v5_markdown(body)

渲染 Markdown 文本

渲染 Markdown 文本

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MiscellaneousApi()
body = gitee.Body67() # Body67 | 

try:
    # 渲染 Markdown 文本
    api_instance.post_v5_markdown(body)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->post_v5_markdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body67**](Body67.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

