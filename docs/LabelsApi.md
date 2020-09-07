# gitee.LabelsApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo_issues_number_labels**](LabelsApi.md#delete_v5_repos_owner_repo_issues_number_labels) | **DELETE** /v5/repos/{owner}/{repo}/issues/{number}/labels | 删除Issue所有标签
[**delete_v5_repos_owner_repo_issues_number_labels_name**](LabelsApi.md#delete_v5_repos_owner_repo_issues_number_labels_name) | **DELETE** /v5/repos/{owner}/{repo}/issues/{number}/labels/{name} | 删除Issue标签
[**delete_v5_repos_owner_repo_labels_name**](LabelsApi.md#delete_v5_repos_owner_repo_labels_name) | **DELETE** /v5/repos/{owner}/{repo}/labels/{name} | 删除一个仓库任务标签
[**get_v5_enterprises_enterprise_labels**](LabelsApi.md#get_v5_enterprises_enterprise_labels) | **GET** /v5/enterprises/{enterprise}/labels | 获取企业所有标签
[**get_v5_enterprises_enterprise_labels_name**](LabelsApi.md#get_v5_enterprises_enterprise_labels_name) | **GET** /v5/enterprises/{enterprise}/labels/{name} | 获取企业某个标签
[**get_v5_repos_owner_repo_issues_number_labels**](LabelsApi.md#get_v5_repos_owner_repo_issues_number_labels) | **GET** /v5/repos/{owner}/{repo}/issues/{number}/labels | 获取仓库任务的所有标签
[**get_v5_repos_owner_repo_labels**](LabelsApi.md#get_v5_repos_owner_repo_labels) | **GET** /v5/repos/{owner}/{repo}/labels | 获取仓库所有任务标签
[**get_v5_repos_owner_repo_labels_name**](LabelsApi.md#get_v5_repos_owner_repo_labels_name) | **GET** /v5/repos/{owner}/{repo}/labels/{name} | 根据标签名称获取单个标签
[**patch_v5_repos_owner_repo_labels_original_name**](LabelsApi.md#patch_v5_repos_owner_repo_labels_original_name) | **PATCH** /v5/repos/{owner}/{repo}/labels/{original_name} | 更新一个仓库任务标签
[**post_v5_repos_owner_repo_issues_number_labels**](LabelsApi.md#post_v5_repos_owner_repo_issues_number_labels) | **POST** /v5/repos/{owner}/{repo}/issues/{number}/labels | 创建Issue标签
[**post_v5_repos_owner_repo_labels**](LabelsApi.md#post_v5_repos_owner_repo_labels) | **POST** /v5/repos/{owner}/{repo}/labels | 创建仓库任务标签
[**put_v5_repos_owner_repo_issues_number_labels**](LabelsApi.md#put_v5_repos_owner_repo_issues_number_labels) | **PUT** /v5/repos/{owner}/{repo}/issues/{number}/labels | 替换Issue所有标签

# **delete_v5_repos_owner_repo_issues_number_labels**
> delete_v5_repos_owner_repo_issues_number_labels(owner, repo, number, access_token=access_token)

删除Issue所有标签

删除Issue所有标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Issue所有标签
    api_instance.delete_v5_repos_owner_repo_issues_number_labels(owner, repo, number, access_token=access_token)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_v5_repos_owner_repo_issues_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_issues_number_labels_name**
> delete_v5_repos_owner_repo_issues_number_labels_name(owner, repo, number, name, access_token=access_token)

删除Issue标签

删除Issue标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Issue标签
    api_instance.delete_v5_repos_owner_repo_issues_number_labels_name(owner, repo, number, name, access_token=access_token)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_v5_repos_owner_repo_issues_number_labels_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_labels_name**
> delete_v5_repos_owner_repo_labels_name(owner, repo, name, access_token=access_token)

删除一个仓库任务标签

删除一个仓库任务标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个仓库任务标签
    api_instance.delete_v5_repos_owner_repo_labels_name(owner, repo, name, access_token=access_token)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_v5_repos_owner_repo_labels_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_labels**
> list[Label] get_v5_enterprises_enterprise_labels(enterprise, access_token=access_token)

获取企业所有标签

获取企业所有标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业所有标签
    api_response = api_instance.get_v5_enterprises_enterprise_labels(enterprise, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_v5_enterprises_enterprise_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_labels_name**
> Label get_v5_enterprises_enterprise_labels_name(enterprise, name, access_token=access_token)

获取企业某个标签

获取企业某个标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业某个标签
    api_response = api_instance.get_v5_enterprises_enterprise_labels_name(enterprise, name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_v5_enterprises_enterprise_labels_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_issues_number_labels**
> list[Label] get_v5_repos_owner_repo_issues_number_labels(owner, repo, number, access_token=access_token)

获取仓库任务的所有标签

获取仓库任务的所有标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库任务的所有标签
    api_response = api_instance.get_v5_repos_owner_repo_issues_number_labels(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_v5_repos_owner_repo_issues_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_labels**
> list[Label] get_v5_repos_owner_repo_labels(owner, repo, access_token=access_token)

获取仓库所有任务标签

获取仓库所有任务标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库所有任务标签
    api_response = api_instance.get_v5_repos_owner_repo_labels(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_v5_repos_owner_repo_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_labels_name**
> Label get_v5_repos_owner_repo_labels_name(owner, repo, name, access_token=access_token)

根据标签名称获取单个标签

根据标签名称获取单个标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 根据标签名称获取单个标签
    api_response = api_instance.get_v5_repos_owner_repo_labels_name(owner, repo, name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_v5_repos_owner_repo_labels_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_labels_original_name**
> Label patch_v5_repos_owner_repo_labels_original_name(owner, repo, original_name, access_token=access_token, name=name, color=color)

更新一个仓库任务标签

更新一个仓库任务标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
original_name = 'original_name_example' # str | 标签原有名称
access_token = 'access_token_example' # str |  (optional)
name = 'name_example' # str |  (optional)
color = 'color_example' # str |  (optional)

try:
    # 更新一个仓库任务标签
    api_response = api_instance.patch_v5_repos_owner_repo_labels_original_name(owner, repo, original_name, access_token=access_token, name=name, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->patch_v5_repos_owner_repo_labels_original_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **original_name** | **str**| 标签原有名称 | 
 **access_token** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **color** | **str**|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_issues_number_labels**
> Label post_v5_repos_owner_repo_issues_number_labels(owner, repo, number, body=body)

创建Issue标签

创建Issue标签  需要在请求的body里填上数组，元素为标签的名字。如: [\"performance\", \"bug\"]

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = gitee.Body11() # Body11 |  (optional)

try:
    # 创建Issue标签
    api_response = api_instance.post_v5_repos_owner_repo_issues_number_labels(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->post_v5_repos_owner_repo_issues_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_labels**
> Label post_v5_repos_owner_repo_labels(body, owner, repo)

创建仓库任务标签

创建仓库任务标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
body = gitee.Body8() # Body8 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)

try:
    # 创建仓库任务标签
    api_response = api_instance.post_v5_repos_owner_repo_labels(body, owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->post_v5_repos_owner_repo_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_issues_number_labels**
> Label put_v5_repos_owner_repo_issues_number_labels(owner, repo, number, body=body)

替换Issue所有标签

替换Issue所有标签  需要在请求的body里填上数组，元素为标签的名字。如: [\"performance\", \"bug\"]

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.LabelsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = gitee.Body10() # Body10 |  (optional)

try:
    # 替换Issue所有标签
    api_response = api_instance.put_v5_repos_owner_repo_issues_number_labels(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->put_v5_repos_owner_repo_issues_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

